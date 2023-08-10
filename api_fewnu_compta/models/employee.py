from django.db import models
from api_fewnu_compta.models import User

class Employee(models.Model):

    nom_complet = models.CharField(max_length=125)
    telephone = models.CharField(max_length=100)
    email = models.EmailField()
    addresse = models.CharField(max_length=125)
    numero_cni = models.CharField(max_length=32)
    salaire = models.IntegerField()
    photo = models.ImageField(upload_to='uploads/employee', blank=True)
    contrat = models.CharField(max_length=125)
    poste = models.CharField(max_length=125)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # date_debut = models.DateTimeField(auto_now_add=True)
    # date_fin = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nom_complet