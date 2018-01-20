from django.db import models

class Credito(models.Model):
    d_credito = models.IntegerField()
    d_credito_p = models.IntegerField()
    a_credito_o = models.IntegerField()
    a_credito_l = models.IntegerField()
    
class Departamento(models.Model):
    nome = models.CharField(max_length = 30)
    
class Professor(models.Model):
    nome = models.CharField(max_length = 30)
    departamento = models.ForeignKey(Departamento, null = True)
    
class Secretaria(models.Model):
    nome = models.CharField(max_length = 30)
    tipo = models.IntegerField() #Tipo '0' para graduados, Tipo '1' para pós-graduados
    departamento = models.ForeignKey(Departamento, null = True)
    
class Curso(models.Model):
    nome = models.CharField(max_length = 30)
    secretaria = models.ForeignKey(Secretaria, null = True)
    
class Disciplina(models.Model):
    nome = models.CharField(max_length = 30)
    codigo = models.CharField(max_length = 30)
    obr_let = models.CharField(max_length = 30)
    status = models.CharField(max_length = 30)
    credito = models.ForeignKey(Credito)
    d_requisito = models.ManyToManyField('Disciplina')
    curso = models.ForeignKey(Curso)
    professor = models.ForeignKey(Professor, null=True)

class Aluno(models.Model):
    nome = models.CharField(max_length = 30)
    matricula = models.IntegerField()
    curso = models.ForeignKey(Curso)
    credito = models.ForeignKey(Credito)
    disciplinas = models.ManyToManyField(Disciplina, null=True)