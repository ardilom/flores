# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-15 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidanueva', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='documento',
            field=models.IntegerField(blank=True, null=True, verbose_name='Documento'),
        ),
    ]