from django.test import TestCase, Client
from datetime import datetime, date, timedelta
from rest_framework import status
from rest_framework.test import APITestCase
from emanga.models import Pedido, Cobranca, ItemPedido, Pagamento, Usuario, Endereco, Manga, FormaPagamento
import json

class PedidoTestCase(TestCase):
    def test_criar_pedido(self):

        self.usuario_teste = Usuario.objects.create(nome='Teste', email='teste@teste.com', senha='123456')
        endereco = Endereco.objects.create(user=self.usuario_teste, cep='12345-678', logradouro='Rua Teste', num='123', cidade='Cidade Teste', uf='TS')
        manga = Manga.objects.create(
            ds_titulo='Título do Manga',
            ds_sinopse='Sinopse do Manga',
            cidade='São Paulo',
            estado='SP',
            valor=29.99,
            quantidade=10,
            fotoCaminho='/caminho/para/foto.jpg',
            disponivel=True
        )

        forma_pagamento = FormaPagamento.objects.create(
            id=1,
            descricao='Cartão de Crédito'
        )
        # Dados do pedido
        pedido = {
            "pagamento":
                {
                    "forma_pagamento_id": forma_pagamento.id,
                    "nr_parcelas":1,
                    "valor_parcela":manga.valor,
                    "vl_pago":manga.valor,
                    "dh_pagamento":"2023-04-04",
                    "dh_vencimento":"2023-04-04"
                },
            "pedido":
            {
                "user_id":1,
                "endereco_entrega_id":endereco.id,
                "vl_total": manga.valor,
                "item_pedido":
                    [
                        {
                        "manga_id":manga.id,
                        "qt_pedido":1,
                        "vl_unitario":manga.valor,
                        "vl_total":manga.valor
                        }
                    ]
            }
        }

        # Envia a requisição POST para a API
        response = self.client.post('/pedido', json.dumps(pedido), content_type="application/json")

        # Verifica se a resposta da API é 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se o pedido foi salvo no banco de dados
        self.assertEqual(Pedido.objects.count(), 1)
        self.assertEqual(ItemPedido.objects.count(), 1)
        self.assertEqual(Cobranca.objects.count(), 1)
        self.assertEqual(Pagamento.objects.count(), 1)

        # Verifica se os dados do pedido foram salvos corretamente
        pedido_salvo = Pedido.objects.first()
        self.assertEqual(pedido_salvo.user_id, 1)
        self.assertEqual(pedido_salvo.endereco_entrega_id, 1)
        # self.assertEqual(pedido_salvo.vl_total, manga.valor)

        # Verifica se os dados do item do pedido foram salvos corretamente
        item_pedido_salvo = ItemPedido.objects.first()
        self.assertEqual(item_pedido_salvo.manga_id, 1)
        self.assertEqual(item_pedido_salvo.qt_pedido, '1')
        #self.assertEqual(item_pedido_salvo.vl_unitario, manga.valor)
        #self.assertEqual(item_pedido_salvo.vl_total, manga.valor)

        # Verifica se os dados da cobrança foram salvos corretamente
        cobranca_salva = Cobranca.objects.first()
        self.assertEqual(cobranca_salva.forma_pagamento_id, 1)
        self.assertEqual(cobranca_salva.pedido, pedido_salvo)
        self.assertEqual(cobranca_salva.dh_vencimento, datetime.strptime('2023-04-04', '%Y-%m-%d').date())
        #self.assertEqual(cobranca_salva.vl_total, manga.valor)
        self.assertEqual(cobranca_salva.nr_parcelas, '1')

        # Verifica se os dados dos pagamentos foram salvos corretamente
        pagamento_1 = Pagamento.objects.first()
        self.assertEqual(pagamento_1.cobranca, cobranca_salva)
        #self.assertEqual(pagamento_1.vl_fatura, manga.valor)
        self