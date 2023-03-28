from django.test import TestCase
from datetime import date
from myapp.models import Pedido

class PedidoModelTest(TestCase):
    def setUp(self):
        Pedido.objects.create(
            user=1,
            email="johndoe@example.com",
            dh_pedido=date.today(),
            endereco_entrega="1",
            vl_total=100.00
            )

    def test_model_creation(self):
        obj = Pedido.objects.get(id=1)
        self.assertEqual(obj.email, "johndoe@example.com")
