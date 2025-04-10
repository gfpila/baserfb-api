from rest_framework import serializers

from .models import Estabelecimentos


class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimentos
        fields = ['cnpj', 'nome_fantasia', 'data_inicio_atividade', 'cnae_principal',  'cnae_secundarios', 'logradouro', 'cep', 'uf', 'municipio', 'telefone1', 'email']