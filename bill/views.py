from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

import bill
from unit.models import Unit
from .forms import UserBillsForm, UserBillsSearchForm
from .models import Bill
from users.decorators import allowed_users
from users.models import CustomUser


def deposit_report_list(request):
    deposits = Unit.objects.all()
    context = {
        'deposits': deposits
    }
    return render(request, 'bill/deposits_list.html', context)


@login_required(login_url='login')
def addUserBills(request):
    if request.method == 'POST':
        form = UserBillsForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, f'Bills attached successfully')
            return redirect('add-bills')
    else:
        form = UserBillsForm(request.POST or None)
    return render(request, 'bill/add_user_bills.html', {'form': form})


@login_required(login_url='login')
def userBillsList(request):
    bills = Bill.objects.all()
    form = UserBillsSearchForm(request.POST or None)
    # if request.method == 'POST':
    #     # tenant = form['tenant'].value()
    #     bills = Bills.objects.filter(
    #         # bill__icontains=form['bill'].value(),
    #         created_at__range=[
    #             form['start_date'].value(),
    #             form['end_date'].value(),
    #         ]
    #     )
    #     # if tenant != '':
    #     #     bills = bills.filter(tenant_id=tenant)
    # context = {
    #     'bills': bills,
    #     'form': form
    # }

    return render(request, 'bill/bills_list.html', {'bills': bills})


@login_required(login_url='login')
@allowed_users
def updateBill(request, pk):
    bill = get_object_or_404(Unit, pk=pk)
    form = UserBillsForm(request.POST or None, instance=bill)
    if form.is_valid():
        form.save()
        messages.success(request, f'Bill for {bill.tenant} is updated successfully')
        return redirect('list-bills')
    else:
        return render(request, 'bill/bills_update.html', {'form': form})


@login_required(login_url='login')
@allowed_users
def bill_delete_view(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    context = {'bill': bill}
    if request.method == "POST":
        bill.delete()
        messages.success(request, f'Bill for {bill.tenant} Deleted Successfully')
        return redirect("list-bills")
    return render(request, "bill/bills_delete.html", context)


#
# ['select_apartment', 'unit_no', 'unit_type',
#                   'rent', 'tenant', 'deposit', 'rent_paid',
#                   'placement_date', 'confirm_allocation'
#                   ]
# ['tenant', 'bill', 'amount', 'date']

@login_required(login_url='login')
@allowed_users
def pay_due_bills(request):
    units = Unit.objects.all()
    bills = Bill.objects.all()

    context = {
        'units': units,
        'bills': bills,
    }
    return render(request, "bill/pay_due_bills.html", context)
