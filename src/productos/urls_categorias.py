from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from .views import CategoriaListView, CategoriaDetailView
# from boletin.views import inicio

urlpatterns = [
    #url(r'^$', views.inicio, name='inicio'),
    url(r'^(?P<slug>[\w-]+)/$', CategoriaDetailView.as_view(), name='categoria_detail'),
    url(r'^$', CategoriaListView.as_view(), name='categoria_list'),
]

