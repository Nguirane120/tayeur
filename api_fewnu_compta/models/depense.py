from django.db import models
from django.utils import timezone
from .user import User
from .category import Category
from .fournisseur import Fournisseur
from .product import Product


class Depense(models.Model):
    date = models.DateTimeField(default=timezone.now)
    products = models.ManyToManyField(Product, through='DepenseArticle')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    total = models.IntegerField(null=True, blank=True)
    archived = models.BooleanField(default=False)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_fewnu_compta_depense"
        app_label = "api_fewnu_compta"