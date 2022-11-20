from django.db import models
from django.utils import timezone
from .user import User


#Mesure
class Mesure(models.Model):

    COU = models.IntegerField(null=True, blank=True)
    EPAULE = models.IntegerField(null=True, blank=True)
    MANCHES = models.IntegerField(null=True, blank=True)
    CEINTURE = models.IntegerField(null=True, blank=True)
    TOURS_DE_BRAS = models.IntegerField(null=True, blank=True)
    TOURS_DE_HANCHES = models.IntegerField(null=True, blank=True)
    TOURS_DE_CUISSE = models.IntegerField(null=True, blank=True)
    LONGUEUR_HAUT = models.IntegerField(null=True, blank=True)
    LONGUEUR_BAS = models.IntegerField(null=True, blank=True)
    LONGUEUR_BOUBOU = models.IntegerField(null=True, blank=True)
    LONGUEUR_JUPE = models.IntegerField(null=True, blank=True)
    POITRINE = models.IntegerField(null=True, blank=True)
    TOURS_DE_TAILLE = models.IntegerField(null=True, blank=True)
    LONGUEUR_BRAS = models.IntegerField(null=True, blank=True)
    LONGUEUR_ROBE = models.IntegerField(null=True, blank=True)



class Customer(models.Model):
    FEMME = "femme"
    HOMME = "homme"
    SEXE = (
        (FEMME, 'femme'),
        (HOMME, 'homme')
    )
    date = models.DateTimeField(default=timezone.now)
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    telephone = models.CharField(max_length=30)
    adresse = models.CharField(max_length=250)
    email = models.EmailField(("Email"), max_length=254)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    # shop = models.ForeignKey('Shop',on_delete = models.CASCADE, related_name='customer',null=True)
    archived = models.BooleanField(default=False)

    sexe = models.CharField(max_length=10,choices=SEXE,default=FEMME,)
    mesure = models.ForeignKey(
        Mesure , on_delete=models.CASCADE, blank=False, null=True)


    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_fewnu_compta_client"
        app_label = "api_fewnu_compta"

    def __str__(self):
        return self.email