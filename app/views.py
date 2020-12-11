from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import RegistroForm, ProductoForm, CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import unathenticated_user, allowed_users

from django.contrib.auth.decorators import login_required
# Create your views here.

@unathenticated_user
def registrarse(request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Una cuenta fue creada para ' + user)

				return redirect('ingreso')
			

		context = {'form':form}

		return render(request, 'app/cuentas/registrarse.html', context)

@unathenticated_user
def ingreso(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'El usuario O la contraseña es incorrecta')

    context = {}
    return render(request, 'app/cuentas/ingreso.html', context)

def home(request):
    return render(request, 'app/home.html')

def menu(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/menu.html', data)

@login_required(login_url='ingreso')
@allowed_users(allowed_roles=['admin'])
def agregar_producto(request):

    data= {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario =ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

@login_required(login_url='ingreso')
@allowed_users(allowed_roles=['admin'])
def registro(request):
    data={
        'form': RegistroForm()
    }

    if request.method == 'POST':
        formulario =RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro Guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/registro.html', data)

@login_required(login_url='ingreso')
@allowed_users(allowed_roles=['admin'])
def modificar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)

    data={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="menu")
        data["form"] = formulario

    return render(request, 'app/producto/modificar.html',data)

@login_required(login_url='ingreso')
@allowed_users(allowed_roles=['admin'])
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="menu")

@login_required(login_url='ingreso')
@allowed_users(allowed_roles=['admin'])
def listar_producto(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/producto/listar.html', data)