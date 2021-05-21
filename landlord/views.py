from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apartment.models import Apartment
from unit.models import Unit, AllocateTenantUnit
from users.decorators import allowed_users, admin_only
from django.shortcuts import redirect, render, get_object_or_404

# from apartment.models import Apartment
from landlord.forms import AddLandlordForm
from landlord.models import Landlord

# from bill.models import Unit
from users.models import CustomUser


@login_required(login_url='login')
# @admin_only.count()

    # vacants = Unit.objects.filter(confirm_allocation=False)[:3]

    # tenant_order = CustomUser.objects.filter(is_tenant=True)
    # tenant_orders = tenant_orde
def dashboard(request):
    occupied = Unit.objects.filter(confirm_allocation=True)
    occupied_units_count = occupied.count()

    vacant = Unit.objects.filter(confirm_allocation=False)
    vacant_units_count = vacant.count()

    vacants = Unit.objects.filter(confirm_allocation=False)[:3]

    tenant_order = CustomUser.objects.filter(is_tenant=True)
    tenant_orders = tenant_order.order_by('-date_joined')[:3]

    tenants = CustomUser.objects.filter(is_tenant=True)
    tenants_registered = tenants.count()

    landlords = Landlord.objects.all()
    landlords_registered = landlords.count()

    apartments = Apartment.objects.all()
    apartments_registered = apartments.count()

    units = Unit.objects.all()

    units_registered = units.count()

    context = {'vacant_units_count': vacant_units_count, 'occupied_units_count': occupied_units_count,
               'vacant': vacant, 'vacants': vacants, 'occupied': occupied,
               'tenants': tenants, 'landlords': landlords, 'apartments': apartments,
               'units': units, 'tenants_registered': tenants_registered,
               'landlords_registered': landlords_registered, 'tenant_orders': tenant_orders,
               'units_registered': units_registered, 'apartments_registered': apartments_registered}
    return render(request, 'landlord/home.html', context)


@login_required(login_url='login')
@allowed_users
def list_landlords(request):
    context = {
        'landlords': Landlord.objects.all()
    }

    return render(request, 'landlord/landlord_list.html', context)


@login_required(login_url='login')
@allowed_users
def add_landlord(request):
    context = {}
    form = AddLandlordForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Landlord Registered Successfully')
        return redirect('add-landlord')
    else:
        context['form'] = form
    return render(request, 'landlord/landlord_add.html', context)


@login_required(login_url='login')
@allowed_users
def landlord_detail_view(request, pk):
    landlord = get_object_or_404(Landlord, pk=pk)
    apartments = landlord.owner.all()
    apartments_count = apartments.count()
    context = {'landlord': landlord, 'apartments': apartments,
               'apartments_count': apartments_count}
    return render(request, 'landlord/landlord_detail.html', context)


@login_required(login_url='login')
@allowed_users
def landlord_update_view(request, pk):
    obj = get_object_or_404(Landlord, pk=pk)
    form = AddLandlordForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Landlord Updated Successfully')
        return redirect('landlord-list')
    else:
        return render(request, 'landlord/landlord_update.html', {'form': form})


@login_required(login_url='login')
@allowed_users
def landlord_delete_view(request, pk):
    landlord = get_object_or_404(Landlord, pk=pk)
    context = {'landlord': landlord}
    if request.method == "POST":
        landlord.delete()
        messages.success(request, f'landlord Deleted Successfully')
        return redirect("landlord-list")
    return render(request, "landlord/landlord_delete.html", context)
