from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=1255)
    file = models.FileField(upload_to='file/')