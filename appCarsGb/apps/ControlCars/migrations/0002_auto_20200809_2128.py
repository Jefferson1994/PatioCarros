# Generated by Django 3.0.5 on 2020-08-10 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlCars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carros',
            name='EstadoAlquiler',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='carros',
            name='EstadoVenta',
            field=models.BooleanField(default=False),
        ),
    ]
