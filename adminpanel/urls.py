from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('catalogo/', views.catalogo_list, name='catalogo_list'),
    path('catalogo/agregar/', views.catalogo_add, name='catalogo_add'),
    path('catalogo/eliminar/<int:id>/', views.catalogo_delete, name='catalogo_delete'),
]