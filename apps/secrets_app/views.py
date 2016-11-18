from django.shortcuts import render, redirect
from ..login_and_registration_app.models import User
from django.contrib import messages

def index(request):
    if 'user_id' not in request.session:
        return redirect("login_reg:index")
    
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "secrets_app/index.html", context)

def logoff(request):
    request.session.clear()
    return redirect("login_reg:index")

# Create your views here.
