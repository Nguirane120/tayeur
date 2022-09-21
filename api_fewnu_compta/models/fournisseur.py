from django.db import models
from django.utils import timezone
from .user import User

class Fournisseur(models.Model):
    date = models.DateTimeField(default=timezone.now)
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    telephone = models.CharField(max_length=30)
    adresse = models.CharField(max_length=250)
    email = models.EmailField(("Email"), max_length=254)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fournisseur')
    archived = models.BooleanField(default=False)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_fewnu_compta_fournisseur"
        app_label = "api_fewnu_compta"

    def __str__(self):
        return self.email