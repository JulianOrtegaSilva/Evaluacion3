from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Registro, Producto
from django.forms import ModelForm


class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = '__all__'

        widgets = {
            "fecha_nacimiento:": forms.SelectDateWidget()
        }


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']