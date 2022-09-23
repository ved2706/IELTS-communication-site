from django.shortcuts import render,redirect
from http.client import HTTPResponse
from django.contrib.auth.models import User,auth
from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(requests):
    return render(requests,'index.html')
def payment(requests):
    return render(requests,'payment.html')
def nick(requests):
    return render(requests,'nick.html')
def refrence(requests):
    return render(requests,'refrence.html')
def uk(requests):
    return render(requests,'uk.html')
def usa(requests):
    return render(requests,'usa.html')
def australia(requests):
    return render(requests,'australia.html')
def login(requests):
    if requests.method == 'POST':
        username=requests.POST['username']
        password=requests.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(requests,user)
            print("login sucessfullu")
            return redirect('/back')
    else:
        return render(requests,'login.html')        
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
        return redirect('/welcome')
    else:
        return render(requests,'signup.html')
def welcome(requests):
    return render(requests,'welcome.html')
def back(requests):
    return render(requests,'back.html')
        