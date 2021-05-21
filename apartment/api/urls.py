from django.urls import path, include
from apartment.api.views import ApartmentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', ApartmentViewSet)

app_name = 'apartment'
urlpatterns = [
    path('', include(router.urls)),

]
