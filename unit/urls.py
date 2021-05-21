from django.urls import path
from django.views.i18n import JavaScriptCatalog

from unit import views


urlpatterns = [
    path('jsi18n1', JavaScriptCatalog.as_view(), name='js-catlog1'),

    path('tenant_vacate/<int:pk>', views.vacate_tenant_view, name='vacate-tenant'),
    path('occupied_units/', views.list_occupied_units, name='list-occupied'),
    path('vacant_units/', views.list_vacant_units, name='list-vacant'),
    path('unit_list/', views.list_units, name='list-unit'),
    path('unit_add/', views.add_unit, name='add-unit'),
    path('unit/<int:pk>', views.unit_detail_view, name='unit-detail'),
    path('unit/<int:pk>/', views.unit_allocate_view, name='assign-unit'),
    path('unit/<int:pk>/update', views.unit_update_view, name='update-unit'),
    path('unit/<int:pk>/update_occupied', views.unit_allocate_update_view, name='update-allocate'),
    path('unit/<int:pk>/delete', views.unit_delete_view, name='delete-unit'),

]