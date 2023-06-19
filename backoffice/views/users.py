from django.shortcuts import render
from api_fewnu_compta.models import User


def usersList(request):
    users = User.objects.all().order_by("-id")
    context = {"users":users}
    return render(request, "backoffice/users/userList.html", context)