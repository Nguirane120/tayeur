from django.db import models
from django.utils import timezone
from .user import User
from .client import Customer





LIVREE = 'livree' 
ENCOURS = 'encours'
NOUVELLE = 'nouvelle'
STATUS_TYPES = (
    (NOUVELLE,NOUVELLE),
    (LIVREE,LIVREE),
    (ENCOURS,ENCOURS)
)

class Commande(models.Model):
    nom_tissu = models.CharField(max_length=255,null=True, blank=True)
    metre_tissu = models.IntegerField(null=True, blank=True)
    modele = models.FileField(upload_to='images/', blank=True, null=True)
    date_livraison = models.DateTimeField(default=timezone.now, blank=True, null = True)
    montant = models.FloatField()
    montant_paye = models.FloatField(blank=True, null=True, default=0)
    montant_restant = models.FloatField(blank=True, null=True, default=0)
    statut = models.CharField(max_length=300,choices=STATUS_TYPES,  null=True, blank=True , default=NOUVELLE)
    clientId = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    archived = models.BooleanField(default=False)
    date_commande = models.DateTimeField(default=timezone.now)

    # reduction = models.DecimalField(decimal_places=2, max_digits=20)


    def __str__(self):
        return self.nom_tissu
