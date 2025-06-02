from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Estabelecimentos
from .serializers import EstabelecimentoSerializer


class EstabelecimentosListView(generics.ListAPIView):
    queryset = Estabelecimentos.objects.all()[:50000]  # Limite de 50 mil
    serializer_class = EstabelecimentoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['razao', 'cnpj', 'nome_fantasia', 'situacao_cadastral', 'data_inicio_atividade', 'cnae_principal', 'endereco', 'cep', 'uf', 'municipio']
