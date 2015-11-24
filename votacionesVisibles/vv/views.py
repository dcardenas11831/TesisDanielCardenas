# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from operator import itemgetter
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, Count, IntegerField, When, Case
import json
from .models import ProyectoDeLeyProyectoley, ProyectoDeLeyEstadodeproyectodeley, ProyectoDeLeyVotacion, \
    CongresoPartido, CongresoCongresista, ProyectoDeLeyVoto, CongresoPeriodocongresista, \
    ProyectoDeLeyAutorproyectoley, ProyectoDeLeyLegislatura
from .models import GeneralTema
from datetime import datetime

# Constantes
ID_PERIODO = 7
MEDIA_URL = "http://congresovisible.org/media/"


def proyectos_clave():
    claves = ProyectoDeLeyProyectoley.objects.filter(periodo__id=ID_PERIODO, destacado=True) \
                 .order_by('-fecha_radicacion')[:4]
    resultado = []
    for pc in claves:
        sp = pc.titulo.split("[")
        nombre_corto = sp[len(sp) - 1][:-1]  # se toma el nombre corto cuando es posible
        if nombre_corto == "":
            nombre_corto = pc.titulo
        p = {
            'nombre': nombre_corto,
            'id': pc.id,
        }
        resultado.append(p)
    return resultado


# Metodo para controlar la pagina home
def index(request):
    p_claves = proyectos_clave()
    return render(request, 'vv/base.html', {'proyectos_clave': p_claves})


# /proyectos/ Pagina principal de PROYECTOS-----------------------------------------------------------------------------
# Metodo que contiene la informacion necesari para mostrar todos los proyectos en el treemap


def main_proyectos(request):
    p_claves = proyectos_clave()
    proyectos_periodo = ProyectoDeLeyProyectoley.objects.filter(periodo__id=ID_PERIODO).order_by('-fecha_radicacion')
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
        elif estado.id in range(32, 35) or estado.id == 70:
            data[temp]['Archivados'] += 1
            data_proyectos[temp]['Archivados'].append(json_proyecto)
        else:
            data[temp]['En debate'] += 1
            data_proyectos[temp]['En debate'].append(json_proyecto)

    return render(request, 'vv/main_proyectos.html',
                  {'proyectos_clave': p_claves, 'data': json.dumps(data), 'proyectos': json.dumps(data_proyectos)})


# /proyectos/#### Pagina detalle de un proyecto-------------------------------------------------------------------------


