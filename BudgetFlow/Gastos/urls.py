from django.urls import path
from Gastos import views

urlpatterns = [
    path('add_despesa/', views.add_despesa, name='add_despesa'),
    path('add_receita/', views.add_receita, name='add_receita'),
]