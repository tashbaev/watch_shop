from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.list import BaseListView

from .models import Category, Product


class CategoryListView(ListView):
    model = Category # Category.objects.all()
    template_name = 'home.html'
    context_object_name = 'categories'

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
