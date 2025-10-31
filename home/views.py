from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    return HttpResponse("Menu")

def inicio(request):
    return render(request, "inicio.html")

def catalogo(request):
    return render(request, "catalogo.html")

def servicios(request):
    return render(request, "servicios.html")

def contacto(request):
    return render(request, "contacto.html")

