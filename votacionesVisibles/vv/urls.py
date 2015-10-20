from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^proyectos/$', views.main_proyectos, name='proyectos'),
    url(r'^proyectos/(?P<proyecto_id>[0-9]+)/$', views.detalle_proyecto, name='proyecto'),

]