def detalle_proyecto(request, proyecto_id):
    p_claves = proyectos_clave()
    proyecto = ProyectoDeLeyProyectoley.objects.get(id=proyecto_id)
    estados = ProyectoDeLeyEstadodeproyectodeley.objects.filter(proyecto=proyecto).order_by('fecha')
    estados_cambio_debate = []
    print "-------------------------------------------------------------"
    fecha_anterior = ""
    votaciones = []
    votaciones_grafico = []
    str_votaciones = ""
    for estado in estados:
        print "nuemero de estados........................................"
        print str(len(estados)) + "estado: " + estado.estado.nombre
        votaciones_estado = []
        if estado.estado.id in range(16, 32) or estado.estado.id == 73:  # el ultimo es para los aprobados en 1 y 3 deb
            estados_cambio_debate.append(estado)
            if fecha_anterior != "":
                votaciones_estado = ProyectoDeLeyVotacion.objects.filter((Q(motivo__icontains="tránsito") |
                                                                          Q(motivo__icontains="título ")),
                                                                         proyecto_id=proyecto_id,
                                                                         tipo_votacion_id__lte=3,
                                                                         fecha__lte=estado.fecha,
                                                                         fecha__gt=fecha_anterior,
                                                                         ).order_by('fecha')
            else:
                votaciones_estado = ProyectoDeLeyVotacion.objects.filter((Q(motivo__icontains="tránsito") |
                                                                          Q(motivo__icontains="título ")),
                                                                         proyecto_id=proyecto_id,
                                                                         tipo_votacion_id__lte=3,
                                                                         fecha__lte=estado.fecha,
                                                                         ).order_by('fecha')
            votaciones.append(votaciones_estado)
            if len(votaciones_estado) > 0:
                ultima = votaciones_estado[len(votaciones_estado) - 1]
                votaciones_grafico.append(ultima)
                str_votaciones += str(ultima.id) + "-"
                # se toma la ultima para mostrar en el grafico
            else:
                votaciones_grafico.append(None)
                str_votaciones += "0-"
            fecha_anterior = estado.fecha

        elif estado.estado.id == 32:
            estados_cambio_debate.append(estado)
            if fecha_anterior != "":
                votaciones_estado = ProyectoDeLeyVotacion.objects.filter(proyecto_id=proyecto_id,
                                                                         tipo_votacion_id__lte=3,
                                                                         fecha__lte=estado.fecha,
                                                                         fecha__gt=fecha_anterior,
                                                                         ).order_by('fecha')
            else:
                votaciones_estado = ProyectoDeLeyVotacion.objects.filter(proyecto_id=proyecto_id,
                                                                         tipo_votacion_id__lte=3,
                                                                         fecha__lte=estado.fecha,
                                                                         ).order_by('fecha')
            votaciones.append(votaciones_estado)
            if len(votaciones_estado) > 0:
                ultima = votaciones_estado[len(votaciones_estado) - 1]
                votaciones_grafico.append(ultima)
                str_votaciones += str(ultima.id) + "-"
                # se toma la ultima para mostrar en el grafico
            else:
                votaciones_grafico.append(None)
                str_votaciones += "0-"
            fecha_anterior = estado.fecha

        print votaciones_estado
        print "nuemero de votaciones........................................"
        print len(votaciones)

    # Todas las votaciones tienen que estar en un dict que contenga como clave el id del estado

    json_votaciones_proyecto = {}
    e = 0  # indice para los estados
    for votacion in votaciones_grafico:
        json_votacion = []
        json_index = {}
        if votacion is not None:
            votos = ProyectoDeLeyVoto.objects.filter(votacion=votacion).select_related('congresista__partido_politico')
            for voto in votos:
                partido = voto.congresista.partido_politico
                if partido.id not in json_index:
                    json_index[partido.id] = len(json_votacion)
                    p = {
                        'name': partido.nombre,
                        'color': partido.get_color(),
                        'data': {'inasistencias': 0, 'abstenciones': 0, 'no': 0, 'si': 0},
                        'total_votos': 0,
                    }
                    json_votacion.append(p)
                if voto.voto == 0:  # abstenciones en la bd
                    json_votacion[json_index[partido.id]]['data']['abstenciones'] += 1
                elif voto.voto == 1:  # no en la bd
                    json_votacion[json_index[partido.id]]['data']['no'] += 1
                elif voto.voto == 2:  # si en la bd
                    json_votacion[json_index[partido.id]]['data']['si'] += 1
                elif voto.voto == 3:  # no asistio en la bd
                    json_votacion[json_index[partido.id]]['data']['inasistencias'] += 1
                json_votacion[json_index[partido.id]]['total_votos'] += 1
        # Si la votacion es None significa que fue aprobada por pupitrazo y se pone un dict vacio
        json_votaciones_proyecto[estados_cambio_debate[e].id] = json_votacion
        e += 1
    ids_estados = [str(e.id) for e in estados_cambio_debate]
    str_estados = '-'.join(ids_estados)
    return render(request, 'vv/detalle_proyecto.html', {'proyectos_clave': p_claves, 'proyecto': proyecto,
                                                        'votaciones_proyecto': json.dumps(json_votaciones_proyecto),
                                                        'str_votaciones': str_votaciones, 'str_estados': str_estados,
                                                        'estados': estados_cambio_debate, 'ids_estados': ids_estados})


