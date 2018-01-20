from django.db import models

class Credito(models.Model):
    d_credito = models.IntegerField()
    a_credito_o = models.IntegerField()
    a_credito_l = models.IntegerField()
    

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    matricula = models.IntegerField()
    