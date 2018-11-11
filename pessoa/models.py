from django.db import models
from parametros.models import Profissao
from parametros.models import Bairro, Cidade, Estadocivil, Estado, Parentesco  , Cadeira, CadeiraDeBanho, Andador, Muleta

class Pessoa(models.Model):
    registro = models.CharField(max_length=20, blank=True)
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    profissao = models.ForeignKey(Profissao, on_delete=models.SET_NULL, blank=True, null=True)
    nacionalidade = models.CharField(max_length=25, blank=True)
    rg = models.CharField(max_length=15, blank=True)
    cep = models.CharField(verbose_name="Cep", max_length=15, blank=True)
    endereco = models.CharField(max_length=50, verbose_name="Endereço", blank=True)
    numero = models.CharField(max_length=15, blank=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.SET_NULL, blank=True, null=True)
    municipios = models.ForeignKey(Cidade, on_delete=models.SET_NULL, blank=True, null=True)
    etadocivil = models.ForeignKey(Estadocivil, on_delete=models.SET_NULL, blank=True, null=True)
    uf = models.ForeignKey(Estado, on_delete=models.SET_NULL, blank=True, null=True)
    telefone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    def __str__(self):
        return self.nome

class CadastroDeAluguel(models.Model):
    usuario = models.OneToOneField(Pessoa, related_name='usuario2usuario', on_delete=models.SET_NULL, null=True, unique=True)
    comodante = models.ForeignKey(Pessoa, related_name='comodante2comodante', on_delete=models.SET_NULL, null=True)
    dataRequerimento = models.DateField(verbose_name="Data de Requerimento", blank=True,null=True)
    dataLocacao = models.DateField(verbose_name="Data de Devolução", blank=True,null=True)
    parentesco = models.ForeignKey(Parentesco, on_delete=models.SET_NULL, blank=True, null=True,verbose_name="Grau de Parentesco")
    cadeira = models.ForeignKey(Cadeira, on_delete=models.SET_NULL, blank=True, null=True,verbose_name="Codigo Cadeira")
    cadeiraDeBanho = models.ForeignKey(CadeiraDeBanho, on_delete=models.SET_NULL, blank=True, null=True,verbose_name="Codigo Cadeira de Banho")
    andador = models.ForeignKey(Andador, on_delete=models.SET_NULL, blank=True, null=True,verbose_name="Codigo Andador")
    muleta = models.ForeignKey(Muleta, on_delete=models.SET_NULL, blank=True, null=True,verbose_name="Codigo Muleta")
    dataEmprestimoCadeira = models.DateField(verbose_name="Emprestimo Cadeira", blank=True,null=True)
    dataEmprestimoCadeiraDeBanho = models.DateField(verbose_name="Emprestimo Cadeira de Banho", blank=True,null=True)
    dataEmprestimoMuleta = models.DateField(verbose_name="Emprestimo Muleta", blank=True,null=True)
    dataEmprestimoAndador = models.DateField(verbose_name="Emprestimo Andador", blank=True,null=True)
    dataDevolucaoCadeira = models.DateField(verbose_name="Devolucao Cadeira", blank=True,null=True)
    dataDevolucaoCadeiraDeBanho = models.DateField(verbose_name="Devolucao Cadeira de Banho", blank=True,null=True)
    dataDevolucaoMuleta = models.DateField(verbose_name="Devolucao Muleta", blank=True,null=True)
    dataDevolucaoAndador = models.DateField(verbose_name="Devolucao Andador", blank=True,null=True)


    def dataRequerimentoFormatado(self):
        data_ral = dataRequerimento.day+'/'+dataRequerimento.month+'/'+dataRequerimento.year
        return data_ral

    def __str__(self):
        return self.usuario.__str__().upper()

    def __unicode__(self):
        return self.nome.upper()
