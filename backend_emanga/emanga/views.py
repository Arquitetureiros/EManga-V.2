from django.shortcuts import render
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from emanga.models import Usuario, Endereco, Pedido
from emanga.serializers import UsuarioSerializer, EnderecoSerializer, PedidoSerializer, CobrancaSerializer, PagamentoSerializer, ItemPedidoSerializer, CobrancaSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import json

# from .serializers import ModelSerializer

@csrf_exempt
def test_message(request):
    print(request)
    body_unicode = request.body.decode('utf-8')
    # Converter a string JSON em um objeto Python
    response = json.loads(body_unicode)
    # Fazer algo com o objeto Python, por exemplo:
    return JsonResponse(response, safe=False, status=200)
# Create your views here.

@csrf_exempt
def return_frete(request):
    obj = [
            {
            'id': 1,
            'nome': 'PAC', 
            'dias_uteis': 7,
            'valor': 8.00 
            },
            {
            'id': 2,
            'nome': 'SEDEX',
            'dias_uteis': 5,
            'valor': 15.00 
            }
    ]
    return JsonResponse(obj, safe=False, status=200)

@csrf_exempt
@transaction.atomic()
def pedidoApi(request, id=0):
    if request.method == 'GET' and id != 0:
        usuario = Pedido.objects.get(id = id)
        serializer = PedidoSerializer(pedido)
        return JsonResponse(serializer.data)
    elif request.method == 'GET':
        pedidos = Pedido.objects.all()
        pedido_serializer = PedidoSerializer(pedidos, many = True)
        return JsonResponse(pedido_serializer.data, safe=False)

    elif request.method == 'POST':
        request = JSONParser().parse(request)
        
        pedido = { 
            'user': request['pedido']['user_id'],
            'endereco_entrega': request['pedido']['endereco_entrega_id'],
            'vl_total': request['pedido']['vl_total']
        }

        pedido_serializer = PedidoSerializer(data=pedido)
        if pedido_serializer.is_valid():
            pedido_save = pedido_serializer.save()
            for item in request['pedido']['item_pedido']:
                item_pedido = {
                    'manga': item['manga_id'],
                    'qt_pedido': item['qt_pedido'],
                    'vl_unitario': item['vl_unitario'],
                    'vl_total': item['vl_total']
                }
                item_serializer = ItemPedidoSerializer(data=item_pedido)
                if(item_serializer.is_valid()):
                    item_serializer.save()
                else:
                    return JsonResponse({
                        'data': item_pedido,
                        'message': 'item invalido'
                        }, safe=False)
                        
            cobranca = {
                'forma_pagamento': request['pagamento']['forma_pagamento_id'],
                'pedido' : pedido_save.id,
                'dh_vencimento': request['pagamento']['dh_vencimento'],
                'vl_total':  request['pedido']['vl_total'],
                'nr_parcelas': request['pagamento']['nr_parcelas'],
            }
            cobranca_serializer = CobrancaSerializer(data=cobranca)
            
            if(cobranca_serializer.is_valid()):
                cobranca_save = cobranca_serializer.save()
                #cria n pagamentos sendo n o nr de parcelas
                for i in range(1, request['pagamento']['nr_parcelas']):
                    print('AQUI')
                    Pagamento = {
                        'cobranca' : cobranca_save.id,
                        'nr_parcela' : i,
                        'vl_fatura' : request['pagamento']['valor_parcela'],
                        'vl_pago' : request['pagamento']['vl_pago'],
                        'dh_pagamento' : request['pagamento']['dh_pagamento']
                    }
                    
                    pagamento_serializer = PagamentoSerializer(data=Pagamento);
                    if pagamento_serializer.is_valid():
                        pagamento_serializer.save()
                    else:
                        return JsonResponse({
                            'data': pagamento,
                            'message': 'pagamento invalido'
                        }, safe=False)
                    
                return JsonResponse({
                    'data': request,
                    'message': 'pedido salvo com sucesso'
                }, safe=False)
            else:
                return JsonResponse({
                    'data': cobranca,
                    'message': 'cobranca invalida'
                }, safe=False)
        else:
            return JsonResponse({
                'data': request,
                'message': 'erro ao salvar pedido'
            }, safe=False)

            
    elif request.method == 'PUT':
        pedido_data=JSONParser().parse(request)
        pedido = Pedido.objects.get(id = pedido_data['id'])
        pedido_serializer = PedidoSerializer(pedido, data=pedido_data)
        if pedido_serializer.is_valid():
            pedido_serializer.save()
            return JsonResponse("Updated Sucessfuly", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        pedido = Pedido.objects.get(id = id)
        pedido.delete()
        return JsonResponse("Deleted Sucessfuly", safe=False)

@csrf_exempt
def getPedidosByUser(request, id=0):
     if request.method == 'GET' and id != 0:
        Pedidos = Pedido.objects.get(user_id = id)
        serializer = PedidoSerializer(Pedidos)
        return JsonResponse(serializer.data)

@csrf_exempt
def usuarioApi(request, id=0):
    if request.method == 'GET' and id != 0:
        usuario = Usuario.objects.get(id = id)
        serializer = UsuarioSerializer(usuario)
        return JsonResponse(serializer.data)
    elif request.method == 'GET':
        usuarios = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuarios, many = True)
        return JsonResponse(usuario_serializer.data, safe=False)
    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Added Succesfuly", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        usuario_data=JSONParser().parse(request)
        usuario = Usuario.objects.get(id = usuario_data['id'])
        usuario_serializer = UsuarioSerializer(usuario, data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Updated Sucessfuly", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        usuario = Usuario.objects.get(id = id)
        usuario.delete()
        return JsonResponse("Deleted Sucessfuly", safe=False)

@csrf_exempt
def enderecoApi(request, id=0):
    if request.method == 'GET' and id != 0 and 'usuario' in request.path:
        enderecos = Endereco.objects.filter(user_id = id)
        serializer = EnderecoSerializer(enderecos, many= True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'GET' and id != 0:
        endereco = Endereco.objects.get(id = id)
        serializer = EnderecoSerializer(endereco)
        return JsonResponse(serializer.data)
    elif request.method == 'GET':
        enderecos = Endereco.objects.all()
        endereco_serializer = EnderecoSerializer(enderecos, many = True)
        return JsonResponse(endereco_serializer.data, safe=False)
    elif request.method == 'POST':
        endereco_data = JSONParser().parse(request)
        endereco_serializer = EnderecoSerializer(data=endereco_data)
        if endereco_serializer.is_valid():
            endereco_serializer.save()
            return JsonResponse("Added Succesfuly", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        endereco_data=JSONParser().parse(request)
        endereco = Endereco.objects.get(id = endereco_data['id'])
        endereco_serializer = EnderecoSerializer(endereco, data=endereco_data)
        if endereco_serializer.is_valid():
            endereco_serializer.save()
            return JsonResponse("Updated Sucessfuly", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        endereco = Endereco.objects.get(id = id)
        endereco.delete()
        return JsonResponse("Deleted Sucessfuly", safe=False)
    
from rest_framework_simplejwt.views import TokenObtainPairView

class UsuarioTokenObtainPairView(TokenObtainPairView):
    serializer_class = UsuarioSerializer
