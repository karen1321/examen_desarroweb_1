# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from django.shortcuts import render
from .models import Car

from .forms import CarModelForm
from .mixin import FormUserNeededMixin
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    prueba = "Esta es una prueba" 

    return render(request, "home.html", context={"prueba": prueba})


class car_list(ListView):

    template_name = "car_list.html"
    queryset = Car.objects.all()

    def get_object(self):
        Type = self.kwargs.get("q")
        print Type
        return Car.objects.get(Type=Type)

class car_detail(DetailView):
    template_name = "car_detail.html"
    queryset = Car.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return Car.objects.get(id=id)

class CarCreateView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
      form_class =CarModelForm
      template_name = "create_view.html"
      success_url = "list"
      login_url = "/admin"

class CarUpdateView(UpdateView):
    queryset = Car.objects.all()
    form_class = CarModelForm
    template_name = "update_view.html"
    success_url = "/list"

class CarDeleteView(LoginRequiredMixin,DeleteView):
    model = Car
    template_name ="delete_confirm.html"
    success_url = reverse_lazy("CarList")

