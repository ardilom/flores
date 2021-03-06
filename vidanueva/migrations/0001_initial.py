# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-18 21:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CantidadArreglo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300, verbose_name='Pedido por')),
                ('documento', models.IntegerField(blank=True, null=True, verbose_name='Documento')),
                ('telefono', models.IntegerField(blank=True, null=True, verbose_name='Telefono')),
            ],
        ),
        migrations.CreateModel(
            name='TipoArreglo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300, verbose_name='Tipo de arreglo')),
                ('precio', models.IntegerField(verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de venta')),
                ('nombre_fallecido', models.CharField(max_length=300, verbose_name='Fallecido')),
                ('arreglos', models.ManyToManyField(through='vidanueva.CantidadArreglo', to='vidanueva.TipoArreglo')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vidanueva.Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vidanueva.TipoCliente'),
        ),
        migrations.AddField(
            model_name='cantidadarreglo',
            name='tipo_arreglo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vidanueva.TipoArreglo'),
        ),
        migrations.AddField(
            model_name='cantidadarreglo',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vidanueva.Venta'),
        ),
    ]
