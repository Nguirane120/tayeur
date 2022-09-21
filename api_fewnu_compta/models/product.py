from django.db import models
from django.utils import timezone
from .user import User
from .category import Category

class Product(models.Model):
    date = models.DateTimeField(default=timezone.now)
    libelle = models.CharField(max_length=250)
    description = models.CharField(max_length=512)
    qte = models.IntegerField()
    min_stock= models.IntegerField()
    prix_achat = models.IntegerField()
    prix_vente = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Product')
    archived = models.BooleanField(default=False)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_fewnu_compta_produit"
        app_label = "api_fewnu_compta"

    def __str__(self):
        return self.libelle