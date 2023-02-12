from django.urls import include, re_path
from emanga import views

urlpatterns = [
    re_path(r'^usuario$', views.usuarioApi),
    re_path(r'^usuario/([0-9]+)$', views.usuarioApi)
]