from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'Login/homepage.html')

def cadastro_usuario(request):
    return  render(request, 'Login/cadastro.html')