from django.db import models

class Estabelecimentos(models.Model):
    cnpj_basico = models.CharField(max_length=255)
    cnpj_ordem = models.CharField(max_length=255)
    cnpj_dv = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255, editable=False, primary_key=True)
    ind_m_f = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    situacao_cadastral = models.CharField(max_length=255)
    data_situacao_cadastral = models.CharField(null=True, blank=True, max_length=255)
    motivo_situacao_cadastral = models.CharField(max_length=255)
    nome_cid_exterior = models.CharField(max_length=255, null=True, blank=True)
    pais = models.CharField(max_length=255)
    data_inicio_atividade = models.CharField(null=True, blank=True, max_length=255)
    cnae_principal = models.CharField(max_length=255)
    cnae_secundarios = models.CharField(max_length=255, null=True, blank=True)
    tipo_logradouro = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    ddd1 = models.CharField(max_length=255)
    telefone1 = models.CharField(max_length=255)
    ddd2 = models.CharField(max_length=255, null=True, blank=True)
    telefone2 = models.CharField(max_length=255, null=True, blank=True)
    ddd_fax = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    situacao_especial = models.CharField(max_length=255, null=True, blank=True)
    data_situacao_especial = models.CharField(null=True, blank=True, max_length=255)

    @property
    def cnpj_completo(self):
        return f"{self.cnpj_basico}/{self.cnpj_ordem}-{self.cnpj_dv}"

    def __str__(self):
        return self.nome_fantasia or self.cnpj
    
    class Meta:
        db_table = 'estabelecimentos'