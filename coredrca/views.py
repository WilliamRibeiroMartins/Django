from django.http.response import HttpResponse
from django.template import loader
from coredrca.models import Aluno

'''
def artigo(request, ano):
    return HttpResponse('Ola mundo! Estamos no ano de ' + ano + '!!')
'''

def home(request):
    template = loader.get_template('index.html')
    context = {'alunos' : alunos}
    return HttpResponse(template.render(context, request))
    
def alunos(request):
    alunos = Aluno.objects.all()
    teste = 'Alunos'
    template = loader.get_template('alunos.html')
    context = {'alunos' : alunos}
    return HttpResponse(template.render(context, request))