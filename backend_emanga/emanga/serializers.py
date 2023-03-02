from rest_framework import serializers
from emanga.models import Usuario

from rest_framework_simplejwt.tokens import RefreshToken

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=('id', 'nome', 'email', 'senha')
        extra_kwargs = {
            'nome': {'required': False}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'] = serializers.CharField()
        self.fields['senha'] = serializers.CharField()

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
                raise serializers.ValidationError('Usuário não encontrado ou senha inválida.')
        else:
            raise serializers.ValidationError('Email e senha são obrigatórios.')
    
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