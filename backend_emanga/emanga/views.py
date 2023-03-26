from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from emanga.models import Usuario, Endereco, Cartao
from emanga.serializers import UsuarioSerializer, EnderecoSerializer, CartaoSerializer

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
    
from rest_framework_simplejwt.views import TokenObtainPairView

class UsuarioTokenObtainPairView(TokenObtainPairView):
    serializer_class = UsuarioSerializer