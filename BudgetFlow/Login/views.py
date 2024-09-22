from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserRegisterForm
import bcrypt

def homepage(request):
    return render(request, 'Login/homepage.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  # Redirecionar para a página de login
    else:
        form = UserRegisterForm()
    
    return render(request, 'Login/cadastro.html', {'form': form})


def login_usuario(request):
    return HttpResponse("teste")