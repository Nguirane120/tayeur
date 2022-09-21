from django.db import models
from django.utils import timezone
from .product import Product
from .vente import Vente

class Article(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE , related_name="articles")
    prod_qte = models.IntegerField(default=1)
    total = models.IntegerField(default=0)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_fewnu_compta_article"
        app_label = "api_fewnu_compta"
        unique_together = [['products','vente']]

