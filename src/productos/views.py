from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import CaracteristicaStockFormSet
from .models import Producto, Caracteristica
# Create your views here.
class CaracteristicaListView(ListView):
	model = Caracteristica

	def get_context_data(self, *args, **kwargs):
		context = super(CaracteristicaListView, self).get_context_data(*args, **kwargs)
		context["formset"] = CaracteristicaStockFormSet(queryset=self.get_queryset())
		return context 

	def get_queryset(self, *args, **kwargs):
		producto_pk = self.kwargs.get("pk")
		if producto_pk:
			producto = get_object_or_404(Producto, pk=producto_pk)
			queryset = Caracteristica.objects.filter(producto=producto)
		return queryset

	def post(self, request, *args, **kwargs):
		formset = CaracteristicaStockFormSet(request.POST, request.FILES)
		print request.POST
		if formset.is_valid():
			formset.save(commit=False) 
			for form in formset:
				nuevo_pro = form.save(commit=False)
				producto_pk = self.kwargs.get("pk")
				producto = get_object_or_404(Producto, pk=producto_pk)
				nuevo_pro.producto = producto
				nuevo_pro.save()
			return redirect("producto_list") 
		raise Http404


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