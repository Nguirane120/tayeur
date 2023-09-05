from django.db import models
from django.utils import timezone
from .employee import Employee


class Paiement(models.Model):
    PAYE = 'PAYE'
    AVANCE = 'AVANCE'
    CHOICE_STATUS = (
            (PAYE, 'PAYE'),
            (AVANCE, 'AVANCE'),
)
    id_employe = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employe')
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,choices=CHOICE_STATUS,default=AVANCE,)
    montant = models.IntegerField(null=True, blank=True)
    archived = models.BooleanField(default=False)
