from django.urls import path
from apartment import views

urlpatterns = [
    path('apartment_list/', views.list_apartments, name='list-apartment'),
    path('apartment_add/', views.add_apartment, name='add-apartment'),
    path('apartment/<int:pk>', views.apartment_detail_view, name='apartment-detail'),
    path('apartment/<int:pk>/update', views.apartment_update_view, name='update-apartment'),
    path('apartment/<int:pk>/delete', views.apartment_delete_view, name='delete-apartment'),
]
