from django.db import models
from django.utils import timezone
from .vente import Vente
from .depense import Depense

class Statistic(models.Model):
    ventes = models.ForeignKey(Vente, on_delete=models.CASCADE)
    depenses = models.ForeignKey(Depense, on_delete=models.CASCADE)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_fewnu_compta_statistic"
        app_label = "api_fewnu_compta"

