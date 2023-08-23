from django.shortcuts import render, redirect
from api_fewnu_compta.models import User
from ..decorators import admin_only, unauthenticated_user, allowed_user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages




@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def usersList(request):
    users = User.objects.all().order_by("-id")
    context = {"users":users}
    return render(request, "backoffice/users/userList.html", context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def userDetail(request, id):
    user = User.objects.get(id=id)
    context = {"user":user}
    return render(request, "backoffice/users/userDetail.html",  context)



@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteUser(request, id):
        user = User.objects.get(id=id)
        if request.method == "POST":
            user.delete()
            messages.success(request, "Utilisateur " + user.firstName + " supprime avec success ")
            return redirect('users')
        context = {"user":user}
        return render(request, 'backoffice/users/deleteUser.html', context)
