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
            # Criptografar a senha usando bcrypt
            password = form.cleaned_data['password']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            # Atualizar o campo de senha do formulário com a senha criptografada
            form.cleaned_data['password'] = hashed_password
            
            # Salvar o usuário com a senha criptografada
            form.save()
            return redirect('/login')  # Redirecionar para a página de login
    else:
        form = UserRegisterForm()
    
    return render(request, 'Login/cadastro.html', {'form': form})


def login_usuario(request):
    return HttpResponse("teste")