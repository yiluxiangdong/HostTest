# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#python  manage.py makemigrations --empty 你的应用名;
#python  manage.py makemigrations;
#python  manage.py migrate;
#python manage.py  createsuperuser
# Create your models here.
class  user(models.Model):
    name = models.CharField(max_length=128,verbose_name='姓名')
    age = models.IntegerField(verbose_name='姓名')
    address = models.CharField(max_length=124,verbose_name='住址')
    score = models.CharField(max_length=124, verbose_name='分数')
    def __str__(self):
        return  self.no