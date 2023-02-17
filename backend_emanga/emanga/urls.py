from django.urls import re_path
from emanga import views

urlpatterns = [
  re_path(r'^manga$', views.mangaApi),
  re_path(r'^manga/([0-9]+)$', views.mangaApi)
]