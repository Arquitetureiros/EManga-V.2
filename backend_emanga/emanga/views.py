from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from emanga.models import manga, produto
from emanga.serializers import MangaSerializer, ProdutoSerializer

# Create your views here.

def getTest(request):
  return JsonResponse({'valortes': 1, 'message': 'bao'})

def receber_dado(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        print(titulo)
        return HttpResponse('Dado recebido com sucesso!')
    return HttpResponse('Requisição inválida')

@csrf_exempt
def mangaApi(request, id=0):
  if request.method=='GET':
    id = request.GET.get('id')
    print(id)
    if id:
        mangas = manga.objects.filter(id=id, quantidade__gt=0)
    else:
        mangas = manga.objects.filter(quantidade__gt=0)
    manga_serializer = MangaSerializer(mangas, many=True)
    return JsonResponse(manga_serializer.data, safe=False)
  elif request.method=='POST':
    manga_data = JSONParser().parse(request)
    manga_serializer = MangaSerializer(data=manga_data)
    if manga_serializer.is_valid():
      manga_serializer.save()
      return JsonResponse("adicionado com sucesso", safe=False)
    return JsonResponse("falha na adição", safe=False)
  elif request.method == 'PUT':
    manga_data = JSONParser().parse(request)
    mangas = manga.objects.get(id=id)
    manga_serializer = MangaSerializer(mangas, data=manga_data)
    if manga_serializer.is_valid():
        manga_serializer.save()
        return JsonResponse("atualização feita", safe=False)
    return JsonResponse("falha na atualização")
  elif request.method=="DELETE":
    mangas = manga.objects.get(id = id)
    mangas.delete()
    return JsonResponse("deletado com sucesso", safe=False)




