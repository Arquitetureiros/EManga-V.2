from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from emanga.serializers import UsuarioSerializer

class UsuarioTestCase(APITestCase):
    def test_listar(self):
        response = self.client.get(reverse('usuario'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_criar(self):
        data = {"nome": "teste", "email": "teste@teste", "senha": "teste"}
        response = self.client.post(reverse('usuario'), data, format='json')
        self.assertEqual(response.status_code, 200)

class EnderecoTestCase(APITestCase):
    def test_listar(self):
        response = self.client.get(reverse('endereco'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_criar(self):
        data = {"cep": "123456", "num": "123", "logradouro": "rua teste", "cidade": "teste", "uf": "te"}
        response = self.client.post(reverse('endereco'), data, format='json')
        self.assertEqual(response.status_code, 200)

class CartaoTestCase(APITestCase):
    def test_listar(self):
        response = self.client.get(reverse('cartao'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_criar(self):
        data = {"nome": "teste", "numero": "123", "validade": "23/03", "cvc": "321", "user_id": 1}
        response = self.client.post(reverse('cartao'), data, format='json')
        self.assertEqual(response.status_code, 200)

class ValidateTestCase(TestCase):
    def test_usuario_invalido(self):
        serializer = UsuarioSerializer({"email": "aaaa@bbb", "senha": "test"})
        response = serializer.validate({"email": "aaaa@bbb", "senha": "test"})
        self.assertEqual(response, {"email": "aaaa@bbb", "senha": "test"})

    def test_credencial_errada(self):
        serializer = UsuarioSerializer({"email": "giovanni@test", "senha": "test"})
        response = serializer.validate({"email": "giovanni@test"})
        self.assertEqual(response, 'Email e senha são obrigatórios.')

    