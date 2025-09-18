"""
URL configuration for repair_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from repairs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
    
    # Cliente URLs
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/excluir/<int:pk>/', views.cliente_delete, name='cliente_delete'),
    
    # Técnico URLs
    path('tecnicos/', views.tecnico_list, name='tecnico_list'),
    path('tecnicos/novo/', views.tecnico_create, name='tecnico_create'),
    path('tecnicos/editar/<int:pk>/', views.tecnico_edit, name='tecnico_edit'),
    path('tecnicos/excluir/<int:pk>/', views.tecnico_delete, name='tecnico_delete'),
    
    # Equipamento URLs
    path('equipamentos/', views.equipamento_list, name='equipamento_list'),
    path('equipamentos/novo/', views.equipamento_create, name='equipamento_create'),
    path('equipamentos/editar/<int:pk>/', views.equipamento_edit, name='equipamento_edit'),
    path('equipamentos/excluir/<int:pk>/', views.equipamento_delete, name='equipamento_delete'),
    
    # Reparo URLs
    path('reparos/', views.reparo_list, name='reparo_list'),
    path('reparos/novo/', views.reparo_create, name='reparo_create'),
    path('reparos/editar/<int:pk>/', views.reparo_edit, name='reparo_edit'),
    path('reparos/excluir/<int:pk>/', views.reparo_delete, name='reparo_delete'),
    path('reparos/relatorio/<int:reparo_id>/', views.gerar_relatorio_pdf, name='gerar_relatorio_pdf'),
]