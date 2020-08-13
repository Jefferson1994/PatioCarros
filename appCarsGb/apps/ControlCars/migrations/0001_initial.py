# Generated by Django 3.0.5 on 2020-05-28 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=1000)),
                ('placa', models.CharField(max_length=20)),
                ('extra', models.CharField(max_length=20)),
                ('Codigo', models.CharField(max_length=20)),
                ('FechaCompra', models.DateField()),
                ('DuenoA', models.CharField(max_length=20)),
                ('Chasis', models.CharField(max_length=20)),
                ('Tipo', models.CharField(max_length=20)),
                ('Motor', models.CharField(max_length=20)),
                ('PrecioCompra', models.CharField(max_length=20)),
                ('Color', models.CharField(max_length=20)),
                ('Clase', models.CharField(max_length=20)),
                ('MatriculadoEn', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('NombreyApellido', models.CharField(max_length=100)),
                ('Cedula', models.CharField(max_length=20)),
                ('Celular', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VentaCars',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('MatriculadoPor', models.CharField(max_length=100)),
                ('PrecioVenta', models.CharField(max_length=20)),
                ('TipodeVenta', models.CharField(max_length=100)),
                ('Fecha_Documentacion', models.DateField()),
                ('CiudadVenta', models.CharField(max_length=100)),
                ('Fecha_Venta', models.DateField()),
                ('descripcionA', models.CharField(max_length=1000)),
                ('idcar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlCars.Carros')),
                ('idcliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlCars.Clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha_Salida', models.DateField()),
                ('F_Entrega', models.DateField()),
                ('llantas', models.CharField(max_length=20)),
                ('motor', models.CharField(max_length=20)),
                ('pintura', models.CharField(max_length=20)),
                ('luces', models.CharField(max_length=20)),
                ('kmActual', models.CharField(max_length=20)),
                ('valor', models.CharField(max_length=20)),
                ('descripcionA', models.CharField(max_length=1000)),
                ('cajas', models.CharField(max_length=20)),
                ('idcar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlCars.Carros')),
                ('idcliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlCars.Clientes')),
            ],
        ),
    ]
