from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=150)
    def __str__(self):
        return self.nome
class Cidade(models.Model):
    nome = models.CharField(verbose_name="Cidade",max_length=150)
    def __str__(self):
        return self.nome
class Bairro(models.Model):
    nome = models.CharField(verbose_name="Bairro",max_length=150)
    def __str__(self):
        return self.nome
class Profissao(models.Model):
    nome = models.CharField(verbose_name="Profissao",max_length=150)
    def __str__(self):
        return self.nome
class Nacionalidade(models.Model):
    nome = models.CharField(max_length=150)
    def __str__(self):
        return self.nome
class Avaliador(models.Model):
    nome = models.CharField(max_length=150)
    def __str__(self):
        return self.nome
class Cadeira(models.Model):
    numero = models.CharField(max_length=4,unique=True)
    def __str__(self):
        return self.numero

class Parentesco(models.Model):
    nome = models.CharField(max_length=150)
    def __str__(self):
        return self.nome

class Estadocivil(models.Model):
    nome = models.CharField(max_length=150)
    def __str__(self):
        return self.nome

class Rotariano(models.Model):
    nome = models.CharField(max_length=150)
    fone = models.CharField(max_length=150)
    presidente = models.CharField(max_length=150)
    profissao = models.CharField(max_length=150)
    estadocivil = models.CharField(max_length=150)
    identidade = models.CharField(max_length=150)
    cpf = models.CharField(max_length=150)
    endereco =models.CharField(max_length=150)
    distrito =models.CharField(max_length=150)
    sede = models.CharField(max_length=250)

    def __str__(self):
        return self.nome
