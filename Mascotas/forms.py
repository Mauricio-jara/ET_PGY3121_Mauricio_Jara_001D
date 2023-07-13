from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import Productos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos          
        fields = ['dv', 'nombre', 'descripcion', 'cantidad', 'precio', 'imagen']
        labels = {                
            'dv': 'Id',
            'nombre' : 'Nombre',
            'descripcion' : 'Descripcion',
            'precio':'Precio',
            'imagen':'Imagen'
        }
        widgets = {
            'dv' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese id del producto..',
                    'id':'dv',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre del producto..',
                    'id':'nombre',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripición del producto..',
                    'id':'descripcion',
                }
            ),
            'cantidad': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese cantidad del producto..',
                    'id':'cantidad',
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese precio del producto..',
                    'id':'precio',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen',
                }
            ),
        }
