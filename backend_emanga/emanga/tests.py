from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
import json

class PedidoTestCase(APITestCase):

    def test_criar_pedido(self):

        c = Client()

        # Dados do pedido
        pedido = {
            "pedido": {
                "user_id": 1,
                "endereco_entrega_id": 1,
                "vl_total": 100.0,
                "item_pedido": [
                    {
                        "manga_id": 1,
                        "qt_pedido": 1,
                        "vl_unitario": 100.0,
                        "vl_total": 100.0
                    }
                ]
            },
            "pagamento": {
                "forma_pagamento_id": 1,
                "dh_vencimento": "2022-04-04",
                "valor_parcela": 100.0,
                "vl_pago": 100.0,
                "nr_parcelas": 1,
                "dh_pagamento": "2022-04-04"
            }
        }

        # Envia a requisição POST para a API
        response = c.post('/pedido/', json.dumps(pedido), content_type="application/json")

        # Verifica se a resposta da API é 201 CREATED
        self.assertEqual(response.status_code, 200)

        # Verifica se o pedido foi salvo no banco de dados
        self.assertEqual(Pedido.objects.count(), 1)
        self.assertEqual(ItemPedido.objects.count(), 1)
        self.assertEqual(Cobranca.objects.count(), 1)
        self.assertEqual(Pagamento.objects.count(), 1)

        # Verifica se os dados do pedido foram salvos corretamente
        pedido_salvo = Pedido.objects.first()
        self.assertEqual(pedido_salvo.user_id, 1)
        self.assertEqual(pedido_salvo.endereco_entrega_id, 1)
        self.assertEqual(pedido_salvo.vl_total, 100.0)

        # Verifica se os dados do item do pedido foram salvos corretamente
        item_pedido_salvo = ItemPedido.objects.first()
        self.assertEqual(item_pedido_salvo.manga_id, 1)
        self.assertEqual(item_pedido_salvo.qt_pedido, 1)
        self.assertEqual(item_pedido_salvo.vl_unitario, 100.0)
        self.assertEqual(item_pedido_salvo.vl_total, 100.0)

        # Verifica se os dados da cobrança foram salvos corretamente
        cobranca_salva = Cobranca.objects.first()
        self.assertEqual(cobranca_salva.forma_pagamento_id, 1)
        self.assertEqual(cobranca_salva.pedido, pedido_salvo)
        self.assertEqual(cobranca_salva.dh_vencimento, "2022-01-01T00:00:00Z")
        self.assertEqual(cobranca_salva.vl_total, 100.0)
        self.assertEqual(cobranca_salva.nr_parcelas, 1)

        # Verifica se os dados dos pagamentos foram salvos corretamente
        pagamento_1 = Pagamento.objects.get(nr_parcela=1)
        self.assertEqual(pagamento_1.cobranca, cobranca_salva)
        self.assertEqual(pagamento_1.vl_fatura, 100.0)
        self