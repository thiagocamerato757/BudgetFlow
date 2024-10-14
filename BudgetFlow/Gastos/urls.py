from django.urls import path
from Gastos import views

urlpatterns = [
    path('add_despesa/', views.add_despesa, name='add_despesa'),
    path('add_receita/', views.add_receita, name='add_receita'),
    path('receitas/', views.listar_receitas_view, name='listar_receitas'),
    path('despesas/', views.listar_despesas_view, name='listar_despesas'),
    path('remover_receita/<int:receita_id>/', views.remover_receita_view, name='remover_receita'),
    path('remover_despesa/<int:despesa_id>/', views.remover_despesa_view, name='remover_despesa'),
    path('editar_despesa/<int:despesa_id>/', views.editar_despesa_view, name='editar_despesa'),
    path('editar_receita/<int:receita_id>/', views.editar_receita_view, name='editar_receita'),
]