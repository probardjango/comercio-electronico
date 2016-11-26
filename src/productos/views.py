from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import CaracteristicaStockFormSet
from .mixins import StaffRequiredMixin, LoginRequiredMixin
from .models import Producto, Caracteristica, Categoria
# Create your views here.
class CategoriaListView(ListView):
	model = Categoria
	queryset = Categoria.objects.all()
	template_name = "productos/producto_list.html"

class CategoriaDetailView(DetailView):
	model = Categoria

	def get_context_data(self, *args, **kwargs):
		context = super(CategoriaDetailView, self).get_context_data(*args, **kwargs)
		obj = self.get_object()
		producto_set = obj.producto_set.all()
		producto_default = obj.categoria_default.all()
		productos = ( producto_set | producto_default ).distinct()
		context["productos"] = productos
		return context


class CaracteristicaListView(StaffRequiredMixin, ListView):
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
		if formset.is_valid():
			formset.save(commit=False) 
			for form in formset:
				nuevo_pro = form.save(commit=False)
				# if nuevo_pro.titulo:
				producto_pk = self.kwargs.get("pk")
				producto = get_object_or_404(Producto, pk=producto_pk)
				nuevo_pro.producto = producto
				nuevo_pro.save()
			messages.success(request, "Tu stock ha sido modificado correctamente.")
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

	def get_context_data(self, *args, **kwargs):
		context = super(ProductoDetailView, self).get_context_data(*args, **kwargs)
		instance = self.get_object()
		context["similares"] = Producto.objects.get_similares(instance).order_by("?")[:3]
		return context
