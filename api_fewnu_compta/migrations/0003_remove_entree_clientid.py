# Generated by Django 4.2.1 on 2023-06-15 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api_fewnu_compta", "0002_entree"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="entree",
            name="clientId",
        ),
    ]