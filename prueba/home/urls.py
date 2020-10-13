from django.urls import path
from .views import *

urlpatterns = [
    path('', vista_base, name = 'base'),
    path('index/', vista_index, name = 'index'),
]