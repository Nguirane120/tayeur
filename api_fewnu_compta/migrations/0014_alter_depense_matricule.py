# Generated by Django 4.1 on 2022-10-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_fewnu_compta', '0013_depense_matricule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depense',
            name='matricule',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
