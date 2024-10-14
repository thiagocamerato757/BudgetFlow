from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Receita, Despesa
from .forms import DespesaForm, ReceitaForm
from .services import listar_receitas_aux, listar_despesas_aux, remover_receita_aux, remover_despesa_aux, editar_receita_aux

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

@login_required(login_url='login')
def listar_receitas_view(request):
    receitas = listar_receitas_aux(request.user)
    return render(request, 'Gastos/listar_receitas.html', {'receitas': receitas})

@login_required(login_url='login')
def listar_despesas_view(request):
    despesas = listar_despesas_aux(request.user)
    return render(request, 'Gastos/listar_despesas.html', {'despesas': despesas})

@login_required(login_url='login')
def remover_receita_view(request, receita_id):
    sucesso = remover_receita_aux(receita_id, request.user)
    if sucesso:
        return redirect('listar_receitas')
    else:
        return render(request, 'Gastos/listar_receitas.html', {'erro': 'Receita inexistente ou erro ao deletar.'})
    
@login_required(login_url='login')
def remover_despesa_view(request, despesa_id):
    sucesso = remover_despesa_aux(despesa_id, request.user)
    if sucesso:
        return redirect('listar_despesas')
    else:
        return render(request, 'Gastos/listar_despesas.html', {'erro': 'Despesa inexistente ou erro ao deletar.'})
@login_required(login_url='login')
def editar_receita_view(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id, user=request.user)
    
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=receita)
        if form.is_valid():
            form.save()
            return redirect('listar_receitas')
        else:
            return render(request, 'Gastos/editar_receitas.html', {'form': form, 'receita': receita})
    
    # Se for GET, exibe o formulário pré-preenchido
    form = ReceitaForm(instance=receita)
    return render(request, 'Gastos/editar_receitas.html', {'form': form, 'receita': receita})

@login_required(login_url='login')
def editar_despesa_view(request, despesa_id):
    despesa = get_object_or_404(Despesa, id=despesa_id, user=request.user)
    
    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            return redirect('listar_despesas')
        else:
            return render(request, 'Gastos/editar_despesas.html', {'form': form, 'despesa': despesa})
    
    # Se for GET, exibe o formulário pré-preenchido
    form = DespesaForm(instance=despesa)
    return render(request, 'Gastos/editar_despesas.html', {'form': form, 'despesa': despesa})
