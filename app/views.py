from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def menu(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/menu.html', data)

def registro(request):
    return render(request, 'app/registro.html')