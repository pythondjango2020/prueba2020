from django import forms
from .models import *

tipo = (
    ('gato','gato'),
    ('Perros','Perros'),
    ('Pajaros','Pajaros'),
    ('Peces','Peces'),
)
raza=(
    ('Huski','Huski siberiano'),
    ('Golden','Golden retriever'),
    ('caniche','caniche'),
    ('Pastor','Pastor aleman'),
    ('dalmata','Dalmata'),
    ('chihuahua','chihuahua'),
)

class citaform(forms.Form):
    mascota =  forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=100)

    tipo = forms.ChoiceField(choices= tipo,label="tipo", required=True, widget=forms.Select(
        attrs={'class':'form-control'}
    ))

    raza = forms.ChoiceField(choices= raza,label="raza", required=True, widget=forms.Select(
        attrs={'class':'form-control'}
    ))

    años = forms.CharField(label="años", required=True, widget=forms.Select(
        attrs={'class':'form-control'}
    ))

    dueño = forms.CharField(label="Dueño", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=100)

    descripcion = forms.CharField(label="descripcion", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Escribe tu mensaje'}
    ), min_length=10, max_length=1000)

    fecha = forms.DateField(label="fecha", required=True, widget=forms.TimeInput(
        attrs={'class':'form-control', 'type':'date'}
    ))
    
    hora = forms.TimeField(label="hora", required=True, widget=forms.DateInput(
        attrs={'class':'form-control', 'type':'time'}
    ))