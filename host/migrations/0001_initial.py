# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-13 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='\u59d3\u540d')),
                ('age', models.IntegerField(verbose_name='\u59d3\u540d')),
                ('address', models.CharField(max_length=124, verbose_name='\u4f4f\u5740')),
                ('score', models.CharField(max_length=124, verbose_name='\u5206\u6570')),
            ],
        ),
    ]
