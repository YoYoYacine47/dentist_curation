from django.urls import path
from .views import index, test

app_name = 'patients'

urlpatterns = [
    path('', index, name='index'),
    path('test/', test, name='test')
]
