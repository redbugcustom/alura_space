from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse('<h1>Alura Spcace<p>Bem vindo ao espçao</p></h1>')
