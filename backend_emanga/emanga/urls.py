from django.urls import include, re_path
from emanga import views

urlpatterns = [
    re_path(r'^cliente$', views.clienteApi),
    re_path(r'^cliente/([0-9]+)$', views.clienteApi)
]