from django.views.generic import View, ListView
from django.shortcuts import render
from .models import Item


class HomeView(ListView):
    template_name = 'index.html'
    model = Item
