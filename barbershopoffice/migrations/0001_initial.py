# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DictClients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeClient', models.CharField(max_length=20)),
                ('nameCleint', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DictServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeService', models.CharField(max_length=20)),
                ('nameService', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOrder', models.CharField(max_length=20)),
                ('codeClient', models.CharField(max_length=255)),
                ('nameClient', models.CharField(max_length=2000)),
                ('dateOrder', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershopoffice.DictClients')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeOfService', models.CharField(max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershopoffice.Orders')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershopoffice.DictServices')),
            ],
        ),
    ]
