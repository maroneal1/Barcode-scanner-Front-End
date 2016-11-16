# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_barcode_num',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc_barcode_num',
            field=models.CharField(default=' ', max_length=200, unique=True),
        ),
    ]
