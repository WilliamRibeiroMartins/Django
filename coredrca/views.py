from django.shortcuts import render
from boto.connection import HTTPResponse

# Create your views here.

def artigo(request):
    return HTTPResponse('Ola mundo! Estamos no ano de ')