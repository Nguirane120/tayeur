from django.db import models
from .user import User


class Album(models.Model):
    name = models.CharField(max_length=1255)
    images = models.FileField(upload_to='uploads/albums',null=True, blank=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    archived = models.BooleanField(default=False)
