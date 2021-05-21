from django.urls import path
from landlord import views
from landlord.api import views as api_views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('landlord_add/', views.add_landlord, name='add-landlord'),

    path('landlord_list/', views.list_landlords, name='landlord-list'),
    path('landlord/<int:pk>', views.landlord_detail_view, name='landlord-detail'),
    path('landlord/<int:pk>/update', views.landlord_update_view, name='update-landlord'),
    path('landlord/<int:pk>/delete', views.landlord_delete_view, name='delete-landlord'),
]
