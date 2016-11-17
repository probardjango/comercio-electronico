from django.contrib import admin

from .models import Producto, Caracteristica, ProductoImg
# Register your models here.


admin.site.register(Producto)
admin.site.register(Caracteristica)
admin.site.register(ProductoImg)