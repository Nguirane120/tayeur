from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=1255)
    archived = models.BooleanField(default=False)