# Generated by Django 4.1.3 on 2023-08-24 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_fewnu_compta', '0027_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
