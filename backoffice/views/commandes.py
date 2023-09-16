from django.shortcuts import render
from api_fewnu_compta.models import Commande
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test


def is_admin(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(is_admin)
def commandeList(request):
    commandes = Commande.objects.all().order_by("-id")
    context = {"commandes":commandes}
    return render(request, "backoffice/commandes/commandeList.html", context)