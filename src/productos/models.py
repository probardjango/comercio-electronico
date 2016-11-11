from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
	titulo = models.CharField(max_length=120)
	descripcion = models.TextField(blank=True, null=True)
	precio = models.DecimalField(decimal_places=2, max_digits=10)
	activo = models.BooleanField(default=True)
	#slug
	#stock 

	def __unicode__(self): #2
		return self.titulo 

	def __str__(self): #3
		return self.titulo

		

# imagen Producto

# categoria producto 