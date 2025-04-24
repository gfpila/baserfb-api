from django.db import models

class Municipio(models.Model):
    codigo_municipio = models.CharField(max_length=10, primary_key=True)
    descricao_municipio = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao_municipio
    
    class Meta:
        db_table = 'municipios'


class Estabelecimentos(models.Model):
    razao = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20, primary_key=True)
    cnpj_basico = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    situacao_cadastral = models.CharField(max_length=255)
    data_inicio_atividade = models.CharField(null=True, blank=True, max_length=255)
    cnae_principal = models.CharField(max_length=255)
    cnae_secundarios = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.CharField(max_length=1000)
    cep = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    municipio = models.CharField(max_length=10, null=True, blank=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.razao or self.cnpj

    class Meta:
        db_table = 'estabelecimentos'