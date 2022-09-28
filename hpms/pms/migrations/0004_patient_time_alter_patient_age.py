# Generated by Django 4.1.1 on 2022-09-28 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0003_patient_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]