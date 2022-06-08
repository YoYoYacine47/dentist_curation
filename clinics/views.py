from ast import arg
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def sign_in(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'check your username and password')
            return redirect('/clinic/login')
        auth.login(request, user)
        return redirect('/')

    return render(request, 'clinics/login.html', {})


def logout(request):
    auth.logout(request)
    return redirect('/clinic/login')
