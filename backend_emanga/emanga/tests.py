from django.test import TestCase
from emanga.models import manga
from rest_framework import status
import json

class MangaTestCase(TestCase):
    def test_get_manga_by_ds_titulo(self):
        manga_data = {
            "ds_titulo": "berserk vol.1",
            "ds_sinopse": "primeiro volume do manga de berserk",
            "cidade": "cianorte",
            "estado": "pr",
            "valor": 5,
            "fotoCaminho": "berserk.jpg",
            "quantidade": 4
        }
        manga_data = json.dumps(manga_data)
        self.client.post('/manga', data=manga_data, content_type='application/json')

        response = self.client.get(f'/manga?ds_titulo={json.loads(manga_data)["ds_titulo"]}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        mangas = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(mangas), 1)
        self.assertEqual(mangas[0]['ds_sinopse'], 'primeiro volume do manga de berserk')
        self.assertEqual(mangas[0]['cidade'], 'cianorte')
        self.assertEqual(mangas[0]['estado'], 'pr')
        self.assertEqual(mangas[0]['valor'], 5)
        self.assertEqual(mangas[0]['fotoCaminho'], 'berserk.jpg')
        self.assertEqual(mangas[0]['quantidade'], 4)

