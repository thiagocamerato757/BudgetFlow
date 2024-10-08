from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import DespesaForm
@login_required(login_url='login')
def add_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_despesa')
    else:
        form = DespesaForm()

    return render(request, 'Gastos/add_despesas.html', {'form': form})


@login_required(login_url='login')
def add_receita(request):
    return render(request, 'Gastos/add_receita.html')
