from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('galeria/', views.galeria, name='galeria'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
]