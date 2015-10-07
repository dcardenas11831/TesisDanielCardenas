# -*- coding: utf-8 -*-
from django.shortcuts import render
import json

# Metodo para controlar la pagina home


def index(request):
    return render(request, 'vv/base.html')


def main_proyectos(request):
    data = {
            "Agropecuario y agrícola":{
                "Sancionados": "1",
                "En debate": "1",
                "Archivados": "0",
            },
            "Bienestar y pobreza":{
                "Sancionados": "0",
                "En debate": "3",
                "Archivados": "2",
            },
            "Celebraciones, honores y monumentos":{
                "Sancionados": "0",
                "En debate": "1",
                "Archivados": "0",
            },
            "Comunicaciones, medios y tecnologías de la información":{
                "Sancionados": "2",
                "En debate": "0",
                "Archivados": "0",
            },
            "Conflicto armado":{
                "Sancionados": "4",
                "En debate": "7",
                "Archivados": "3",
            },
            "Economía":{
                "Sancionados": "2",
                "En debate": "5",
                "Archivados": "1",
            },
            "Educación, cultura, ciencia y tecnología":{
                "Sancionados": "1",
                "En debate": "7",
                "Archivados": "1",
            },
            "Impuestos":{
                "Sancionados": "1",
                "En debate": "12",
                "Archivados": "5",
            },
            "Infraestructura":{
                "Sancionados": "0",
                "En debate": "9",
                "Archivados": "0",
            },
            "Justicia":{
                "Sancionados": "1",
                "En debate": "5",
                "Archivados": "3",
            },
            "Laboral":{
                "Sancionados": "3",
                "En debate": "0",
                "Archivados": "0",
            },
            "Medio Ambiente":{
                "Sancionados": "1",
                "En debate": "1",
                "Archivados": "0",
            },
            "Minas y energía":{
                "Sancionados": "0",
                "En debate": "1",
                "Archivados": "2",
            },
            "Organismos de Control y Ministerio público":{
                "Sancionados": "0",
                "En debate": "3",
                "Archivados": "2",
            },
            "Organización Electoral":{
                "Sancionados": "3",
                "En debate": "0",
                "Archivados": "0",
            },
            "Participación ciudadana":{
                "Sancionados": "2",
                "En debate": "2",
                "Archivados": "0",
            },
            "Política Internacional":{
                "Sancionados": "1",
                "En debate": "7",
                "Archivados": "1",
            },
            "Presupuesto":{
                "Sancionados": "4",
                "En debate": "1",
                "Archivados": "0",
            },
            "Profesiones":{
                "Sancionados": "0",
                "En debate": "2",
                "Archivados": "0",
            },
            "Rama Ejecutiva":{
                "Sancionados": "16",
                "En debate": "14",
                "Archivados": "26",
            },
            "Rama Judicial":{
                "Sancionados": "4",
                "En debate": "1",
                "Archivados": "1",
            },
            "Rama Legislativa":{
                "Sancionados": "3",
                "En debate": "0",
                "Archivados": "0",
            },
            "Recreación y deporte":{
                "Sancionados": "0",
                "En debate": "1",
                "Archivados": "0",
            },
            "Seguridad Social y salud":{
                "Sancionados": "3",
                "En debate": "5",
                "Archivados": "2",
            },
            "Seguridad, defensa y fuerza pública":{
                "Sancionados": "7",
                "En debate": "6",
                "Archivados": "3",
            },
            "Servicios Públicos": {
                "Sancionados": "1",
                "En debate": "1",
                "Archivados": "0",
            },
            "Tránsito y transporte": {
                "Sancionados": "0",
                "En debate": "3",
                "Archivados": "0",
            },
            "Vivienda": {
                "Sancionados": "1",
                "En debate": "1",
                "Archivados": "0",
            }

        }
    return render(request, 'vv/main_proyectos.html', {'data': json.dumps(data)})
