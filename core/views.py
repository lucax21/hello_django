from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
    return HttpResponse('<h1>Hello {}</h1>'.format(nome))

def soma(request, a, b):
    return HttpResponse('{} + {} = {}'.format(a,b,a+b))

def subtracao(resquest, a, b):
    return HttpResponse('{} - {} = {}'.format(a,b, a -b))

def multiplicacao(request, a, b):
    return HttpResponse('{} * {} = {}'.format(a,b,a*b))

def divisao(request, a, b):
    return HttpResponse('{} / {} = {}'.format(a,b,a/b))
