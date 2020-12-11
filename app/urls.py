from django.urls import path
from .views import home, menu, registro, agregar_producto,modificar_producto, eliminar_producto, registrarse, ingreso, listar_producto

urlpatterns = [
    path('', home, name = "home"),
    path('menu/', menu, name = "menu"),
    path('registro/', registro, name = "registro"),
    path('agregar-producto/', agregar_producto, name = "agregar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name = "modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),

    path('registrarse/', registrarse, name = "registrarse"),
    path('ingreso/', ingreso, name = "ingreso"),
]
