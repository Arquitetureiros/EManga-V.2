from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from emanga.models import Cliente
from emanga.serializers import ClienteSerializer

# Create your views here.

@csrf_exempt
def clienteApi(request, id=0):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        cliente_serializer = ClienteSerializer(clientes, many = True)
        return JsonResponse(cliente_serializer.data, safe=False)
    elif request.method == 'POST':
        cliente_data = JSONParser().parse(request)
        cliente_serializer = ClienteSerializer(data=cliente_data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse("Added Succesfuly", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        cliente_data=JSONParser().parse(request)
        cliente = Cliente.objects.get(id = cliente_data['id'])
        cliente_serializer = ClienteSerializer(cliente, data=cliente_data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse("Updated Sucessfuly", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        cliente = Cliente.objects.get(id = id)
        cliente.delete()
        return JsonResponse("Deleted Sucessfuly", safe=False)