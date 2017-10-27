# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Car(models.Model):
  make = models.CharField(max_length=20)
  Type = models.CharField(max_length=20)
  year = models.CharField(max_length=10)
  colour = models.CharField(max_length=20)
  price = models.DecimalField(max_digits=10 , decimal_places= 10)
  created = models.DateTimeField(auto_now=True)
  
