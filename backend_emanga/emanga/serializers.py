from rest_framework import serializers
from emanga.models import manga


class MangaSerializer(serializers.ModelSerializer):
  class Meta:
    model=manga
    fields=('id', 'ds_titulo', 'ds_sinopse', 'cidade', 'estado', 'valor', 'fotoCaminho', 'quantidade')


