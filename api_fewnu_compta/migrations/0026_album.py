# Generated by Django 4.1 on 2022-11-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_fewnu_compta', '0025_alter_paiement_id_employe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1255)),
                ('images', models.FileField(upload_to='uploads/albums')),
            ],
        ),
    ]