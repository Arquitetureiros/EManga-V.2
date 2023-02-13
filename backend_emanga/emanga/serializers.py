from rest_framework import serializers
from emanga.models import manga, produto


class MangaSerializer(serializers.ModelSerializer):
  class Meta:
    model=manga
    fields=('id', 'ds_sinopse', 'ds_titulo', 'valor', 'fotoCaminho', 'quantidade')

class ProdutoSerializer(serializers.ModelSerializer):
  class Meta:
    model=produto
    fields=('id', 'nm_produto', 'cd_produto', 'qt_produto', 'bo_ativo')