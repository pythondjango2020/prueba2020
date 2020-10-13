from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
# Create your views here.
from django.shortcuts import render

# Create your views here.
def vista_base(request):
    return render(request, 'base.html')

def vista_index(request):
    cita_form = citaform()

    if request.method == "POST":
        cita_form = citaform(data=request.POST)
        if cita_form.is_valid():
            mascota = request.POST.get('name', '')
            tipo = request.POST.get('name', '')
            raza = request.POST.get('name', '')
            años = request.POST.get('name', '')
            dueño = request.POST.get('name', '')
            descripcion = request.POST.get('name', '')
            fecha = request.POST.get('name', '')
            hora = request.POST.get('name', '')
            return redirect(reverse('index')+"?ok")
    return render(request, 'index.html',{'form':cita_form})

def vista_login(request):
    return render(request, 'login.html')

def vista_register(request):
    return render(request, 'register.html')
