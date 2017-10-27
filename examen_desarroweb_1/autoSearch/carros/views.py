# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.shortcuts import render
from .models import Car


# Create your views here.
def home(request):
    prueba = "Esta es una prueba" 

    return render(request, "home.html", context={"prueba": prueba})


class car_list(ListView):

    template_name = "car_list.html"
    queryset = Car.objects.all()

class car_detail(DetailView):
    template_name = "car_detail.html"
    queryset = Car.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return Car.objects.get(id=id)
