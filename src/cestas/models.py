from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from productos.models import Caracteristica 

# Create your models here.
class CestaArticulo(models.Model):
	articulo = models.ForeignKey(Caracteristica)
	cantidad = models.PositiveIntegerField(default=1)
	# precio total de este articulo

	def __unicode__(self):
		return self.articulo.titulo 

class Cesta(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	articulos = models.ManyToManyField(CestaArticulo)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	modificado = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return str(self.id)

	# subtotal
	# tasas
	# descuentos
	# precio total