from django.db import models
from .user import User


class Profile(models.Model):
    phone = models.CharField(max_length=40, unique=True, null=True,blank=True)
    firstName = models.CharField(max_length=100, blank=True, default="tayeurFirstName")
    lastName = models.CharField(max_length=100, blank=True,default="tayeurLastName")
    email = models.EmailField(("Email"), max_length=254,unique=True, blank=True, null=True)
    adresse = models.CharField(blank=True, max_length=255, null=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    numWhtsapp = models.CharField(max_length=120, null=True, blank=True)
    pays = models.CharField(max_length=120, blank=True, null=True)
    ville = models.CharField(max_length=120, blank=True, null=True)
    images = models.FileField(null=True,blank=True, upload_to='images')
    profile_image =  models.ImageField(upload_to='images/',null=True, blank=True)
    nom_attelier = models.CharField(max_length=100, blank=True)

