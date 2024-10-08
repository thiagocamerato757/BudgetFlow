from django.urls import include, path
from Login import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('login/', views.login_usuario,name = 'login'),
    path('logout/', views.logout_usuario,name = 'logout'),
    path('',include('Gastos.urls')),
]