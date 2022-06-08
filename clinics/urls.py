from django.urls import path
from . import views

app_name = 'auth'


urlpatterns = [
    path('login', views.sign_in, name='login'),
    path('logout', views.logout, name='logout'),
]
