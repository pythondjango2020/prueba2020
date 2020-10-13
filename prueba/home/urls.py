from django.urls import path
from .views import *

urlpatterns = [
    path('', vista_base, name = 'base'),
    path('index/', vista_index, name = 'index'),
    path('login/', vista_login, name = 'login'),
    path('register/', vista_register, name = 'register'),
    path('formulario/', vista_forms, name = 'formulario'),
    path('tienda/', vista_tienda, name = 'tienda'),
]