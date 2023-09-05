from django.db import models
from api_fewnu_compta.models import Album
from .user import User

class Photo(models.Model):
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    images = models.FileField(upload_to='uploads/albums', null=True, blank=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    archived = models.BooleanField(default=False)