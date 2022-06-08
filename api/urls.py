from django.urls import path
from .views import ClinicListAPIView, api_home
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', api_home),
    path('clinicList/', ClinicListAPIView.as_view()),
    path('auth/', obtain_auth_token),
]
