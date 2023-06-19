from django.shortcuts import render
from django.http import HttpResponse
from api_fewnu_compta.models import *
from django.template import loader


def dashboard(request):
    template = loader.get_template("backoffice/dashboard.html")
    users = User.objects.all().count()
    clients = Customer.objects.all().count()
    commandes = Commande.objects.all().count()
    albums = Album.objects.all().count()
    transactions = Transaction.objects.all().count()
    entrees = Entree.objects.all().count()

    context = {"users":users, 
               "clients":clients, 
               "commandes":commandes, 
               "transactions":transactions, 
               "entrees":entrees, 
               "albums":albums
               }
    # return render(request, "backoffice/dashboard.html", context)
    return HttpResponse(template.render(context, request))