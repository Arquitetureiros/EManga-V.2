from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from emanga.serializers import UsuarioSerializer


#class UsuarioTestCase(APITestCase):
#    def test_listar(self):
#        response = self.client.get(reverse('usuario_listar'))
#
#        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ValidateTestCase(TestCase):
    def test_usuario_invalido(self):
        serializer = UsuarioSerializer({"email": "aaaa@bbb", "senha": "test"})
        response = serializer.validate({"email": "aaaa@bbb", "senha": "test"})
        self.assertEqual(response, {"email": "aaaa@bbb", "senha": "test"})

    def test_credencial_errada(self):
        serializer = UsuarioSerializer({"email": "giovanni@test", "senha": "test"})
        response = serializer.validate({"email": "giovanni@test"})
        self.assertEqual(response, 'Email e senha são obrigatórios.')

    