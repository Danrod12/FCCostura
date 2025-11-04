from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.models import *  # si luego tienes modelos de fotos, productos, etc.
from django.shortcuts import render, redirect, get_object_or_404
from home.models import CatalogoItem

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'adminpanel/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'adminpanel/login.html')


#@login_required
def admin_dashboard(request):
    # Aquí puedes traer datos de modelos, como productos, servicios, etc.
    return render(request, 'adminpanel/dashboard.html')


#@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')


# @login_required
def catalogo_list(request):
    items = CatalogoItem.objects.all().order_by('-fecha_creacion')
    return render(request, 'adminpanel/catalogo_list.html', {'items': items})


# @login_required
def catalogo_add(request):
    if request.method == 'POST':
        imagen = request.FILES['imagen']
        categoria = request.POST['categoria']
        CatalogoItem.objects.create(
            imagen=imagen,
            categoria=categoria
        )
        return redirect('catalogo_list')
    return render(request, 'adminpanel/catalogo_add.html')



# @login_required
def catalogo_delete(request, id):
    item = get_object_or_404(CatalogoItem, id=id)
    item.delete()
    return redirect('catalogo_list')
