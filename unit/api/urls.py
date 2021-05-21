from django.urls import path, include
from .views import UnitViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', UnitViewSet)

app_name = 'bill'
urlpatterns = [
    path('', include(router.urls)),

]
