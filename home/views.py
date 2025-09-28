from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    return HttpResponse("Menu")

def inicio(request):
    return render(request, "inicio.html")

def galeria(request):
    return render(request, "galeria.html")

def servicios(request):
    return render(request, "servicios.html")

def contacto(request):
    return render(request, "contacto.html")
