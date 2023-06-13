from django.db import models

class Transaction(models.Model):
    commande = models.ForeignKey('api_fewnu_compta.Commande', on_delete=models.CASCADE, related_name='transactions')
    montant_paye = models.FloatField(blank=True, null=True, default=0)
    date_transaction = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.commande.update_montant_restant()
