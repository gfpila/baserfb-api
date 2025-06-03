# filters.py
import django_filters
from .models import Estabelecimentos, Municipio

class EstabelecimentosFilter(django_filters.FilterSet):
    municipio = django_filters.CharFilter(method='filter_municipio', label='Município')
    situacao_cadastral = django_filters.CharFilter(method='filter_situacao_cadastral')

    class Meta:
        model = Estabelecimentos
        fields = [
            'razao', 'cnpj', 'nome_fantasia', 'data_inicio_atividade',
            'cnae_principal', 'endereco', 'cep', 'uf'
        ]

    def filter_municipio(self, queryset, name, value):
        municipios = Municipio.objects.filter(descricao_municipio__iexact=value)
        codigos = municipios.values_list('codigo_municipio', flat=True)
        if not codigos:
            return queryset.none()
        return queryset.filter(municipio__in=codigos)
    
    def filter_situacao_cadastral(self, queryset, name, value):
        # Mapeamento de texto para valor numérico esperado no banco
        situacoes = {
            'NULA': '1',
            'ATIVA': '2',
            'SUSPENSA': '3',
            'INAPTA': '4',
            'BAIXADA': '8'
        }
        
        # Tenta converter entrada para chave do mapa
        valor_banco = situacoes.get(value.upper())
        
        # Se não encontrar no mapa, usa o valor original
        if not valor_banco:
            valor_banco = value
            
        return queryset.filter(situacao_cadastral=valor_banco)
