from django.urls import path
from .views import home, menu, registro

urlpatterns = [
    path('', home, name = "home"),
    path('menu/', menu, name = "menu"),
    path('registro/', registro, name = "registro")
]
