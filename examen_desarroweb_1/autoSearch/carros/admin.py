# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Registro del modelo Car 

from .models import Car

# Register your models here.

admin.site.register(Car)
