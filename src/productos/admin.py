from django.contrib import admin

from .models import Producto, Caracteristica, ProductoImg, Categoria
# Register your models here.


admin.site.register(Producto)
admin.site.register(Caracteristica)
admin.site.register(ProductoImg)
admin.site.register(Categoria)