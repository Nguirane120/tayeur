from django.db import models
from .user import User
from .client import Customer

class Entree(models.Model):
    montant_entree = models.FloatField(blank=True, null=False, default=0)
    nom_entree = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.montant_entree
