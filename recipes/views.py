from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse(request, 'recipes/home.html')


def sobre(request):
    return HttpResponse('sobre')


def contato(request):
    return HttpResponse('contato')
