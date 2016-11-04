# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-04 01:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('time_scanned', models.CharField(default=' ', max_length=200)),
                ('person_scanned', models.CharField(default=' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('model_number', models.CharField(max_length=200)),
                ('type_equip', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_barcode_num', models.IntegerField(default=0)),
                ('item_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_barcode_num', models.IntegerField(default=0)),
                ('loc_name', models.CharField(default=' ', max_length=200)),
                ('admin', models.CharField(max_length=200)),
                ('user_assigned', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LocDev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Device')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('item_assoc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Device')),
                ('location_assoc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Location')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Location'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Question'),
        ),
    ]
