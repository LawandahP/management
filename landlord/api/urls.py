from django.urls import path
from landlord.api import views as api_views

urlpatterns = [
    path('', api_views.LandlordAPIView.as_view()),
    path('<int:pk>/', api_views.LandlordDetailView.as_view())
]