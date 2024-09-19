from django.urls import path
from Login import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('login/', views.login_usuario,name = 'login')
]