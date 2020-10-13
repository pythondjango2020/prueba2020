from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def vista_base(request):
    return render(request, 'base.html')

def vista_index(request):
    return render(request, 'index.html')
