from django.shortcuts import render
from django.http import HttpResponse
from .models import Disfraz
from collections import defaultdict
from .models import CatalogoItem

def menu(request):
    return HttpResponse("Menu")

def inicio(request):
    return render(request, "inicio.html")


def catalogo(request):
    disfraces = Disfraz.objects.all()
    
    # Agrupamos los disfraces por categoría
    categorias = defaultdict(list)
    for disfraz in disfraces:
        categorias[disfraz.categoria].append(disfraz)
    
    return render(request, 'catalogo.html', {'categorias': categorias})

def servicios(request):
    return render(request, "servicios.html")

def contacto(request):
    return render(request, "contacto.html")


def catalogo(request):
    cosplays = CatalogoItem.objects.filter(categoria='cosplay')
    uniformes = CatalogoItem.objects.filter(categoria='uniformes')
    personalizados = CatalogoItem.objects.filter(categoria='personalizados')
    otros = CatalogoItem.objects.filter(categoria='otros')

    return render(request, 'catalogo.html', {
        'cosplays': cosplays,
        'uniformes': uniformes,
        'personalizados': personalizados,
        'otros': otros,
    })