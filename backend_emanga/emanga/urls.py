from django.urls import re_path
from emanga import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  re_path(r'^manga$', views.mangaApi),
  re_path(r'^manga/([0-9]+)$', views.mangaApi)
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)