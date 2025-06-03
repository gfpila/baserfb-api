# views.py
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend

from .models import Estabelecimentos
from .serializers import EstabelecimentoSerializer
from .filters import EstabelecimentosFilter

class EstabelecimentosListView(generics.ListAPIView):
    queryset = Estabelecimentos.objects.all()
    serializer_class = EstabelecimentoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EstabelecimentosFilter

    def get_queryset(self):
        municipio = self.request.query_params.get('municipio')
        if not municipio:
            raise ValidationError({"municipio": "O filtro 'municipio' é obrigatório."})
        return super().get_queryset()
