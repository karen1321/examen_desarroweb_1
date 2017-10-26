# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.shortcuts import render



# Create your views here.
def home(request):
    prueba = "Esta es una prueba" 

    return render(request, "home.html", context={"prueba": prueba})



