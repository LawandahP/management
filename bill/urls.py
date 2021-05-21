from django.urls import path
from django.views.i18n import JavaScriptCatalog

from bill import views


urlpatterns = [
    path('jsi18n1', JavaScriptCatalog.as_view(), name='js-catlog1'),
    path('deposits/', views.deposit_report_list, name='paid-deposits'),
    path('user_bills/list', views.userBillsList, name='list-bills'),
    path('pay_due_bills/', views.pay_due_bills, name='pay-bills'),

    path('add_bill/', views.addUserBills, name='add-bills'),
    path('bill/<int:pk>/update_bill', views.updateBill, name='update-bills'),
    path('bill/<int:pk>/delete_bill', views.bill_delete_view, name='delete-bills'),

]