from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.
class ProductoQuerySet(models.query.QuerySet):
	def activo(self):
		return self.filter(activo=True)

class ProductoManager(models.Manager):
	def get_queryset(self):
		return ProductoQuerySet(self.model, using=self._db) 

	def all(self, *args, **kwargs):
		return self.get_queryset().activo()

	def get_similares(self, instance):
		productos_uno = self.get_queryset().filter(categorias__in=instance.categorias.all())
		productos_dos = self.get_queryset().filter(default=instance.default)
		qs = (productos_uno | productos_dos).exclude(id=instance.id).distinct()
		return qs


class Producto(models.Model):
	titulo = models.CharField(max_length=120)
	descripcion = models.TextField(blank=True, null=True)
	precio = models.DecimalField(decimal_places=2, max_digits=10)
	activo = models.BooleanField(default=True)
	#slug
	#stock
	categorias = models.ManyToManyField('Categoria', blank=True)
	default = models.ForeignKey('Categoria', related_name='categoria_default', null=True, blank=True)

	objects = ProductoManager()

	def __unicode__(self): #2
		return self.titulo 

	def __str__(self): #3
		return self.titulo

	def get_absolute_url(self):
		return reverse("producto_detail", kwargs={"pk": self.pk})

	def get_img_url(self):
		img = self.productoimg_set.first()
		if img:
			return img.imagen.url
		return img


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

def producto_post_save_receiver(sender, instance, created, *args, **kwargs):
	producto = instance
	caracteristicas = producto.caracteristica_set.all()
	if caracteristicas.count() == 0:
		nuevo_car = Caracteristica()
		nuevo_car.producto = producto
		nuevo_car.titulo = "Default"
		nuevo_car.precio = producto.precio
		nuevo_car.save()

post_save.connect(producto_post_save_receiver, sender=Producto)

def img_upload_to(instance, filename):
	titulo = instance.producto.titulo
	slug = slugify(titulo)
	return "productos/%s/%s" %(slug, filename)

# imagen Producto
class ProductoImg(models.Model):
	producto = models.ForeignKey(Producto)
	imagen = models.ImageField(upload_to=img_upload_to)

	def __unicode__(self):
		return self.producto.titulo
		

# categoria producto 
class Categoria(models.Model):
	titulo = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique=True)
	descripcion = models.TextField(null=True, blank=True)
	activo = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse("categoria_detail", kwargs={"slug": self.slug})