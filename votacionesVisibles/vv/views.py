from django.shortcuts import render
from django.http import HttpResponse

#Metodo para controlar la pagina home
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
