from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# from ..decorators import  unauthenticated_user, allowed_user



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            user = authenticate(username=phone, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'username or passwor is incoorect')

        context = {}
        return render(request, 'backoffice/login.html', context)
    

def logOutUser(request):
    logout(request)
    return redirect('login')