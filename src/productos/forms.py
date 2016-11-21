from django import forms
from django.forms import modelformset_factory

from .models import Caracteristica

class CaracteristicaStockForm(forms.ModelForm):
	class Meta: 
		model = Caracteristica
		fields = [
			"titulo",
			"precio",
			"precio_rebajas",
			"stock",
			"activo",
		]

CaracteristicaStockFormSet = modelformset_factory(Caracteristica, form=CaracteristicaStockForm, extra=1)