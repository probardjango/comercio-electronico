from django.contrib import admin


from .models import Producto, Caracteristica, ProductoImg, Categoria, ProductoDestacado
# Register your models here.

class ProductoImgInline(admin.TabularInline):
	model = ProductoImg
	extra = 0

class CaracteristicaInline(admin.TabularInline):
	model = Caracteristica
	extra = 0

class ProductoAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'precio']
	inlines = [
		CaracteristicaInline,
		ProductoImgInline,
	]
	class Meta:
		model = Producto


admin.site.register(Producto, ProductoAdmin)
# admin.site.register(Caracteristica)
# admin.site.register(ProductoImg)
admin.site.register(Categoria)
admin.site.register(ProductoDestacado)
