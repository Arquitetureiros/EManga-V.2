from rest_framework import serializers
from emanga.models import Usuario, Endereco, Cartao, Manga, Pedido, ItemPedido

from rest_framework_simplejwt.tokens import RefreshToken

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model= ItemPedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pedido
        fields = '__all__'

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Manga
        fields = '__all__'

class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cartao
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Endereco
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=('id', 'nome', 'email', 'senha')
        extra_kwargs = {
            'nome': {'required': False},
            'email': {'required': True},
            'senha': {'required': True}
        }

    def validate(self, attrs):
        email = attrs.get('email')
        senha = attrs.get('senha')

        if email and senha:
            usuario = self.authenticate(email=email, senha=senha)

            if usuario:
                data = { }

                refresh = self.get_token(usuario)

                data['refresh'] = str(refresh)
                data['access'] = str(refresh.access_token)

                return data

            else:
                return attrs
        else:
            return 'Email e senha são obrigatórios.'
    
    def authenticate(self, request='Post', email=None, senha=None, **kwargs):
        try:
            user = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return None

        if user.senha == senha:
            return user

        return None
    
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)