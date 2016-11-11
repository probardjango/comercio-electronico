from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Producto
# Create your views here.

class ProductoDetailView(DetailView):
	model = Producto