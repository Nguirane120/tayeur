from django.db import models
from api_fewnu_compta.models import Employee,User



class Horaire(models.Model):
    employe = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    jour = models.CharField(
        max_length=10,
        choices=[
            ('lundi', 'Lundi'),
            ('mardi', 'Mardi'),
            ('mercredi', 'Mercredi'),
            ('jeudi', 'Jeudi'),
            ('vendredi', 'Vendredi'),
            ('samedi', 'Samedi'),
            ('dimanche', 'Dimanche'),
        ]
    )
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # Ajoutez d'autres champs pertinents pour l'horaire
