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
    ('Pajaro','periquillo'),
    ('PezG', 'pez globo'),
    ('PezP', 'pez payaso'),
    
)
años =(
    ('1 a 5','Entre 1 y 5 meses'),
    ('6 a 12','Entre 6 y 12 meses'),
    ('1 a 4','Entre 1 y 4 años'),
    ('5 a 7','Entre 5 y 7 años'),
    ('8 a 10','Entre 8 y 10 años'),
    ('11 a 13','Entre 11 y 13 años'),
    ('N','No Sabe')
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
    mascota =  forms.CharField(label="Nombre", required=True, widget=forms.TextInput)
    tipo = forms.ChoiceField(choices= tipo,label="tipo", required=True, widget=forms.Select)
    raza = forms.ChoiceField(choices= raza,label="raza", required=True, widget=forms.Select)
    años = forms.ChoiceField(choices= años,label="años", required=True, widget=forms.Select)
    dueño = forms.CharField(label="Dueño", required=True)
    descripcion = forms.CharField(label="descripcion", required=True, widget=forms.Textarea)
    fecha = forms.DateField(label="fecha", required=True, widget=forms.TimeInput)
    hora = forms.TimeField(label="hora", required=True)
