from django import forms
from .models import Despesa, Receita

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['descricao', 'valor', 'data', 'categoria']  # Campos do modelo

    # Adicione aqui widgets ou customizações adicionais, se necessário
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    categoria = forms.ChoiceField(choices=Despesa.CATEGORIAS_DESPESAS, widget=forms.Select(attrs={'class': 'form-control'}))


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['descricao', 'valor', 'data', 'categoria']  # Campos do modelo

    # Adicione aqui widgets ou customizações adicionais, se necessário
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    categoria = forms.ChoiceField(choices=Receita.CATEGORIAS_RECEITAS, widget=forms.Select(attrs={'class': 'form-control'}))
