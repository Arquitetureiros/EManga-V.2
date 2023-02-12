from rest_framework import serializers
from emanga.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=('id', 'nome', 'email', 'senha')