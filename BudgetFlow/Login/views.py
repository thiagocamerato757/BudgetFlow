from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserRegisterForm
from .forms import UserLoginForm
from django.contrib.auth import authenticate,login,logout

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
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        print("Form enviado!")
        if form.is_valid():
            print("Form validado!")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Verificando se a autenticação está funcionando
            user = authenticate(request, username=username, password=password)
            print(f"Usuário autenticado: {user}")

            if user is not None:
                login(request, user)
                return redirect('/')  # Redireciona para a homepage após o login
            else:
                form.add_error(None, "Nome de usuário ou senha incorretos.")
    else:
        form = UserLoginForm()

    return render(request, 'Login/login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('/login')