from django.db import models
from django.utils import timezone
from .user import User
from .category import Category
from .client import Customer
from .product import Product
from django.contrib.postgres.fields import ArrayField

class Vente(models.Model):
    ENCOURS = 'ENCOURS'
    ENVOYE = 'ENVOYE'
    PAYE = 'PAYE'
    ANNULE = 'ANNULE'
    VENTE_STATUS = [
        (ENCOURS, 'ENCOURS'),
        (ENVOYE, 'ENVOYE'),
        (PAYE, 'PAYE'),
        (ANNULE, 'ANNULE'),
    ]
    status = models.CharField(
        max_length=10,
        choices=VENTE_STATUS,
        default=ENCOURS,
    )
    date = models.DateTimeField(default=timezone.now)
    products = models.ManyToManyField(Product, through='Article')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.IntegerField(null=True, blank=True)
    archived = models.BooleanField(default=False)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_fewnu_compta_vente"
        app_label = "api_fewnu_compta"

