# Generated by Django 4.2.1 on 2023-08-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_fewnu_compta', '0014_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='adresse',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstName',
            field=models.CharField(blank=True, default='tayeurFirstName', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastName',
            field=models.CharField(blank=True, default='tayeurLastName', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='nom_attelier',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
    ]
