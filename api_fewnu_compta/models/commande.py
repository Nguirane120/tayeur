from django.db import models
from django.db.models import Sum
from django.db.models import Max
from django.utils import timezone
from .user import User
from .client import Customer





NOUVELLE = 'nouvelle'
LIVREE = 'livree'
ENCOURS = 'encours'
TERMINEE = 'terminee'
STATUS_TYPES = (
    (NOUVELLE, 'Nouvelle'),
    (LIVREE, 'Livree'),
    (ENCOURS, 'Encours'),
    (TERMINEE, 'Terminee'),
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
    numero_commande = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return str(self.nom_tissu)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.numero_commande = Commande.generate_unique_numero_commande()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_numero_commande():
        last_numero = Commande.objects.all().aggregate(Max('numero_commande'))['numero_commande__max']
        if last_numero:
            new_numero = str(int(last_numero) + 1).zfill(4)
        else:
            new_numero = '0001'
        return new_numero


    @classmethod
    def total_amount(cls):
        return cls.objects.aggregate(Sum('montant'))['montant__sum']
