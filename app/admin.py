from django.contrib import admin
from .models import Marca, Producto, Registro
# Register your models here.

admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Registro)