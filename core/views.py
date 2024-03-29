from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as app_login
from django.contrib import messages

def login(request):
    return render(request, "login.html")


def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            app_login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuário ou senha invalida. Tente novamente")
    return redirect("login")
