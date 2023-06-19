from django.shortcuts import render
from api_fewnu_compta.models import Customer


def clientsList(request):
    clients = Customer.objects.all().order_by("-id")
    context = {"clients":clients}
    return render(request, "backoffice/clients/clientsList.html", context)