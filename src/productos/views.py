from django.db.models import Q
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
		context["query"] = self.request.GET.get("q")
		return context 

	def get_queryset(self, *args, **kwargs):
		qs = super(ProductoListView, self).get_queryset(*args, **kwargs)
		query = self.request.GET.get("q")
		if query:
			qs = self.model.objects.filter(
				Q(titulo__icontains=query) |
				Q(descripcion__icontains=query)
			)
		return qs

class ProductoDetailView(DetailView):
	model = Producto