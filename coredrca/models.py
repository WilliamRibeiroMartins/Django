from django.db import models

class Credito(models.Model):
    d_credito = models.IntegerField()
    d_credito_p = models.IntegerField()
    a_credito_o = models.IntegerField()
    a_credito_l = models.IntegerField()
    
    def __str__(self):
        return "Quant. Creditos: "+str(self.a_credito_l)


class Departamento(models.Model):
    nome = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length = 30)
    departamento = models.ForeignKey(Departamento, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome


class Secretaria(models.Model):
    nome = models.CharField(max_length = 30)
    tipo = models.IntegerField() #Tipo '0' para graduados, Tipo '1' para pós-graduados
    departamento = models.ForeignKey(Departamento, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length = 30)
    secretaria = models.ForeignKey(Secretaria, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    

class Disciplina(models.Model):
    nome = models.CharField(max_length = 30)
    codigo = models.CharField(max_length = 30)
    obr_let = models.CharField(max_length = 30)
    status = models.CharField(max_length = 30)
    credito = models.ForeignKey(Credito, null=False, on_delete=models.CASCADE)
    d_requisito = models.ManyToManyField('Disciplina', blank=True)
    curso = models.ForeignKey(Curso, null=False, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length = 30)
    matricula = models.IntegerField()
    curso = models.ForeignKey(Curso, null=False, on_delete=models.CASCADE)
    credito = models.ForeignKey(Credito, null=False, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina, blank=True)
    
    def __str__(self):
        return self.nome
    
    
    
    