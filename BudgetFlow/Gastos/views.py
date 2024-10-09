from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import DespesaForm, ReceitaForm

@login_required(login_url='login')
def add_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)  # Não salva ainda, precisamos associar o usuário
            despesa.user = request.user  # Associa o usuário logado à despesa
            despesa.save()  # Agora salva a despesa
            return redirect('add_despesa')
    else:
        form = DespesaForm()

    return render(request, 'Gastos/add_despesas.html', {'form': form})


@login_required(login_url='login')
def add_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita = form.save(commit=False)  # Não salva ainda, precisamos associar o usuário
            receita.user = request.user  # Associa o usuário logado à receita
            receita.save()  # Agora salva a receita
            return redirect('add_receita')
    else:
        form = ReceitaForm()

    return render(request, 'Gastos/add_receitas.html', {'form': form})
