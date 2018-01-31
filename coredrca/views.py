from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from multiprocessing.sharedctypes import template

def artigo(request, ano):
    return HttpResponse('Ola mundo! Estamos no ano de ' + ano + '!!')

def home(request):
    template = loader.get_template('index.html')
    context = RequestContext(template)
    return HttpResponse(template.render(context))
    