# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import json
from .models import ProyectoDeLeyProyectoley
from .models import GeneralTema

# Metodo para controlar la pagina home


def index(request):
    return render(request, 'vv/base.html')

# Metodo que contiene la informacion necesari aora mostrar todos los proyectos en el treemap


def main_proyectos(request):
    proyectos_periodo = ProyectoDeLeyProyectoley.objects.filter(periodo__id=7).order_by('-fecha_radicacion')
    temas = GeneralTema.objects.all()
    data = {}
    data_proyectos = {}

    for tema in temas:
        data[tema.nombre] = {
            'Sancionados': 0,
            'En debate': 0,
            'Archivados': 0,
        }
        data_proyectos[tema.nombre] = {
            'Sancionados': [],
            'En debate': [],
            'Archivados': [],
        }
    print len(temas)
    for proyecto in proyectos_periodo:
        estado = proyecto.estado_proyecto_ley_actual.estado
        json_proyecto = {
            'id': proyecto.id,
            'titulo': proyecto.titulo,
            'iniciativa': proyecto.iniciativa.nombre,
            'estado': estado.nombre,
        }

        # temp = str(proyecto.tema_principal.nombre)
        temp = proyecto.tema_principal.nombre
        if estado.id == 40 or estado.id == 41:
            data[temp]['Sancionados'] += 1
            data_proyectos[temp]['Sancionados'].append(json_proyecto)
        elif estado.id in range(32, 35):
            data[temp]['Archivados'] += 1
            data_proyectos[temp]['Archivados'].append(json_proyecto)
        else:
            data[temp]['En debate'] += 1
            data_proyectos[temp]['En debate'].append(json_proyecto)

    # print data
    return render(request, 'vv/main_proyectos.html',
                  {'data': json.dumps(data), 'proyectos': json.dumps(data_proyectos)})


def detalle_proyecto(request, proyecto_id):
    proyecto = ProyectoDeLeyProyectoley.objects.get(id=proyecto_id)

    return render(request, 'vv/detalle_proyecto.html', {'proyecto': proyecto})
