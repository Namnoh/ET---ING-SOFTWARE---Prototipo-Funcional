from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . import models

# Formularios
ciudades_choices= [
    ('', '---------'),
    ('Santiago', 'Santiago'),
    ('Melipilla', 'Melipilla'),
    ('Maipo','Maipo'),
    ('Talagante','Talagante'),
    ('Chacabuco','Chacabuco'),
    ('Cordillera','Cordillera'),
    ('Melipilla','Melipilla'),
]

class datosForm(forms.ModelForm):

    class Meta: 
        model = models.datosPasajero
        fields = ['paId', 'paCiudad', 'paComuna', 'paDireccion', 'paSeats']
        labels ={
            'paId': 'Id',
            'paCiudad': 'Ciudad',
            'paComuna': 'Comuna',
            'paDireccion': 'Dirección',
            'paSeats': 'Cantidad de asientos a comprar'
        }
        widgets={
            'paCiudad': forms.Select(
                attrs={ 
                    'class': 'form-control',
                    'id': 'paCiudad'
                },
                choices=ciudades_choices
            ), 
            'paComuna': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'paComuna'
                }
            ),
            'paDireccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su dirección',
                    'id': 'paDireccion'
                }
            ),
            'paSeats': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la cantidad',
                    'id': 'paSeats'
                }
            )
        }