from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'global/home.html', context={
        'name': 'Samuel Santos',
    })


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
