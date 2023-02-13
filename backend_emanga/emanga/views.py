from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
import json

# from .serializers import ModelSerializer

def test_message(request):
    print(json.loads(request));
    return JsonResponse(request)
# Create your views here.
