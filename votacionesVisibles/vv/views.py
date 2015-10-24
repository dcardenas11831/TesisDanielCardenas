# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import ProyectoDeLeyProyectoley, ProyectoDeLeyEstadodeproyectodeley, ProyectoDeLeyVotacion, \
    CongresoPartido, \
    CongresoCongresista
from .models import GeneralTema


# para las fotos tomar la ruta http://congresovisible.org/media/ y sumarle lo que dice la bd
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
    estados = ProyectoDeLeyEstadodeproyectodeley.objects.filter(proyecto=proyecto).order_by('fecha')
    estados_cambio_debate = []
    print "-------------------------------------------------------------"
    fecha_anterior = ""
    votaciones = []
    for estado in estados:
        print "nuemero de estados........................................"
        print str(len(estados)) + "estado: " + estado.estado.nombre
        if estado.estado.id in range(16, 32):
            estados_cambio_debate.append(estado)
            if fecha_anterior != "":
                votaciones_estado = ProyectoDeLeyVotacion.objects.filter(proyecto_id=proyecto_id,
                                                                         tipo_votacion_id__lte=3,
                                                                         fecha__lte=estado.fecha,
                                                                         fecha__gte=fecha_anterior,
                                                                         # motivo__icontains="debate"
                                                                         ).order_by('fecha')
            else:
                votaciones_estado = ProyectoDeLeyVotacion.objects.filter(proyecto_id=proyecto_id,
                                                                         tipo_votacion_id__lte=3,
                                                                         fecha__lte=estado.fecha,
                                                                         # motivo__icontains="debate"
                                                                         ).order_by('fecha')
            votaciones.append(votaciones_estado)
            print "nuemero de votaciones........................................"
            print len(votaciones)
            fecha_anterior = estado.fecha

    partidos = [
        {'name': "La U", 'color': "#FF6600", 'data': [34, 45, 4, 8]},
        {'name': "Conservador", 'color': "#000099", 'data': [12, 34, 90, 5]},
        {'name': "Centro Democrático", 'color': "#00CCFF", 'data': [12, 21, 35, 19]},
        {'name': "Liberal", 'color': "#CC0000", 'data': [4, 45, 27, 23]},
        {'name': "Cambio Radical", 'color': "#FF3366", 'data': [20, 37, 25, 10]},
        {'name': "Verde", 'color': "#339900", 'data': [9, 12, 29, 34]},
        {'name': "Polo", 'color': "#FFCC00", 'data': [29, 10, 20, 9]},
        {'name': "Opción Ciudadana", 'color': "#990066", 'data': [0, 2, 48, 52]},
        {'name': "AICO", 'color': "#330000", 'data': [0, 0, 21, 39]},
    ]
    return render(request, 'vv/detalle_proyecto.html', {'proyecto': proyecto, 'partidos': json.dumps(partidos),
                                                        'votaciones': votaciones})


def autocompletar(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        # Toma todos los partidos activos que tienen el item buscado
        partidos = CongresoPartido.objects.filter(nombre__icontains=q, estado_id=1)[:10]
        congresistas_apellido = CongresoCongresista.objects.filter(persona_ptr__apellidos__icontains=q,
                                                                   es_congresista=True)[:5]
        congresistas_nombre = CongresoCongresista.objects.filter(persona_ptr__nombres__icontains=q,
                                                                 es_congresista=True)[:5]
        results = []
        for partido in partidos:
            drug_json = {'id': partido.id, 'label': partido.nombre, 'value': partido.nombre}
            results.append(drug_json)
        for congresista in congresistas_apellido:
            nombre = congresista.persona_ptr.nombres
            if not nombre.endswith(" "):
                nombre += " "
            nombre += congresista.persona_ptr.apellidos
            drug_json = {'id': congresista.persona_ptr.id, 'label': nombre, 'value': nombre}
            results.append(drug_json)
        for congresista in congresistas_nombre:
            nombre = congresista.persona_ptr.nombres
            if not nombre.endswith(" "):
                nombre += " "
            nombre += congresista.persona_ptr.apellidos
            drug_json = {'id': congresista.persona_ptr.id, 'label': nombre, 'value': nombre}
            results.append(drug_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    print data
    return HttpResponse(data, mimetype)
