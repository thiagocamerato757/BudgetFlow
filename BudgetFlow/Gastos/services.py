from django.forms import ValidationError
from .models import Receita,Despesa


def listar_receitas_aux(user):
    return Receita.objects.filter(user=user)

def listar_despesas_aux(user):
    return Despesa.objects.filter(user=user)

def remover_receita_aux(receita_id, user):
    try:
        receita = Receita.objects.get(id=receita_id, user=user)
        receita.delete()
        return True
    except Receita.DoesNotExist:
        return False
    
def remover_despesa_aux(despesa_id, user):
    try:
        despesa = Despesa.objects.get(id=despesa_id, user=user)
        despesa.delete()
        return True
    except Despesa.DoesNotExist:
        return False
    
def editar_receita_aux(receita_id, user, nova_descricao=None, novo_valor=None, nova_data=None, nova_categoria=None):
    try:
        receita = Receita.objects.get(id=receita_id, user=user)
        if nova_descricao:
            receita.descricao = nova_descricao
        if novo_valor is not None:
            receita.valor = novo_valor
        if nova_data:
            receita.data = nova_data
        if nova_categoria:
            receita.categoria = nova_categoria
        receita.full_clean()  # Valida os dados antes de salvar
        receita.save()
        return receita
    except Receita.DoesNotExist:
        return None
    except ValidationError as e:
        return f"Erro de validação: {e}"
