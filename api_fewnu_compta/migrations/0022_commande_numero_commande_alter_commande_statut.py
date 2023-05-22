# Generated by Django 4.2.1 on 2023-05-17 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_fewnu_compta", "0021_alter_commande_statut"),
    ]

    operations = [
        migrations.AddField(
            model_name="commande",
            name="numero_commande",
            field=models.CharField(default=0, max_length=4, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="commande",
            name="statut",
            field=models.CharField(
                blank=True,
                choices=[
                    ("nouvelle", "Nouvelle"),
                    ("livree", "Livree"),
                    ("encours", "Encours"),
                    ("terminee", "Terminee"),
                ],
                default="nouvelle",
                max_length=300,
                null=True,
            ),
        ),
    ]
