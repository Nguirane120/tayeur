# Generated by Django 4.2.1 on 2023-08-12 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_fewnu_compta', '0019_alter_image_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ParametreImage',
        ),
    ]
