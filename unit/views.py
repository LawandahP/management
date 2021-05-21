from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from apartment.models import Apartment
from unit.forms import AddUnitForm, AllocateTenantUnitForm, VacateTenantForm
from unit.models import Unit, AllocateTenantUnit
from users.decorators import allowed_users
from users.models import CustomUser


@login_required(login_url='login')
@allowed_users
def list_units(request):
    units = Unit.objects.all()
    paginator = Paginator(units, 5)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''
    return render(request, 'unit/unit_list.html',
                  context={'page': page, 'next_page_url': next_url,
                           'prev_page_url': prev_url})


@login_required(login_url='login')
@allowed_users
def add_unit(request):
    if request.method == 'POST':
        form = AddUnitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'A New Unit has been added to the System')
            return redirect('add-unit')
    else:
        form = AddUnitForm()
    return render(request, 'unit/unit_add.html', {'form': form})


@login_required(login_url='login')
@allowed_users
def unit_detail_view(request, pk):
    object = get_object_or_404(Unit, pk=pk)
    context = {'object': object}
    return render(request, 'unit/unit_detail.html', context)


@login_required(login_url='login')
@allowed_users
def unit_update_view(request, pk):
    object = get_object_or_404(Unit, pk=pk)
    form = AddUnitForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        messages.success(request, f'Unit No.{object.unit_no} Updated Successfully')
        return redirect('list-bill')
    else:
        context = {'form': form, 'object': object}
        return render(request, 'unit/unit_update.html', context)


@login_required(login_url='login')
@allowed_users
def unit_allocate_update_view(request, pk):
    object = get_object_or_404(Unit, pk=pk)
    form = AllocateTenantUnitForm(request.POST or None, instance=object)
    if form.is_valid():
        if not object.confirm_allocation:
            messages.info(request, f'The Checkbox cannot be unchecked')
            return redirect('update-allocate', pk=pk)
        form.save()
        messages.success(request, f'Unit No.{object.unit_no} Updated Successfully')
        return redirect('list-unit')
    else:
        context = {'form': form, 'object': object}
        return render(request, 'unit/occupied_update.html', context)


@login_required(login_url='login')
@allowed_users
def unit_delete_view(request, pk):
    obj = get_object_or_404(Unit, pk=pk)
    context = {'obj': obj}
    if request.method == "POST":
        obj.delete()
        messages.success(request, f'Unit Deleted Successfully')
        return redirect('list-unit')
    return render(request, "unit/unit_delete.html", context)


@login_required(login_url='login')
@allowed_users
def unit_allocate_view(request, pk):
    object = get_object_or_404(Unit, pk=pk)
    if request.method == 'POST':
        form = AllocateTenantUnitForm(request.POST or None, instance=object)
        if form.is_valid():
            if not object.confirm_allocation:
                messages.info(request, f'Confirm placement first for successful allocation')
                return redirect('assign-unit', pk=pk)
            form.save()
            messages.success(request, f'Unit no {object.unit_no} allocated Successfully to {object.tenant}')
            return redirect('list-occupied')
    else:
        form = AllocateTenantUnitForm(request.POST or None, instance=object)
    return render(request, 'unit/allocate_unit.html', {'form': form})


@login_required(login_url='login')
@allowed_users
def list_occupied_units(request):
    units = Unit.objects.all()
    paginator = Paginator(units, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return render(request, 'unit/occupied_units.html',
                  context={'units': page.object_list})


@login_required(login_url='login')
@allowed_users
def list_vacant_units(request):
    units = Unit.objects.all()
    paginator = Paginator(units, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context = {'units': page.object_list}
    return render(request, 'unit/vacant_units.html', context)


@login_required(login_url='login')
@allowed_users
def vacate_tenant_view(request, pk):
    obj = get_object_or_404(Unit, pk=pk)
    tenant = obj.tenant
    if request.method == 'POST':
        form = VacateTenantForm(request.POST or None, instance=obj)
        if form.is_valid():
            if obj.confirm_allocation:
                messages.info(request, f'Uncheck checkbox to vacate tenant {tenant}')
                return redirect('vacate-tenant', pk=pk)
            elif obj.confirm_allocation is False:
                form.save()
                tenant.delete()
                messages.success(request, f'Tenant {tenant} has been Vacated Successfully, Unit no. {obj.unit_no} is '
                                          f'now vacant')
                return redirect('list-occupied')
    else:
        form = VacateTenantForm(request.POST or None, instance=obj)
    return render(request, 'unit/vacate_tenant.html', {'form': form})

