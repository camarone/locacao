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
    numero = models.CharField(max_length=4)
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
