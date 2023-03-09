from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from emanga.models import Usuario
from emanga.serializers import UsuarioSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

@csrf_exempt
def usuarioApi(request, id=0):
    if request.method == 'GET' and id != 0:
        usuario = Usuario.objects.get(id = id)
        serializer = UsuarioSerializer(usuario)
        return JsonResponse(serializer.data)
    elif request.method == 'GET':
        print('entrou aqui 2')
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
    
from rest_framework_simplejwt.views import TokenObtainPairView

class UsuarioTokenObtainPairView(TokenObtainPairView):
    serializer_class = UsuarioSerializer