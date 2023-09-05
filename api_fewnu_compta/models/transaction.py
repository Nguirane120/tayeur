from django.db import models
from api_fewnu_compta.models import User




class Transaction(models.Model):
    commande = models.ForeignKey('api_fewnu_compta.Commande', on_delete=models.CASCADE, related_name='transactions')
    montant_paye = models.FloatField(blank=True, null=True, default=0)
    date_transaction = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
