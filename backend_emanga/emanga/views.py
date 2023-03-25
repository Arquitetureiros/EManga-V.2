from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.http import JsonResponse
import json

# from .serializers import ModelSerializer

@csrf_exempt
def test_message(request):
    print(request)
    body_unicode = request.body.decode('utf-8')
    # Converter a string JSON em um objeto Python
    response = json.loads(body_unicode)
    print(response['nr_cartao'])
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