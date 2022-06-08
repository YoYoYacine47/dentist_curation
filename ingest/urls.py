from django.urls import path
from .views import fileUpload, index

app_name = 'ingest'

urlpatterns = [
    path('', index, name='index'),
    path('file_upload/', fileUpload, name='file_upload')
]
