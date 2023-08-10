from django.db import models
from .user import User


class Profile(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    numWhtsapp = models.CharField(max_length=120, null=True, blank=True)
    pays = models.CharField(max_length=120, blank=True, null=True)
    ville = models.CharField(max_length=120, blank=True, null=True)
    images = models.FileField()
