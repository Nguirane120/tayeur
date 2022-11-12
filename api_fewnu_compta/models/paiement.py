from django.db import models
from django.utils import timezone
from .user import employe


class Paiement(models.Model):
    PAYE = 'PAYE'
    AVANCE = 'AVANCE'
    CHOICE_STATUS = (
            (PAYE, 'PAYE'),
            (AVANCE, 'AVANCE'),
)
    id_employe = models.ForeignKey(
        Employe, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,choices=CHOICE_STATUS,default=AVANCE,)
    montant = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "api_fewnu_compta_paiement"
        app_label = "api_fewnu_compta"
