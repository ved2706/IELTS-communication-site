from django.shortcuts import render, redirect
from ast import Return
from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def account(requests):
    return render(requests,'account.html')
def signup(requests):
    if requests.method == 'POST':
        firstname = requests.POST['first_name']
        lastname = requests.POST['last_name']
        email = requests.POST['email']
        username = requests.POST['username']
        password = requests.POST['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name = firstname,
            last_name= lastname
        )
        return redirect('/')
    else:
        return render(requests,'signup.html')