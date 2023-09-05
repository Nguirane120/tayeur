from django.shortcuts import render
from api_fewnu_compta.models import Commande


def commandeList(request):
    commandes = Commande.objects.all().order_by("-id")
    context = {"commandes":commandes}
    return render(request, "backoffice/commandes/commandeList.html", context)