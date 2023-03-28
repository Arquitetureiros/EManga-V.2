from django.test import TestCase
from emanga.models import manga
from rest_framework import status
import json

class MangaTestCase(TestCase):
    def test_manga_created(self):
        manga_data = {
            "ds_titulo": "Titulo do Manga",
            "ds_sinopse": "Sinopse do Manga",
            "cidade": "São Paulo",
            "estado": "SP",
            "valor": 10,
            "fotoCaminho": "chain.jpg",
            "quantidade": 5
        }
        manga_data = json.dumps(manga_data)
        response = self.client.post('/manga', data=manga_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(manga.objects.count(), 1)
        mangas = manga.objects.get(ds_titulo="Titulo do Manga")
        self.assertEqual(mangas.ds_sinopse, 'Sinopse do Manga')
        self.assertEqual(mangas.cidade, 'São Paulo')
        self.assertEqual(mangas.estado, 'SP')
        self.assertEqual(mangas.valor, 10)
        self.assertEqual(mangas.fotoCaminho, 'chain.jpg')
        self.assertEqual(mangas.quantidade, 5)