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
    mascota =  forms.CharField(label="Nombre", required=True)
    tipo = forms.ChoiceField(choices= tipo,label="tipo", required=True, widget=forms.Select)
    raza = forms.ChoiceField(choices= raza,label="raza", required=True, widget=forms.Select)
    años = forms.CharField(label="años", required=True, widget=forms.Select)
    dueño = forms.CharField(label="Dueño", required=True)
    descripcion = forms.CharField(label="descripcion", required=True, widget=forms.Textarea)
    fecha = forms.DateField(label="fecha", required=True, widget=forms.TimeInput)
    hora = forms.TimeField(label="hora", required=True)
