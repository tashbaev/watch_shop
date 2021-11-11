from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.list import BaseListView

from .models import Product


class HomeView(TemplateView):
    # model = Product
    template_name = 'base.html'
    # context_object_name = 'categories'