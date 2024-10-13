from django import forms
from .models import Despesa, Receita
from datetime import date

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['descricao', 'valor', 'data', 'categoria']  # Campos do modelo

    descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.FloatField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    categoria = forms.ChoiceField(choices=Despesa.CATEGORIAS_DESPESAS, widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_data(self):
        data = self.cleaned_data.get('data')
        if data and data > date.today():
            raise forms.ValidationError("A data não pode ser no futuro.")
        return data


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['descricao', 'valor', 'data', 'categoria']  # Campos do modelo

    descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.FloatField(min_value = 0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    categoria = forms.ChoiceField(choices=Receita.CATEGORIAS_RECEITAS, widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_data(self):
        data = self.cleaned_data.get('data')
        if data > date.today():
            raise forms.ValidationError("A data não pode ser no futuro.")
        return data
