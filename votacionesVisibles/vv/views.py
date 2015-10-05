from django.shortcuts import render
from django.http import HttpResponse

#Metodo para controlar la pagina home
def index(request):
    return render(request, 'vv/base.html')
