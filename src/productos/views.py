from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Producto
# Create your views here.

class ProductoListView(ListView):
	model = Producto

	def get_context_data(self, *args, **kwargs):
		context = super(ProductoListView, self).get_context_data(*args, **kwargs)
		context["ahora"] = timezone.now()
<<<<<<< HEAD
		return context 
=======
		return context
>>>>>>> tmp

class ProductoDetailView(DetailView):
	model = Producto