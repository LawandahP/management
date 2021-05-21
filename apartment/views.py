from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from apartment.forms import AddApartmentForm
from apartment.models import Apartment
from users.decorators import allowed_users


@login_required(login_url='login')
@allowed_users
def list_apartments(request):
    context = {
        'apartments': Apartment.objects.all()
    }
    return render(request, 'apartment/apartment_list.html', context)


@login_required(login_url='login')
@allowed_users
def add_apartment(request):
    if request.method == 'POST':
        form = AddApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Apartment Registered Successfully')
            return redirect('add-apartment')
    else:
        form = AddApartmentForm()
    return render(request, 'apartment/apartment_add.html', {'form': form})


@login_required(login_url='login')
@allowed_users
def apartment_detail_view(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    units = apartment.in_apartment.all()
    units_count = units.count()
    context = {'apartment': apartment, 'units': units, 'units_count': units_count}
    return render(request, 'apartment/apartment_detail.html', context)


@login_required(login_url='login')
@allowed_users
def apartment_update_view(request, pk):
    obj = get_object_or_404(Apartment, pk=pk)
    form = AddApartmentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Apartment Updated Successfully')
        return redirect('list-apartment')
    else:
        return render(request, 'apartment/apartment_update.html', {'form': form})


@login_required(login_url='login')
@allowed_users
def apartment_delete_view(request, pk):
    obj = get_object_or_404(Apartment, pk=pk)
    context = {'obj': obj}
    if request.method == "POST":
        obj.delete()
        messages.success(request, f'Apartment Deleted Successfully')
        return redirect("list-apartment")
    return render(request, "apartment/apartment_delete.html", context)
