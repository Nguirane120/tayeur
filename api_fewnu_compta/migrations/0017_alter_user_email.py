# Generated by Django 4.2.1 on 2023-05-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_fewnu_compta", "0016_commande_montant_paye_commande_montant_restant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="Email"
            ),
        ),
    ]