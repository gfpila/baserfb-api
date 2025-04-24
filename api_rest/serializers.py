from rest_framework import serializers
from .models import Municipio
from .models import Estabelecimentos


class EstabelecimentoSerializer(serializers.ModelSerializer):

    cnpj = serializers.SerializerMethodField()
    situacao_cadastral = serializers.SerializerMethodField()
    municipio = serializers.SerializerMethodField()

    class Meta:
        model = Estabelecimentos
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Carrega todos os municípios na memória uma vez
        self.municipios_map = {
            m.codigo_municipio: m.descricao_municipio
            for m in Municipio.objects.all()
        }

    def get_cnpj(self, obj):
        cnpj = obj.cnpj
        if cnpj:
            return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}" if len(cnpj) == 14 else cnpj
        return None

    def get_situacao_cadastral(self, obj):
        try:
            cod_int = int(obj.situacao_cadastral)
        except (TypeError, ValueError):
            return 'DESCONHECIDA'

        mapa = {
            1: 'NULA',
            2: 'ATIVA',
            3: 'SUSPENSA',
            4: 'INAPTA',
            8: 'BAIXADA',
        }
        return mapa.get(cod_int, 'DESCONHECIDA')

    def get_municipio(self, obj):
        return self.municipios_map.get(obj.municipio, None)
