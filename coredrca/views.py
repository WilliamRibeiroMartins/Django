from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def artigo(request, ano):
    return HttpResponse('Ola mundo! Estamos no ano de ' + ano + '!!')