from django.db import models
from .user import User

class Category(models.Model):
    category_name = models.CharField(max_length=250)
    description = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category')
    archived = models.BooleanField(default=False)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_fewnu_compta_category"
        app_label = "api_fewnu_compta"

    def __str__(self):
        return self.category_name