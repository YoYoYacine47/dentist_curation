from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import pandas as pd
from .utils import conn
# Create your views here.


def index(request):
    return render(request, 'ingest/index.html')


def fileUpload(request):
    if request.method == 'POST':

        csv_file = request.FILES.get('file')
        df = pd.read_csv(csv_file)

        print(conn)
        print(df)

        # if 'Month' in df:
        #     print('there is patient')

    return HttpResponse()
