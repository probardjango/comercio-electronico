from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.
class ProductoQuerySet(models.query.QuerySet):
	def activo(self):
		return self.filter(activo=True)

class ProductoManager(models.Manager):
	def get_queryset(self):
		return ProductoQuerySet(self.model, using=self._db) 

	def all(self, *args, **kwargs):
		return self.get_queryset().activo()


class Producto(models.Model):
	titulo = models.CharField(max_length=120)
	descripcion = models.TextField(blank=True, null=True)
	precio = models.DecimalField(decimal_places=2, max_digits=10)
	activo = models.BooleanField(default=True)
	#slug
	#stock

	objects = ProductoManager()

	def __unicode__(self): #2
		return self.titulo 

	def __str__(self): #3
		return self.titulo

	def get_absolute_url(self):
		return reverse("producto_detail", kwargs={"pk": self.pk})

class Caracteristica(models.Model):
	producto = models.ForeignKey(Producto)
	titulo = models.CharField(max_length=120)
	precio = models.DecimalField(decimal_places=2, max_digits=10)
	precio_rebajas = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
	activo = models.BooleanField(default=True)
	stock = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.titulo

	def get_precio(self):
		if self.precio_rebajas is not None: 
			return self.precio_rebajas
		else:
			return self.precio

	def get_absolute_url(self):
		return self.producto.get_absolute_url()
		

# imagen Producto

# categoria producto 