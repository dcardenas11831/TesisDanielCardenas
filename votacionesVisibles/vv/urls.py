from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # SECCION PROYECTOS DE LEY
    url(r'^proyectos/$', views.main_proyectos, name='proyectos'),
    url(r'^proyectos/(?P<proyecto_id>[0-9]+)/$', views.detalle_proyecto, name='proyecto'),
    url(r'^busqueda/autocompletar/', views.autocompletar, name='autocompletar'),
    url(r'^busqueda/ver_votos/', views.ver_votos, name='ver_votos'),

    # SECCION CONGRESO
    url(r'^congreso/$', views.congreso, name='congreso'),
    url(r'^congreso/senado/$', views.senado, name='senado'),
    url(r'^congreso/camara/$', views.camara, name='camara'),
    url(r'^partidos/(?P<partido_id>[0-9]+)/$', views.detalle_partido, name='partido'),
    url(r'^busqueda/resumen_votos_partido/', views.resumen_votos_partido, name='resumen_votos_partido'),
    url(r'^busqueda/ultimas_votaciones_partido/', views.ultimas_votaciones_partido, name='ultimas_votaciones_partido'),
    url(r'^busqueda/disciplina_partido/', views.disciplina_partido, name='disciplina_partido'),
    url(r'^congresista/(?P<congresista_id>[0-9]+)/$', views.detalle_congresista, name='congresista'),
    url(r'^busqueda/resumen_votos_congresista/', views.resumen_votos_congresista, name='resumen_votos_congresista'),
    url(r'^busqueda/ultimas_votaciones_congresista/', views.ultimas_votaciones_congresista,
        name='ultimas_votaciones_congresista'),
    url(r'^busqueda/disciplina_congresista/', views.disciplina_congresista, name='disciplina_congresista'),
]
