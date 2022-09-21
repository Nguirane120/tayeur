from django.db import models
from django.utils import timezone
from .user import User

class Company(models.Model):
    date = models.DateTimeField(default=timezone.now)
    raisonSocial = models.CharField(max_length=250,blank=True, null=True)
    logo = models.ImageField(upload_to='images/',null=True, blank=True)
    formJuridiqu = models.CharField(max_length=250,blank=True, null=True)
    pays = models.CharField(max_length=30,blank=True, null=True)
    adresse = models.CharField(max_length=250,blank=True, null=True)
    pays = models.CharField(max_length=250,blank=True, null=True)
    region = models.CharField(max_length=250,blank=True, null=True)
    ville = models.CharField(max_length=250,blank=True, null=True)
    numeroSiret = models.CharField(max_length=250,blank=True, null=True)
    codePostal = models.IntegerField(blank=True, null=True)
    email = models.EmailField(("Email"), max_length=254)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company')
    archived = models.BooleanField(default=False)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_fewnu_compta_company"
        app_label = "api_fewnu_compta"

    def __str__(self):
        return self.raisonSocial