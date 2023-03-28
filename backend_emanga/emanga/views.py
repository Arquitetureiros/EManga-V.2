from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from emanga.models import Usuario, Endereco, Cartao, Manga, Pedido, ItemPedido
from emanga.serializers import UsuarioSerializer, EnderecoSerializer, CartaoSerializer, MangaSerializer, PedidoSerializer, ItemPedidoSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

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
    
@csrf_exempt
def cartaoApi(request, id=0):
    if request.method == 'GET' and id != 0 and 'usuario' in request.path:
        cartoes = Cartao.objects.filter(user_id = id)
        serializer = CartaoSerializer(cartoes, many= True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'GET' and id != 0:
        cartao = Cartao.objects.get(id = id)
        serializer = CartaoSerializer(cartao)
        return JsonResponse(serializer.data)
    elif request.method == 'GET':
        cartoes = Cartao.objects.all()
        cartao_serializer = CartaoSerializer(cartoes, many = True)
        return JsonResponse(cartao_serializer.data, safe=False)
    elif request.method == 'POST':
        cartao_data = JSONParser().parse(request)
        cartao_serializer = CartaoSerializer(data=cartao_data)
        if cartao_serializer.is_valid():
            cartao_serializer.save()
            return JsonResponse("Added Succesfuly", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        cartao_data=JSONParser().parse(request)
        cartao = Cartao.objects.get(id = cartao_data['id'])
        cartao_serializer = CartaoSerializer(cartao, data=cartao_data)
        if cartao_serializer.is_valid():
            cartao_serializer.save()
            return JsonResponse("Updated Sucessfuly", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        cartao = Cartao.objects.get(id = id)
        cartao.delete()
        return JsonResponse("Deleted Sucessfuly", safe=False)
    
@csrf_exempt
def mangaApi(request, id=0):
    if request.method == 'GET' and id != 0 and 'usuario' in request.path:
        mangas = Manga.objects.filter(user_id = id)
        serializer = MangaSerializer(mangas, many= True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'GET' and id != 0:
        manga = Manga.objects.get(id = id)
        serializer = MangaSerializer(manga)
        return JsonResponse(serializer.data)
    elif request.method == 'GET':
        mangas = Manga.objects.all()
        manga_serializer = MangaSerializer(mangas, many = True)
        return JsonResponse(manga_serializer.data, safe=False)
    elif request.method == 'POST':
        manga_data = JSONParser().parse(request)
        manga_serializer = MangaSerializer(data=manga_data)
        if manga_serializer.is_valid():
            manga_serializer.save()
            return JsonResponse("Added Succesfuly", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        manga_data=JSONParser().parse(request)
        manga = Cartao.objects.get(id = manga_data['id'])
        manga_serializer = CartaoSerializer(manga, data=manga_data)
        if manga_serializer.is_valid():
            manga_serializer.save()
            return JsonResponse("Updated Sucessfuly", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        manga = Manga.objects.get(id = id)
        manga.delete()
        return JsonResponse("Deleted Sucessfuly", safe=False)
    
@csrf_exempt
def pedidoApi(request, id=0):
    if request.method == 'GET' and id != 0 and 'usuario' in request.path:
        pedidos = Pedido.objects.filter(user_id = id)
        serializer = PedidoSerializer(pedidos, many= True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'GET' and id != 0:
        pedido = Pedido.objects.get(id = id)
        serializer = PedidoSerializer(pedido)
        return JsonResponse(serializer.data)
    elif request.method == 'GET':
        pedidos = Pedido.objects.all()
        pedido_serializer = PedidoSerializer(pedidos, many = True)
        return JsonResponse(pedido_serializer.data, safe=False)
    elif request.method == 'POST':
        pedido_data = JSONParser().parse(request)
        pedido_serializer = PedidoSerializer(data=pedido_data)
        if pedido_serializer.is_valid():
            pedido_serializer.save()
            return JsonResponse("Added Succesfuly", safe=False)
        return JsonResponse("Failed to Add", safe=False)
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
def itempedidoApi(request, id=0):
    if request.method == 'GET' and id != 0 and 'pedido' in request.path:
        itenspedido = ItemPedido.objects.filter(pedido = id)
        serializer = ItemPedidoSerializer(itenspedido, many= True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'GET' and id != 0:
        itempedido = ItemPedido.objects.get(id = id)
        serializer = ItemPedidoSerializer(itempedido)
        return JsonResponse(serializer.data)
    elif request.method == 'GET':
        itenspedido = ItemPedido.objects.all()
        itempedido_serializer = ItemPedidoSerializer(itenspedido, many = True)
        return JsonResponse(itempedido_serializer.data, safe=False)
    elif request.method == 'POST':
        itempedido_data = JSONParser().parse(request)
        itempedido_serializer = ItemPedidoSerializer(data=itempedido_data)
        if itempedido_serializer.is_valid():
            itempedido_serializer.save()
            return JsonResponse("Added Succesfuly", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        itempedido_data=JSONParser().parse(request)
        itempedido = ItemPedido.objects.get(id = itempedido_data['id'])
        itempedido_serializer = ItemPedidoSerializer(itempedido, data=itempedido_data)
        if itempedido_serializer.is_valid():
            itempedido_serializer.save()
            return JsonResponse("Updated Sucessfuly", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        itempedido = ItemPedido.objects.get(id = id)
        itempedido.delete()
        return JsonResponse("Deleted Sucessfuly", safe=False)
    
from rest_framework_simplejwt.views import TokenObtainPairView

class UsuarioTokenObtainPairView(TokenObtainPairView):
    serializer_class = UsuarioSerializer