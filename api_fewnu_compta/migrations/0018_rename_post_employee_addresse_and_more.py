# Generated by Django 4.1 on 2022-11-11 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_fewnu_compta', '0017_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='post',
            new_name='addresse',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='numero_telephone',
            new_name='telephone',
        ),
        migrations.AddField(
            model_name='employee',
            name='poste',
            field=models.CharField(default=777777, max_length=125),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, upload_to='uploads/employee'),
        ),
    ]