# ajax para manejar el autocompletar y el buscar los votos de una persona o partido
def autocompletar(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        # Toma los 10 priemro partidos activos que tienen el item buscado
        partidos = CongresoPartido.objects.filter(nombre__icontains=q, estado_id=1)[:10]
        # Busca por el apellido que contenga el item y luego el nombre
        congresistas = CongresoCongresista.objects.filter((Q(persona_ptr__apellidos__icontains=q) |
                                                           Q(persona_ptr__nombres__icontains=q)),
                                                          es_congresista=True)[:10]

        results = []
        for partido in partidos:
            drug_json = {'value_id': partido.id, 'label': partido.nombre, 'value': partido.nombre}
            results.append(drug_json)
        for congresista in congresistas:
            nombre = congresista.persona_ptr.nombre_completo()
            drug_json = {'value_id': congresista.persona_ptr.id, 'label': nombre, 'value': nombre}
            results.append(drug_json)

        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


# ajax para retornar los votos que se van a ver en la tabla. El resultado al hacer enter en el autocompletar
def ver_votos(request):
    if request.is_ajax():
        # se toman los parametros del ajax
        q = request.GET.get('busqueda')
        estados = request.GET.get('ids_estados').split('-')
        votaciones = request.GET.get('ids_votaciones').split('-')[:-1]  # toma todos menos el ultimo que es vacio
        results = {}  # es un diccionario con los nombres de los estados por un lado y los votos por le otro
        try:  # se mira si es un partido
            partido = CongresoPartido.objects.get(nombre=q, estado_id=1)
            # Se sacan los votos del partido por los proyectos seleccionados
            json_congresistas = []
            json_index = {}  # indice de json_congresistas contiene el id y la posicion en el arreglo
            e = 0  # contador de estados
            str_estados = []
            for votacion in votaciones:
                if votacion != 0:
                    votos = ProyectoDeLeyVoto.objects.filter(votacion=votacion, congresista__partido_politico=partido)
                    estado = ProyectoDeLeyEstadodeproyectodeley.objects.get(id=estados[e])
                    str_estados.append(estado.estado.nombre)
                    for voto in votos:
                        congresista = voto.congresista
                        if congresista.persona_ptr.id not in json_index:
                            c = {
                                'nombre': congresista.persona_ptr.nombre_completo(),
                                'camara': 1 if congresista.es_senador else 0,
                                'votos': [-1] * len(estados)
                            }
                            json_index[congresista.persona_ptr.id] = len(json_congresistas)
                            json_congresistas.append(c)
                        json_congresistas[json_index[congresista.persona_ptr.id]]['votos'][e] = voto.voto
                e += 1
            results['estados'] = str_estados
            results['datos'] = json_congresistas
            results['tipo'] = 0  # le dice a la interfaz que es una repsuesta para un partido y no un congresista
        except CongresoPartido.DoesNotExist:  # si llega aca es que no es un partido ys e busca si es un congresista
            q = q.strip()
            qsplit = q.split(' ')
            nombres = u' '.join(qsplit[:1])
            apellidos = u' '.join(qsplit[-2:])
            try:  # se mira si es un congresista
                congresista = CongresoCongresista.objects.get(persona_ptr__nombres__icontains=nombres,
                                                              persona_ptr__apellidos__icontains=apellidos)
                # Se sacan los votos del congresista por los proyectos seleccionados
                json_congresista = {
                    'nombre': congresista.persona_ptr.nombre_completo(),
                    'camara': 'Senador(a)' if congresista.es_senador else 'Representante',
                    'partido': congresista.partido_politico.nombre,
                    'votos': [-1] * len(estados)
                }
                e = 0  # contador de estados
                str_estados = []
                for votacion in votaciones:
                    estado = ProyectoDeLeyEstadodeproyectodeley.objects.get(id=estados[e])
                    str_estados.append(estado.estado.nombre)
                    if votacion != 0:
                        try:
                            voto = ProyectoDeLeyVoto.objects.get(votacion=votacion, congresista=congresista)
                            json_congresista['votos'][e] = voto.voto
                        except ProyectoDeLeyVoto.DoesNotExist:
                            pass  # quiere decir que el congresista no participo de esta votacion
                    e += 1
                results['estados'] = str_estados
                results['datos'] = json_congresista
                results['tipo'] = 1  # le dice a la interfaz que es un congresista

            except CongresoCongresista.DoesNotExist:  # si llega aca no es ninguna de las dos
                results = 'No se encontró el término buscado'

        data = json.dumps(results)

    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


# SECCION CONGRESO
# /congreso/  Pagina principal de la seccion------------------------------------------------------------------
def congreso(request):
    p_claves = proyectos_clave()
    return render(request, 'vv/main_congreso.html', {'proyectos_clave': p_claves})


# /congreso/senado Pagina principal de senado --------------------------------------------------------------------
def senado(request):
    p_claves = proyectos_clave()
    # mandar info para llenar la grafica num_curules, name, color y un data vacio
    # nombre y foto de cada congresista y su partido
    index_partidos = {}
    json_partidos = []
    json_congresistas = {}
    senadores = CongresoCongresista.objects.filter(es_senador=True).select_related('partido_politico', 'persona_ptr')
    print ".-.-.-.-..-.-.-.-numero de partidos: " + str(len(senadores))
    for senador in senadores:
        partido = senador.partido_politico
        if partido.nombre not in index_partidos:  # se pone un nuevo partido si no se tenia ya en el index
            p = {
                'name': partido.nombre,
                'color': partido.get_color(),
                'num_curules': 0,
                'data': [],  # vacio, lo llena el js
                'id': partido.id,
            }
            index_partidos[partido.nombre] = len(json_partidos)
            json_partidos.append(p)
            json_congresistas[partido.nombre] = []

        c = {
            'nombre': senador.persona_ptr.nombre_completo(),
            'foto': MEDIA_URL + str(senador.persona_ptr.imagen),
            'id': senador.persona_ptr.id,
        }
        json_congresistas[partido.nombre].append(c)
        json_partidos[index_partidos[partido.nombre]]['num_curules'] += 1  # se le suma al partido un congresista
    json_partidos = sorted(json_partidos, key=itemgetter('num_curules'))

    return render(request, 'vv/senado.html', {'proyectos_clave': p_claves, 'partidos': json.dumps(json_partidos),
                                              'senado': json.dumps(json_congresistas)})


# /congreso/camara Pagina principal de la camara --------------------------------------------------------------------
def camara(request):
    p_claves = proyectos_clave()
    # mandar info para llenar la grafica num_curules, nombre_circun,
    # En cada region incluir un arreglo con dict de cada partido donde se contenga un arreglo con los congresistas
    json_circunscripciones = {}
    periodos = CongresoPeriodocongresista.objects.filter(periodo__id=ID_PERIODO, camara_id=2, tipo_periodo__id__lte=2,
                                                         congresista__es_representante_camara=True
                                                         ) \
        .select_related('partido', 'congresista__persona_ptr')
    print ".-.-.numero de represenatntes: " + str(len(periodos))
    for periodo in periodos:
        partido = periodo.partido
        representante = periodo.congresista.persona_ptr
        if periodo.circunscripcion_id not in json_circunscripciones:  # agrega la circunscripcion si no estaba
            cir = {
                'num_curules': 0,
                'data': {},
            }
            json_circunscripciones[periodo.circunscripcion_id] = cir
        es_reemplazo = ''
        if partido.nombre not in json_circunscripciones[periodo.circunscripcion_id]['data']:
            if periodo.tipo_periodo.id == 2:
                es_reemplazo = periodo.tipo_periodo.nombre
                print "reemplazo " + str(periodo.circunscripcion_id)
            p = {
                'nombre': partido.nombre,
                'color': partido.get_color(),
                'id': partido.id,
                'congresistas': [],
            }
            json_circunscripciones[periodo.circunscripcion_id]['data'][partido.nombre] = p

        c = {
            'nombre': representante.nombre_completo() + "\n" + es_reemplazo,
            'foto': MEDIA_URL + str(representante.imagen),
            'id': representante.id,
        }
        json_circunscripciones[periodo.circunscripcion_id]['data'][partido.nombre]['congresistas'].append(c)
        json_circunscripciones[periodo.circunscripcion_id]['num_curules'] += 1

    return render(request, 'vv/camara.html', {'proyectos_clave': p_claves,
                                              'camara': json.dumps(json_circunscripciones)})


# /partidos/#### Pagina prinicpal de un partido---------------------------------------------------------
def detalle_partido(request, partido_id):
    p_claves = proyectos_clave()
    partido = CongresoPartido.objects.get(id=partido_id)
    num_senadores = CongresoPeriodocongresista.objects.filter(periodo__id=ID_PERIODO, camara_id=1, tipo_periodo__id=1,
                                                              congresista__partido_politico=partido).count()
    num_representantes = CongresoPeriodocongresista.objects.filter(periodo__id=ID_PERIODO, camara_id=2,
                                                                   tipo_periodo__id=1,
                                                                   congresista__partido_politico=partido).count()
    print "-------------------"
    partido.logo = MEDIA_URL + partido.logo  # se pone la url completa de la imagen
    temas = GeneralTema.objects.all().order_by('nombre')
    return render(request, 'vv/detalle_partido.html', {'proyectos_clave': p_claves,
                                                       'partido': partido, 'num_senadores': num_senadores,
                                                       'num_representantes': num_representantes, 'temas': temas})


# ajax para retornar los votos del resumen de votos
def resumen_votos_partido(request):
    if request.is_ajax():
        # se toman los parametros del ajax
        tema_id = int(request.GET.get('tema_id'))
        partido_id = request.GET.get('partido_id')
        resumen_votos = {  # es un diccionario que de llave tiene cada una de las posibles iniciativas
            'tema': "Todos los temas",
            'total_votos': 0,
            'total_proyectos': 0,
            'partido': {'num_votos': 0, 'si': 0, 'no': 0, 'abstenciones': 0, 'inasistencias': 0},
            'gubernamental': {'num_votos': 0, 'si': 0, 'no': 0, 'abstenciones': 0, 'inasistencias': 0},
            'otros_partidos': {'num_votos': 0, 'si': 0, 'no': 0, 'abstenciones': 0, 'inasistencias': 0},
            'otras': {'num_votos': 0, 'si': 0, 'no': 0, 'abstenciones': 0, 'inasistencias': 0},
        }
        partido = CongresoPartido.objects.get(id=partido_id)
        ids_congresistas = CongresoPeriodocongresista.objects.filter(periodo__id=ID_PERIODO, partido=partido,
                                                                     congresista__es_congresista=True) \
            .order_by('id').values_list('congresista__persona_ptr_id', flat=True)

        # se toma la lista de proyectos buscada por el tema seleccionado
        if tema_id == -1:  # si se eligieron todos los temas
            ids_proyectos = ProyectoDeLeyProyectoley.objects.filter(periodo__id=ID_PERIODO).order_by('id') \
                .values_list('id', flat=True)

        else:  # busca por el tema especificado
            tema = GeneralTema.objects.get(id=tema_id)
            resumen_votos['tema'] = tema.nombre
            ids_proyectos = ProyectoDeLeyProyectoley.objects.filter(periodo__id=ID_PERIODO,
                                                                    tema_principal=tema).order_by('id') \
                .values_list('id', flat=True)
        print len(ids_proyectos)
        resumen_votos['total_proyectos'] = len(ids_proyectos)
        # me retorna los ids de los proyectos que hicieron estos congresistas
        ids_proyectos_autores_partido = ProyectoDeLeyAutorproyectoley.objects \
            .filter(proyecto_ley__id__in=ids_proyectos, autor_id__in=ids_congresistas) \
            .order_by('proyecto_ley__id').values_list('proyecto_ley__id', flat=True).distinct()
        # toma los ids de los proyectos que hicieron otros
        ids_proyectos_autores_otros = list(set(ids_proyectos) - set(ids_proyectos_autores_partido))
        print len(ids_proyectos_autores_partido)
        print len(ids_proyectos_autores_otros)
        gub = ProyectoDeLeyVoto.objects.filter((Q(votacion__motivo__icontains="tránsito") |
                                                Q(votacion__motivo__icontains="título ")),
                                               votacion__proyecto__id__in=ids_proyectos,
                                               votacion__tipo_votacion_id__lte=3,
                                               voto__in=(0, 1, 2, 3),
                                               votacion__proyecto__iniciativa__id=2,
                                               congresista__partido_politico=partido) \
            .values_list('voto').annotate(Count('voto'))
        gub = dict(gub)
        otr = ProyectoDeLeyVoto.objects.filter((Q(votacion__motivo__icontains="tránsito") |
                                                Q(votacion__motivo__icontains="título ")),
                                               votacion__proyecto__id__in=ids_proyectos,
                                               votacion__tipo_votacion_id__lte=3,
                                               voto__in=(0, 1, 2, 3),
                                               votacion__proyecto__iniciativa__id__gte=3,
                                               congresista__partido_politico=partido) \
            .values_list('voto').annotate(Count('voto'))
        otr = dict(otr)
        leg_par = ProyectoDeLeyVoto.objects.filter((Q(votacion__motivo__icontains="tránsito") |
                                                    Q(votacion__motivo__icontains="título ")),
                                                   votacion__proyecto__id__in=ids_proyectos_autores_partido,
                                                   votacion__tipo_votacion_id__lte=3,
                                                   voto__in=(0, 1, 2, 3),
                                                   votacion__proyecto__iniciativa__id=1,
                                                   congresista__partido_politico=partido) \
            .values_list('voto').annotate(Count('voto'))
        leg_par = dict(leg_par)
        leg_otr = ProyectoDeLeyVoto.objects.filter((Q(votacion__motivo__icontains="tránsito") |
                                                    Q(votacion__motivo__icontains="título ")),
                                                   votacion__proyecto__id__in=ids_proyectos_autores_otros,
                                                   votacion__tipo_votacion_id__lte=3,
                                                   voto__in=(0, 1, 2, 3),
                                                   votacion__proyecto__iniciativa__id=1,
                                                   congresista__partido_politico=partido) \
            .values_list('voto').annotate(Count('voto'))
        leg_otr = dict(leg_otr)
        # tipos de votos para hacer el for, estan ubicados en el orden en que aparecen en la bd
        tipos_voto = ['abstenciones', 'no', 'si', 'inasistencias']
        for i, tipo_voto in enumerate(tipos_voto):
            resumen_votos['gubernamental'][tipo_voto] = gub.get(i, 0)
            resumen_votos['gubernamental']['num_votos'] += gub.get(i, 0)
            resumen_votos['otras'][tipo_voto] = otr.get(i, 0)
            resumen_votos['otras']['num_votos'] += otr.get(i, 0)
            resumen_votos['partido'][tipo_voto] = leg_par.get(i, 0)
            resumen_votos['partido']['num_votos'] += leg_par.get(i, 0)
            resumen_votos['otros_partidos'][tipo_voto] = leg_otr.get(i, 0)
            resumen_votos['otros_partidos']['num_votos'] += leg_otr.get(i, 0)
            resumen_votos['total_votos'] += gub.get(i, 0) + otr.get(i, 0) + leg_par.get(i, 0) + leg_otr.get(i, 0)

        results = {
            'resumen_votos': resumen_votos,
        }
        data = json.dumps(results)
        print "////////////////////////////////////"

    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


# ajax para retornar las ultimas votaciones del partido
def ultimas_votaciones_partido(request):
    if request.is_ajax():
        # se toman los parametros del ajax
        tema_id = int(request.GET.get('tema_id'))
        partido_id = request.GET.get('partido_id')
        partido = CongresoPartido.objects.get(id=partido_id)
        proyectos_partido = []
        # se toma la lista de proyectos buscada por el tema seleccionado
        if tema_id == -1:  # si se eligieron todos los temas
            ids_proyectos = ProyectoDeLeyProyectoley.objects.filter(periodo__id=ID_PERIODO).order_by('id') \
                .values_list('id', flat=True)

        else:  # busca por el tema especificado
            tema = GeneralTema.objects.get(id=tema_id)
            ids_proyectos = ProyectoDeLeyProyectoley.objects.filter(periodo__id=ID_PERIODO,
                                                                    tema_principal=tema).order_by('id') \
                .values_list('id', flat=True)
        # para sacar los proyectos que van en la tabla (solo se toman 20 para no llenar de info al usuario )
        votaciones = ProyectoDeLeyVoto.objects.filter((Q(votacion__motivo__icontains="tránsito") |
                                                       Q(votacion__motivo__icontains="título ")),
                                                      votacion__proyecto__id__in=ids_proyectos,
                                                      votacion__tipo_votacion_id__lte=3,
                                                      congresista__partido_politico=partido) \
            .values_list('votacion__id', flat=True).distinct().order_by('-votacion__fecha')[:20]
        for votacion_id in votaciones:
            votacion = ProyectoDeLeyVotacion.objects.get(id=votacion_id)
            proyecto = votacion.proyecto
            sp = proyecto.titulo.split("[")
            nombre_corto = sp[len(sp) - 1][:-1]  # se toma el nombre corto cuando es posible
            if nombre_corto == "":
                nombre_corto = proyecto.titulo
            votos = ProyectoDeLeyVoto.objects.filter(votacion=votacion, congresista__partido_politico=partido,
                                                     voto__in=(0, 1, 2, 3)).values_list('voto').annotate(Count('voto'))
            votos = dict(votos)
            # solo lo guarda si hay al menos un voto
            if votos.get(0, 0) + votos.get(1, 0) + votos.get(2, 0) + votos.get(3, 0) > 0:
                p = {
                    'nombre': nombre_corto,
                    'id': proyecto.id,
                    'id_votacion': votacion.id,
                    'votos_totales': [votacion.votosabstencion, votacion.votoscontra,
                                      votacion.votosfavor, votacion.numero_no_asistencias],
                    'votos_partido': [votos.get(0, 0), votos.get(1, 0), votos.get(2, 0), votos.get(3, 0)],
                }
                proyectos_partido.append(p)

        results = {
            'ultimas_votaciones': proyectos_partido,
        }
        data = json.dumps(results)
        print "////////////////////////////////////"

    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


# ajax para retornar la disciplina del partido y de los demas
def disciplina_partido(request):
    if request.is_ajax():
        # se toman los parametros del ajax
        tema_id = int(request.GET.get('tema_id'))
        partido_id = request.GET.get('partido_id')
        # se toma la lista de proyectos buscada por el tema seleccionado
        if tema_id == -1:  # si se eligieron todos los temas
            ids_proyectos = ProyectoDeLeyProyectoley.objects.filter(periodo__id=ID_PERIODO).order_by('id') \
                .values_list('id', flat=True)

        else:  # busca por el tema especificado
            tema = GeneralTema.objects.get(id=tema_id)
            ids_proyectos = ProyectoDeLeyProyectoley.objects.filter(periodo__id=ID_PERIODO,
                                                                    tema_principal=tema).order_by('id') \
                .values_list('id', flat=True)

        legislaturas = ProyectoDeLeyLegislatura.objects.filter(cuatrienio__id=ID_PERIODO,
                                                               fecha_inicio__lte=datetime.now().date()).order_by(
            'fecha_inicio').values()
        anio_inicio = legislaturas[0]['fecha_inicio'].year
        disciplina_rice = {}
        for leg in legislaturas:
            disc = ProyectoDeLeyVoto.objects.filter((Q(votacion__motivo__icontains="tránsito") |
                                                     Q(votacion__motivo__icontains="título ")),
                                                    votacion__proyecto__id__in=ids_proyectos,
                                                    votacion__tipo_votacion_id__lte=3,
                                                    votacion__fecha__range=(leg['fecha_inicio'], leg['fecha_fin']),
                                                    voto__in=(0, 1, 2, 3)) \
                .values('congresista__partido_politico__id', 'congresista__partido_politico__nombre') \
                .annotate(total=Count('voto'),
                          si=Count(Case(When(voto=2, then=1), output_field=IntegerField())),
                          no=Count(Case(When(voto=1, then=1), output_field=IntegerField())))
            for p in disc:  # para poenrle un nombre elegante a los campos del dict
                nombre_partido = p['congresista__partido_politico__nombre']
                if nombre_partido not in disciplina_rice:
                    disciplina_rice[nombre_partido] = {
                        'id': p['congresista__partido_politico__id'],
                        'nombre': nombre_partido,
                        'color': CongresoPartido.COLORES[nombre_partido],
                        'seleccionado': False,
                    }
                    if disciplina_rice[nombre_partido]['id'] == int(partido_id):
                        disciplina_rice[nombre_partido]['seleccionado'] = True
                disciplina_rice[nombre_partido][str(anio_inicio) + ' - ' + str(anio_inicio + 1)] = {
                    'si': p['si'],
                    'no': p['no'],
                    'total': p['total'],
                    'disciplina': float("%.2f" % abs(p['si'] / p['total'] - p['no'] / p['total'])),
                }
            anio_inicio += 1
        print "-=-=-=-==-=-=-=-=-=-=-=-=-=-="
        print disciplina_rice
        anios = [str(l['fecha_inicio'].year)+" - "+str(l['fecha_fin'].year) for l in legislaturas]
        results = {
            'disciplina_rice': disciplina_rice,
            'anios': anios
        }
        data = json.dumps(results)
        print "////////////////////////////////////"

    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
