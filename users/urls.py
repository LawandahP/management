from django.urls import path, include
from users import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('register/', views.registerPage, name='register'),
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_Profile, name='update'),

    path('user_list/', views.list_users, name='list-user'),
    path('tenant_add/', views.addTenant, name='add-tenant'),
    path('user/<int:pk>', views.user_detail_view, name='user-detail'),
    path('user/<int:pk>/update', views.user_update_view, name='update-user'),
    path('user/<int:pk>/delete', views.user_delete_view, name='delete-user'),

    path('user/<int:pk>/lease', views.generate_lease_pdf, name='lease-agreement'),



]
