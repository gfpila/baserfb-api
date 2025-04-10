from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Estabelecimentos
from .serializers import EstabelecimentoSerializer

import json

# Create your views here.
@api_view(['GET'])
def get_estabelecimentos(request):
    
    if request.method == 'GET':
        estabelecimentos = Estabelecimentos.objects.all()[:1000]
        serializer = EstabelecimentoSerializer(estabelecimentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response({"error": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        