from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from emanga.models import manga
from emanga.serializers import MangaSerializer

# Create your views here.

@csrf_exempt
def mangaApi(request, id=0):
  if request.method=='GET':
    id = request.GET.get('id')
    if id:
        mangas = manga.objects.filter(id=id)
    else:
        mangas = manga.objects.all().order_by('-id')
    manga_serializer = MangaSerializer(mangas, many=True)
    return JsonResponse(manga_serializer.data, safe=False)
  elif request.method=='GET' and 'titulo' in request.path:
    titulo = manga.objects.filter(user_id = id)
    serializer = manga(titulo, many= True)
    return JsonResponse(serializer.data, safe=False)
  elif request.method=='POST':
    manga_data = JSONParser().parse(request)
    manga_serializer = MangaSerializer(data=manga_data)
    if manga_serializer.is_valid():
      manga_serializer.save()
      return JsonResponse("adicionado com sucesso", safe=False)
    return JsonResponse("falha na adição", safe=False)
  elif request.method == 'PUT':
    manga_data = JSONParser().parse(request)
    mangas = manga.objects.get(id=manga_data['id'])
    manga_serializer = MangaSerializer(mangas, data=manga_data)
    if manga_serializer.is_valid():
        manga_serializer.save()
        return JsonResponse("atualização feita", safe=False)
    return JsonResponse("falha na atualização")
  elif request.method=="DELETE":
    mangas = manga.objects.get(id = id)
    mangas.delete()
    return JsonResponse("deletado com sucesso", safe=False)

