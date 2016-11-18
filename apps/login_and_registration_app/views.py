from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'login_and_registration_app/index.html')
# Create your views here.

def register(request):
    res = User.objects.register(request.POST)

    if res["added"]:
        request.session['user_id'] = res['new_user'].id
    else:
        for error in res["errors"]:
            messages.error(request, error)

    return redirect("login_reg:index")

def login(request):
    user = User.objects.login(request.POST)

    if user:
        request.session['user_id'] = user.id
    else:
        messages.error(request, "E-mail address or password incorrect")

    return redirect("secrets:index")
