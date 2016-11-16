from django.contrib import admin

from .models import Producto, Caracteristica
# Register your models here.


admin.site.register(Producto)
admin.site.register(Caracteristica)