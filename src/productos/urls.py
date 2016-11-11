from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from .views import ProductoDetailView
# from boletin.views import inicio

urlpatterns = [
    #url(r'^$', views.inicio, name='inicio'),
    url(r'^(?P<pk>\d+)/$', ProductoDetailView.as_view(), name='producto_detail')
]