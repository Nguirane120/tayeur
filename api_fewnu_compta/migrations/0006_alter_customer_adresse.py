# Generated by Django 4.2.1 on 2023-08-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_fewnu_compta', '0005_alter_entree_nom_entree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='adresse',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
