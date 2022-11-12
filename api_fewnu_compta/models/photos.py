from django.db import models
from api_fewnu_compta.models import Album

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    images = models.FileField(upload_to='uploads/albums')
    archived = models.BooleanField(default=False)