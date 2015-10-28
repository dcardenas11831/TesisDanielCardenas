# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class ActividadActividad(models.Model):
    seguido_por = models.ForeignKey('ActividadSiguea', models.DO_NOTHING)
    fecha_hora = models.DateTimeField()
    tipo = models.ForeignKey('ActividadTipoactividad', models.DO_NOTHING)
    objeto_disparador_id = models.IntegerField(blank=True, null=True)
    objeto_seguido_id = models.IntegerField(blank=True, null=True)
    objeto_seguido_content_type_id = models.IntegerField(blank=True, null=True)
    objeto_disparador_content_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividad_actividad'


class ActividadSiguea(models.Model):
    seguido_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    seguido_id = models.IntegerField()
    seguidor = models.ForeignKey('CongresoPersona', models.DO_NOTHING)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividad_siguea'


class ActividadTipoactividad(models.Model):
    nombre = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'actividad_tipoactividad'


'''
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = ['group_id', 'permission_id']


class AuthMessage(models.Model):
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'auth_message'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = ['content_type_id', 'codename']


class AuthUser(models.Model):
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = ['user_id', 'group_id']


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = ['user_id', 'permission_id']
'''


class AyudaAyudaseccion(models.Model):
    orden = models.IntegerField()
    fecha_actualizacion = models.DateField()
    id_video_ayuda = models.CharField(max_length=70)
    regex_seccion = models.CharField(unique=True, max_length=70)
    exacto = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ayuda_ayudaseccion'


class AyudaEnlaceinteres(models.Model):
    titulo = models.CharField(max_length=150)
    enlace = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=240, blank=True, null=True)
    seccion = models.ForeignKey('AyudaEnlacesseccion', models.DO_NOTHING)
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ayuda_enlaceinteres'


class AyudaEnlacesseccion(models.Model):
    orden = models.IntegerField()
    regex_seccion = models.CharField(unique=True, max_length=70)

    class Meta:
        managed = False
        db_table = 'ayuda_enlacesseccion'


class AyudaPreguntarespuesta(models.Model):
    orden = models.IntegerField()
    pregunta = models.TextField()
    respuesta = models.TextField()
    seccion = models.ForeignKey(AyudaAyudaseccion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ayuda_preguntarespuesta'


'''
class BlogBlog(models.Model):
    autor = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    tipo_blog = models.ForeignKey('BlogTipoblog', models.DO_NOTHING)
    destacado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'blog_blog'


class BlogBoletin(models.Model):
    orden = models.IntegerField()
    nombre = models.CharField(max_length=50)
    anio = models.IntegerField()
    objeto = models.TextField()
    destacar = models.BooleanField()
    archivo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_boletin'


class BlogPost(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    blog = models.ForeignKey(BlogBlog, models.DO_NOTHING)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    esta_publicado = models.BooleanField()
    esta_vetado = models.BooleanField()
    destacado = models.BooleanField()
    imagen = models.CharField(max_length=100, blank=True, null=True)
    imagen_menu = models.CharField(max_length=100, blank=True, null=True)
    imagen_menu_seleccionada = models.CharField(max_length=100, blank=True, null=True)
    ee = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'blog_post'


class BlogPostTags(models.Model):
    post = models.ForeignKey(BlogPost, models.DO_NOTHING)
    tag = models.ForeignKey('BlogTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post_tags'
        unique_together = ['post_id', 'tag_id']


class BlogTag(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'blog_tag'


class BlogTipoblog(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'blog_tipoblog'
'''


class CeleryPeriodictaskmeta(models.Model):
    name = models.CharField(unique=True, max_length=255)
    last_run_at = models.DateTimeField()
    total_run_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'celery_periodictaskmeta'


class CeleryTaskmeta(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celery_taskmeta'


class CeleryTasksetmeta(models.Model):
    taskset_id = models.CharField(unique=True, max_length=255)
    result = models.TextField()
    date_done = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'celery_tasksetmeta'


class CongresoActividadpersona(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    fecha_hora = models.DateTimeField()
    persona = models.ForeignKey('CongresoPersona', models.DO_NOTHING)
    tipo = models.ForeignKey('CongresoTipoactividad', models.DO_NOTHING)
    texto = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    object_id = models.IntegerField()
    periodo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_actividadpersona'


class CongresoAlianza(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    congresista_alianza = models.ForeignKey('CongresoCongresista', related_name='congresista_alianza_uno')
    congresista_alianza2 = models.ForeignKey('CongresoCongresista', related_name='congresista_alianza_dos')
    periodo_id = models.IntegerField(blank=True, null=True)
    partido = models.ForeignKey('CongresoPartido', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_alianza'


class CongresoAlianzapartido(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    tiempo = models.BooleanField()
    partido_origen = models.ForeignKey('CongresoPartido', related_name='partido_origen')
    partido_aliado = models.ForeignKey('CongresoPartido', related_name='partido_aliado')

    class Meta:
        managed = False
        db_table = 'congreso_alianzapartido'


class CongresoAval(models.Model):
    nombre = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'congreso_aval'


class CongresoBancada(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=50)
    posicion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'congreso_bancada'


class CongresoCamara(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'congreso_camara'


class CongresoCampania(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    congresista = models.ForeignKey('CongresoCongresista', related_name='campanias')
    partido = models.ForeignKey('CongresoPartido', models.DO_NOTHING)
    aspira = models.IntegerField()
    departamento = models.ForeignKey('GeneralDepartamento', models.DO_NOTHING, blank=True, null=True)
    sitio_web = models.CharField(max_length=200, blank=True, null=True)
    correo = models.CharField(max_length=75, blank=True, null=True)
    propuestas = models.TextField(blank=True, null=True)
    costo_total = models.IntegerField(blank=True, null=True)
    circunscripcion = models.IntegerField(blank=True, null=True)
    tipo_voto = models.IntegerField(blank=True, null=True)
    formula = models.ForeignKey('CongresoCongresista', related_name='formula', blank=True, null=True)
    contacto = models.ForeignKey('CongresoPersona', models.DO_NOTHING, blank=True, null=True)
    camara_id = models.IntegerField(blank=True, null=True)
    periodo = models.ForeignKey('CongresoPeriodo', null=True)
    inversion_dinero = models.CharField(max_length=40, blank=True, null=True)
    financiacion_recursos_propios = models.CharField(max_length=20, blank=True, null=True)
    financiacion_prestamos = models.CharField(max_length=20, blank=True, null=True)
    financiacion_donaciones = models.CharField(max_length=20, blank=True, null=True)
    financiacion_empresa_privada = models.CharField(max_length=20, blank=True, null=True)
    fuente_financiacion_personas = models.CharField(max_length=20, blank=True, null=True)
    circunscripcion_model = models.ForeignKey('CongresoCircunscripcion', models.DO_NOTHING, blank=True, null=True)
    numero_lista = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_campania'
        unique_together = ['congresista', 'periodo']


class CongresoCampaniaSectores(models.Model):
    campania = models.ForeignKey('CongresoCampania', models.DO_NOTHING)
    sectorindustria = models.ForeignKey('GeneralSectorindustria', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_campania_sectores'
        unique_together = ['campania', 'sectorindustria']


class CongresoCandidatosConcejo(models.Model):
    nombre_completo = models.CharField(max_length=150)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    genero = models.CharField(max_length=1)
    telefono_candidato = models.CharField(max_length=50, blank=True, null=True)
    email_candidato = models.CharField(max_length=75, blank=True, null=True)
    sitio_web = models.CharField(max_length=200, blank=True, null=True)
    facebook_candidato = models.CharField(max_length=260, blank=True, null=True)
    twitter_candidato = models.CharField(max_length=260, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    partido = models.ForeignKey('CongresoPartido', models.DO_NOTHING)
    propuestas = models.TextField(blank=True, null=True)
    tipo_voto = models.IntegerField(blank=True, null=True)
    imagen_concejo = models.CharField(max_length=100, blank=True, null=True)
    por_que_votar = models.TextField(blank=True, null=True)
    numero_lista = models.IntegerField(blank=True, null=True)
    actualmente_concejal = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'congreso_candidatos_concejo'


class CongresoCargo(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    persona = models.ForeignKey('CongresoPersona', models.DO_NOTHING)
    sector = models.ForeignKey('GeneralSectorindustria', models.DO_NOTHING, blank=True, null=True)
    cargo = models.CharField(max_length=140, blank=True, null=True)
    entidad = models.CharField(max_length=140, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_cargo'


class CongresoCargocamara(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'congreso_cargocamara'


class CongresoCargocomision(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'congreso_cargocomision'


class CongresoCargopolitico(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    persona = models.ForeignKey('CongresoPersona', models.DO_NOTHING)
    cargo = models.CharField(max_length=140)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    partido = models.ForeignKey('CongresoPartido', models.DO_NOTHING, blank=True, null=True)
    resultado = models.CharField(max_length=1)
    camara = models.ForeignKey(CongresoCamara, models.DO_NOTHING, blank=True, null=True)
    comision = models.ForeignKey('CongresoComision', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_cargopolitico'


class CongresoCircunscripcion(models.Model):
    nombre = models.CharField(max_length=140)
    departamento = models.ForeignKey('GeneralDepartamento', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_circunscripcion'


class CongresoComision(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=50)
    camara = models.ForeignKey(CongresoCamara, models.DO_NOTHING, blank=True, null=True)
    permanente = models.BooleanField()
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.CharField(max_length=100, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    tipo_comision = models.ForeignKey('CongresoTipocomision', models.DO_NOTHING)
    correo = models.CharField(max_length=75, blank=True, null=True)
    oficina = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_comision'


class CongresoCongresista(models.Model):
    persona_ptr = models.OneToOneField('CongresoPersona', models.DO_NOTHING, primary_key=True)
    partido_politico = models.ForeignKey('CongresoPartido', related_name='partido_congresista')
    es_candidato = models.BooleanField()
    orgullo = models.TextField(blank=True, null=True)
    se_identifica = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    ha_reemplazado = models.BooleanField()
    es_activo = models.BooleanField()
    cantidad_actividades = models.IntegerField()
    cantidad_comentarios = models.IntegerField()
    comision_actual_id = models.IntegerField(blank=True, null=True)
    periodo_actual_id = models.IntegerField(blank=True, null=True)
    es_congresista = models.NullBooleanField()
    ha_sido_congresista = models.NullBooleanField()
    numero_votos_partido = models.IntegerField(blank=True, null=True)
    vota_con_partido = models.FloatField(blank=True, null=True)
    old_id = models.IntegerField(blank=True, null=True)
    investigado = models.CharField(max_length=150, blank=True, null=True)
    slug = models.CharField(max_length=250, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    campania_actual_id = models.IntegerField(blank=True, null=True)
    actividad_actual_id = models.IntegerField(blank=True, null=True)
    numero_oficina = models.CharField(max_length=100, blank=True, null=True)
    telefono_oficina = models.CharField(max_length=100, blank=True, null=True)
    ha_sido_reemplazo = models.NullBooleanField()
    tiene_formula_electoral_aspirante_a_la_otra_camara = models.NullBooleanField()
    formula_electoral = models.CharField(max_length=50, blank=True, null=True)
    partido_formula_electoral = models.ForeignKey('CongresoPartido', related_name='partido_formula', blank=True,
                                                  null=True)
    ha_estado_en_bancada_diferente = models.NullBooleanField()
    ha_ejercido_cargo_diferente = models.NullBooleanField()
    cargo_popular = models.CharField(max_length=20, blank=True, null=True)
    ha_ejercido_cargo_en_rama_ejecutiva = models.NullBooleanField()
    ha_sido_dirigente_sindical = models.NullBooleanField()
    ha_sido_dirigente_gremial = models.NullBooleanField()
    tiene_pariente_en_la_politica = models.NullBooleanField()
    es_representante_camara = models.NullBooleanField()
    es_candidato_camara = models.NullBooleanField()
    es_senador = models.NullBooleanField()
    es_candidato_senador = models.NullBooleanField()
    cargo_ejecutivo = models.CharField(max_length=20, blank=True, null=True)
    pariente_politica = models.CharField(max_length=40, blank=True, null=True)
    ha_tenido_pariente_en_la_politica = models.NullBooleanField()
    pariente_politica_inactivo = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_congresista'


class CongresoCongresistadebancada(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    congresista = models.ForeignKey(CongresoCongresista, models.DO_NOTHING)
    bancada = models.ForeignKey(CongresoBancada, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_congresistadebancada'


class CongresoCongresistadepartido(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    congresista = models.ForeignKey(CongresoCongresista, models.DO_NOTHING)
    partido = models.ForeignKey('CongresoPartido', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_congresistadepartido'


class CongresoContadorcongresistas(models.Model):
    congresistas = models.IntegerField()
    candidatos = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    object_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'congreso_contadorcongresistas'


class CongresoEntidad(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'congreso_entidad'


class CongresoEstadopartido(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=150)
    es_activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'congreso_estadopartido'


class CongresoFinanciador(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    porcentaje = models.IntegerField()
    campania = models.ForeignKey(CongresoCampania, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_financiador'


class CongresoIntegrantecamara(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    cargo = models.ForeignKey(CongresoCargocamara, models.DO_NOTHING, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    congresista = models.ForeignKey(CongresoCongresista, models.DO_NOTHING)
    camara = models.ForeignKey(CongresoCamara, models.DO_NOTHING)
    periodo = models.ForeignKey('CongresoPeriodo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_integrantecamara'


class CongresoIntegrantecomision(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    cargo = models.ForeignKey(CongresoCargocomision, models.DO_NOTHING, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    congresista = models.ForeignKey(CongresoCongresista, models.DO_NOTHING)
    comision = models.ForeignKey(CongresoComision, models.DO_NOTHING)
    periodo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_integrantecomision'


class CongresoLink(models.Model):
    link = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_link'


class CongresoPartido(models.Model):
    COLORES = {
        'Alianza Social Independiente': "#CD6428",
        'Alianza Verde': "#339900",
        'Autoridades Indígenas de Colombia AICO': "#474900",
        'Bancada Afrocolombiana ': "#0F0000",
        'Bancada Indígena': "#554B0F",
        'Cambio Radical': "#FF3366",
        'Centro Democrático': "#00CCFF",
        'Conservador Colombiano': "#000099",
        'Fundación Ébano de Colombia Funeco': "#FF00FF",
        'Liberal Colombiano': "#CC0000",
        'MIRA': "#000019",
        'Movimiento Alternativo Indígena y Social - MAIS': "#FF0000",
        'Movimiento de Integración Regional - MIR': "#373737",
        'Movimiento Político Cien por Ciento por Colombia': "#6A2952",
        'Opción Ciudadana': "#CD9500",
        'Partido Social de Unidad Nacional - Partido de la U': "#FF6600",
        'Polo Democrático Alternativo': "#FFCC00",
        'Por un Huila Mejor': "#AB2B00",
    }

    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=100)
    fecha_fundacion = models.DateField(blank=True, null=True)
    lugar_creacion = models.CharField(max_length=100, blank=True, null=True)
    direccion_sede_principal = models.CharField(max_length=100, blank=True, null=True)
    sitio_web = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    estatutos = models.CharField(max_length=200, blank=True, null=True)
    lineamientos = models.TextField(blank=True, null=True)
    resenia_historica = models.TextField(blank=True, null=True)
    propuestas = models.TextField(blank=True, null=True)
    director = models.ForeignKey('CongresoPersona', related_name='director', blank=True, null=True)
    secretario = models.ForeignKey('CongresoPersona', related_name='secretario', blank=True, null=True)
    representante_legal = models.ForeignKey('CongresoPersona', related_name='representante_legal', blank=True,
                                            null=True)
    fundador = models.CharField(max_length=140, blank=True, null=True)
    posicion_ideologica = models.IntegerField(blank=True, null=True)
    sistema_avales = models.IntegerField(blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    rango_edad_id = models.IntegerField(blank=True, null=True)
    telefono_contacto = models.CharField(max_length=150, blank=True, null=True)
    celular_contacto = models.CharField(max_length=150, blank=True, null=True)
    correo_contacto = models.CharField(max_length=75, blank=True, null=True)
    direccion_contacto = models.CharField(max_length=150, blank=True, null=True)
    estado_id = models.IntegerField(blank=True, null=True)
    nombre_contacto = models.CharField(max_length=150, blank=True, null=True)
    old_id = models.IntegerField(blank=True, null=True)
    usuario = models.ForeignKey('CongresoPersona', related_name='usuario', blank=True, null=True)
    feed_rss = models.CharField(max_length=200, blank=True, null=True)
    datos_clave = models.TextField(blank=True, null=True)
    es_bancada = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'congreso_partido'

    def get_color(self):
        return self.COLORES[self.nombre]


class CongresoPartidoAvales(models.Model):
    partido = models.ForeignKey('CongresoPartido', models.DO_NOTHING)
    aval = models.ForeignKey('CongresoAval', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_partido_avales'
        unique_together = ['partido', 'aval']


class CongresoPartidoSectores(models.Model):
    partido = models.ForeignKey('CongresoPartido', models.DO_NOTHING)
    sectorindustria = models.ForeignKey('GeneralSectorindustria', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_partido_sectores'
        unique_together = ['partido', 'sectorindustria']


class CongresoPeriodo(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    old_id = models.IntegerField(blank=True, null=True)
    activo = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'congreso_periodo'


class CongresoPeriodocongresista(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    tipo_periodo = models.ForeignKey('CongresoTipoperiodo', models.DO_NOTHING)
    periodo = models.ForeignKey(CongresoPeriodo, models.DO_NOTHING)
    partido = models.ForeignKey(CongresoPartido, models.DO_NOTHING)
    congresista = models.ForeignKey(CongresoCongresista, models.DO_NOTHING)
    camara_id = models.IntegerField(blank=True, null=True)
    depto_mayor_votacion_id = models.IntegerField(blank=True, null=True)
    numero_lista = models.IntegerField(blank=True, null=True)
    numero_votos = models.IntegerField(blank=True, null=True)
    circunscripcion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_periodocongresista'


class CongresoPersona(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    # user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    facebook_id = models.CharField(max_length=100, blank=True, null=True)
    activation_key = models.CharField(max_length=40)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sitio_web = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    lugar_cedula = models.ForeignKey('GeneralMunicipio', related_name='cedula_lugar', blank=True, null=True)
    imagen = models.CharField(max_length=100, blank=True, null=True)
    anio_nacimiento = models.DateField(blank=True, null=True)
    departamento_nacimiento = models.ForeignKey('GeneralDepartamento', related_name='departamento_nacimiento',
                                                blank=True, null=True)
    municipio_nacimiento = models.ForeignKey('GeneralMunicipio', related_name='municipio_nacimiento', blank=True,
                                             null=True)
    nivel_educativo = models.CharField(max_length=50, blank=True, null=True)
    rango_edad = models.ForeignKey('GeneralRangoedad', models.DO_NOTHING, blank=True, null=True)
    profesion = models.ForeignKey('GeneralProfesion', models.DO_NOTHING, blank=True, null=True)
    genero = models.ForeignKey('GeneralGenero', models.DO_NOTHING, blank=True, null=True)
    fecha_fallecimiento = models.DateField(blank=True, null=True)
    flickr_user = models.CharField(max_length=260, blank=True, null=True)
    youtube_user = models.CharField(max_length=260, blank=True, null=True)
    tumblr_user = models.CharField(max_length=260, blank=True, null=True)
    twitter_user = models.CharField(max_length=260, blank=True, null=True)
    linkedin_user = models.CharField(max_length=260, blank=True, null=True)
    blogspot_user = models.CharField(max_length=260, blank=True, null=True)
    posicion_ideologica = models.IntegerField(blank=True, null=True)
    region_nacimiento = models.ForeignKey('GeneralRegion', related_name='region_nacimiento', blank=True, null=True)
    facebook_user = models.CharField(max_length=260, blank=True, null=True)
    mini_bio = models.TextField(blank=True, null=True)
    estrato = models.CharField(max_length=2, blank=True, null=True)
    idrac = models.CharField(max_length=15, blank=True, null=True)
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    religion = models.CharField(max_length=30, blank=True, null=True)
    frecuencia_actos_religiosos = models.CharField(max_length=20, blank=True, null=True)

    def nombre_completo(self):
        return u'%s %s' % (self.nombres.strip(), self.apellidos.strip())

    class Meta:
        managed = False
        db_table = 'congreso_persona'


class CongresoPosicion(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    congresista = models.ForeignKey(CongresoPersona, models.DO_NOTHING)
    a_favor = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_posicion'


class CongresoPosicionpartido(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    partido = models.ForeignKey(CongresoPartido, models.DO_NOTHING)
    a_favor = models.IntegerField()
    tema_opinion = models.ForeignKey('CongresoTemaopinion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_posicionpartido'


class CongresoPosicionproposicion(models.Model):
    posicion_ptr = models.OneToOneField('CongresoPosicion', models.DO_NOTHING, primary_key=True)
    proposicion = models.ForeignKey('CongresoProposicion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_posicionproposicion'


class CongresoPosiciontemaopinion(models.Model):
    posicion_ptr = models.OneToOneField('CongresoPosicion', models.DO_NOTHING, primary_key=True)
    tema = models.ForeignKey('CongresoTemaopinion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_posiciontemaopinion'


class CongresoProblema(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    tipo_problema = models.ForeignKey('CongresoTipoproblema', models.DO_NOTHING)
    descripcion = models.TextField()
    congresista = models.ForeignKey(CongresoCongresista, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_problema'


class CongresoProblemaLink(models.Model):
    problema = models.ForeignKey('CongresoProblema', models.DO_NOTHING)
    link = models.ForeignKey('CongresoLink', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_problema_link'
        unique_together = ['problema', 'link']


class CongresoProposicion(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'congreso_proposicion'


class CongresoReemplazo(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    congresista_reemplaza = models.ForeignKey(CongresoCongresista, related_name='congresista_al_que_reemplaza')
    congresista_reemplado_por = models.ForeignKey(CongresoCongresista, related_name='congresista_que_reemplazo')
    periodo_inicial = models.DateField()
    periodo_final = models.DateField()
    partido = models.ForeignKey(CongresoPartido, models.DO_NOTHING, blank=True, null=True)
    camara = models.ForeignKey(CongresoCamara, models.DO_NOTHING, blank=True, null=True)
    comision = models.ForeignKey(CongresoComision, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_reemplazo'


class CongresoSecretario(models.Model):
    persona_ptr = models.OneToOneField('CongresoPersona', models.DO_NOTHING, primary_key=True)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    comision = models.ForeignKey(CongresoComision, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'congreso_secretario'


class CongresoTemaopinion(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField()
    obtenido_votacion = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'congreso_temaopinion'


class CongresoTipoactividad(models.Model):
    nombre = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'congreso_tipoactividad'


class CongresoTipocomision(models.Model):
    nombre = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'congreso_tipocomision'


class CongresoTipoperiodo(models.Model):
    nombre = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'congreso_tipoperiodo'


class CongresoTipoproblema(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'congreso_tipoproblema'


class CongresoTrayectoria(models.Model):
    id_candidato_concejo = models.ForeignKey(CongresoCandidatosConcejo, models.DO_NOTHING)
    trayectoria_anio = models.IntegerField()
    cargo = models.CharField(max_length=100, blank=True, null=True)
    partido = models.CharField(max_length=100, blank=True, null=True)
    votos = models.CharField(max_length=100, blank=True, null=True)
    es_electo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congreso_trayectoria'


class CorteSentencia(models.Model):
    proyecto = models.ForeignKey('ProyectoDeLeyProyectoley', models.DO_NOTHING, blank=True, null=True)
    anio = models.CharField(max_length=4)
    cod_sentencia = models.CharField(max_length=20)
    num_sentencia = models.CharField(max_length=20)
    tipo_caso = models.ForeignKey('CorteTipocaso', models.DO_NOTHING)
    id_norma = models.TextField()
    titulo_norma = models.TextField()
    mas_normas = models.BooleanField()
    otras_normas = models.TextField()
    numero_camara = models.CharField(max_length=100)
    numero_senado = models.CharField(max_length=100)
    tipo_demanda = models.ForeignKey('CorteTipodemanda', models.DO_NOTHING)
    oficio = models.BooleanField()
    fecha_norma = models.DateField()

    class Meta:
        managed = False
        db_table = 'corte_sentencia'


class CorteTipocaso(models.Model):
    descripcion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'corte_tipocaso'


class CorteTipodemanda(models.Model):
    descripcion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'corte_tipodemanda'


class DbsettingsSetting(models.Model):
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    module_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    attribute_name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dbsettings_setting'


'''
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCommentFlags(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    comment = models.ForeignKey('DjangoComments', models.DO_NOTHING)
    flag = models.CharField(max_length=30)
    flag_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_comment_flags'
        unique_together = ['user_id', 'comment_id', 'flag']


class DjangoComments(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    object_pk = models.TextField()
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=75)
    user_url = models.CharField(max_length=200)
    comment = models.TextField()
    submit_date = models.DateTimeField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    is_public = models.BooleanField()
    is_removed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'django_comments'
'''


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = ['app_label', 'model']


'''
class DjangoEvolution(models.Model):
    version = models.ForeignKey('DjangoProjectVersion', models.DO_NOTHING)
    app_label = models.CharField(max_length=200)
    label = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_evolution'


class DjangoFlatpage(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    enable_comments = models.BooleanField()
    template_name = models.CharField(max_length=70)
    registration_required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'django_flatpage'


class DjangoFlatpageSites(models.Model):
    flatpage = models.ForeignKey(DjangoFlatpage, models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_flatpage_sites'
        unique_together = ['flatpage_id', 'site_id']


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoProjectVersion(models.Model):
    signature = models.TextField()
    when = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_project_version'


class DjangoSelect2Keymap(models.Model):
    key = models.CharField(unique=True, max_length=40)
    value = models.CharField(max_length=100)
    accessed_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_select2_keymap'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
'''


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


'''

class FacebookconnectFacebookprofile(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    facebook_id = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'facebookconnect_facebookprofile'


class FacebookconnectFacebooktemplate(models.Model):
    name = models.CharField(unique=True, max_length=50)
    template_bundle_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'facebookconnect_facebooktemplate'
'''


class GeneralDepartamento(models.Model):
    nombre = models.CharField(max_length=70)
    region = models.ForeignKey('GeneralRegion', models.DO_NOTHING)
    old_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_departamento'


class GeneralGenero(models.Model):
    nombre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'general_genero'


class GeneralMunicipio(models.Model):
    nombre = models.CharField(max_length=70)
    departamento = models.ForeignKey(GeneralDepartamento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'general_municipio'


class GeneralProfesion(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'general_profesion'


class GeneralRangoedad(models.Model):
    edad_minima = models.SmallIntegerField()
    edad_maxima = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'general_rangoedad'


class GeneralRegion(models.Model):
    nombre = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'general_region'


class GeneralSectorindustria(models.Model):
    nombre = models.CharField(max_length=140)

    class Meta:
        managed = False
        db_table = 'general_sectorindustria'


class GeneralTema(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'general_tema'


'''
class GrappelliBookmark(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'grappelli_bookmark'


class GrappelliBookmarkitem(models.Model):
    bookmark = models.ForeignKey(GrappelliBookmark, models.DO_NOTHING)
    title = models.CharField(max_length=80)
    link = models.CharField(max_length=200)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grappelli_bookmarkitem'


class GrappelliHelp(models.Model):
    title = models.CharField(max_length=50)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grappelli_help'


class GrappelliHelpitem(models.Model):
    help = models.ForeignKey(GrappelliHelp, models.DO_NOTHING)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    body = models.TextField()
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grappelli_helpitem'


class GrappelliNavigation(models.Model):
    title = models.CharField(max_length=30)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grappelli_navigation'


class GrappelliNavigationitem(models.Model):
    navigation = models.ForeignKey(GrappelliNavigation, models.DO_NOTHING)
    title = models.CharField(max_length=30)
    link = models.CharField(max_length=200)
    category = models.CharField(max_length=1)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grappelli_navigationitem'


class GrappelliNavigationitemGroups(models.Model):
    navigationitem = models.ForeignKey(GrappelliNavigationitem, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'grappelli_navigationitem_groups'
        unique_together = ['navigationitem_id', 'group_id']


class GrappelliNavigationitemUsers(models.Model):
    navigationitem = models.ForeignKey(GrappelliNavigationitem, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'grappelli_navigationitem_users'
        unique_together = ['navigationitem_id', 'user_id']
'''


class GrupoGrupo(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    persona = models.ForeignKey(CongresoPersona, models.DO_NOTHING)
    nombre_grupo = models.CharField(max_length=200)
    nombre_contacto = models.CharField(max_length=120, blank=True, null=True)
    email_contacto = models.CharField(max_length=120, blank=True, null=True)
    sitio_web = models.CharField(max_length=200, blank=True, null=True)
    fecha_fundacion = models.DateField(blank=True, null=True)
    objetivos = models.TextField(blank=True, null=True)
    activo = models.BooleanField()
    imagen = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    mision = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupo_grupo'


class HomeBanner(models.Model):
    titulo = models.CharField(max_length=140)
    texto = models.CharField(max_length=280)
    img = models.CharField(max_length=100)
    activo = models.BooleanField()
    orden = models.IntegerField()
    link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_banner'


class HomeFeedhome(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    feed_rss = models.CharField(max_length=200)
    enlace = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'home_feedhome'


class HomeFrasemencion(models.Model):
    frase = models.TextField()
    sitio = models.CharField(max_length=70)
    enlace = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_frasemencion'


class HomeLinkfooter(models.Model):
    nombre = models.CharField(max_length=80)
    enlace = models.CharField(max_length=200)
    activo = models.BooleanField()
    orden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'home_linkfooter'


class HomeSeccionhome(models.Model):
    nombre = models.CharField(max_length=40)
    nombre_template = models.CharField(max_length=200)
    activo = models.BooleanField()
    orden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'home_seccionhome'


'''
class LibCounter(models.Model):
    entity_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    count = models.IntegerField()
    counted_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    counted_object_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lib_counter'


class OpenidConsumerAssociation(models.Model):
    server_url = models.TextField()
    handle = models.CharField(max_length=255)
    secret = models.TextField()
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'openid_consumer_association'


class OpenidConsumerNonce(models.Model):
    server_url = models.CharField(max_length=200)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'openid_consumer_nonce'
'''


class OrdenDelDiaCargocitado(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=200)
    old_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_cargocitado'


class OrdenDelDiaCitacion(models.Model):
    itemdeordendeldia_ptr = models.OneToOneField('OrdenDelDiaItemdeordendeldia', models.DO_NOTHING, primary_key=True)
    tipo = models.ForeignKey('OrdenDelDiaTipocitacion', models.DO_NOTHING)
    tema_principal = models.ForeignKey(GeneralTema, related_name='citacion_tema_principal', blank=True, null=True)
    tema_secundario = models.ForeignKey(GeneralTema, related_name='citacion_tema_secundario', blank=True, null=True)
    plenaria = models.BooleanField()
    tags = models.CharField(max_length=200, blank=True, null=True)
    fecha_proposicion = models.DateField(blank=True, null=True)
    old_id = models.IntegerField(blank=True, null=True)
    detalles = models.TextField(blank=True, null=True)
    gacetas = models.CharField(max_length=50, blank=True, null=True)
    cuestionario = models.TextField(blank=True, null=True)
    numero_proposicion = models.CharField(max_length=200, blank=True, null=True)
    respuesta = models.TextField(blank=True, null=True)
    duplicado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'orden_del_dia_citacion'


class OrdenDelDiaCitacionCitantes(models.Model):
    citacion = models.ForeignKey('OrdenDelDiaCitacion', models.DO_NOTHING)
    congresista = models.ForeignKey('CongresoCongresista', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_citacion_citantes'
        unique_together = ['citacion', 'congresista']


class OrdenDelDiaCitacionOtrosInvitados(models.Model):
    citacion = models.ForeignKey('OrdenDelDiaCitacion', models.DO_NOTHING)
    persona = models.ForeignKey('CongresoPersona', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_citacion_otros_invitados'
        unique_together = ['citacion', 'persona']


class OrdenDelDiaCitado(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombres = models.CharField(max_length=200, blank=True, null=True)
    entidad = models.ForeignKey('OrdenDelDiaEntidadcitado', models.DO_NOTHING, blank=True, null=True)
    cargo = models.ForeignKey(OrdenDelDiaCargocitado, models.DO_NOTHING, blank=True, null=True)
    old_id = models.IntegerField(blank=True, null=True)
    imagen = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_citado'


class OrdenDelDiaCitadoasistentecitacion(models.Model):
    citacion = models.ForeignKey(OrdenDelDiaCitacion, models.DO_NOTHING)
    citado = models.ForeignKey(OrdenDelDiaCitado, models.DO_NOTHING)
    asiste = models.NullBooleanField()
    delega_asistencia = models.BooleanField()
    excuso = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'orden_del_dia_citadoasistentecitacion'


class OrdenDelDiaEntidadcitado(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=200)
    old_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_entidadcitado'


class OrdenDelDiaInvitadoasistentecitacion(models.Model):
    citacion = models.ForeignKey(OrdenDelDiaCitacion, models.DO_NOTHING)
    citado = models.ForeignKey(OrdenDelDiaCitado, models.DO_NOTHING)
    asiste = models.NullBooleanField()
    delega_asistencia = models.BooleanField()
    excuso = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'orden_del_dia_invitadoasistentecitacion'


class OrdenDelDiaItemdeordendeldia(models.Model):
    orden = models.IntegerField()
    proposito = models.TextField(blank=True, null=True)
    importante = models.BooleanField()
    orden_del_dia = models.ForeignKey('OrdenDelDiaOrdendeldia', models.DO_NOTHING)
    realizado = models.NullBooleanField()
    menu_realizado = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_itemdeordendeldia'


class OrdenDelDiaOrdendeldia(models.Model):
    fecha_programada = models.DateTimeField()
    fecha_realizada = models.DateField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
    cuatrienio = models.ForeignKey(CongresoPeriodo, models.DO_NOTHING)
    realizado = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_ordendeldia'


class OrdenDelDiaOrdendeldiaCamaras(models.Model):
    ordendeldia = models.ForeignKey('OrdenDelDiaOrdendeldia', models.DO_NOTHING)
    camara = models.ForeignKey('CongresoCamara', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_ordendeldia_camaras'
        unique_together = ['ordendeldia', 'camara']


class OrdenDelDiaOrdendeldiaComisiones(models.Model):
    ordendeldia = models.ForeignKey('OrdenDelDiaOrdendeldia', models.DO_NOTHING)
    comision = models.ForeignKey('CongresoComision', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_ordendeldia_comisiones'
        unique_together = ['ordendeldia', 'comision']


class OrdenDelDiaProyectoenordendia(models.Model):
    itemdeordendeldia_ptr = models.OneToOneField('OrdenDelDiaItemdeordendeldia', models.DO_NOTHING, primary_key=True)
    proyecto = models.ForeignKey('ProyectoDeLeyProyectoley', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_proyectoenordendia'


class OrdenDelDiaTipocitacion(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_tipocitacion'


class OrdenDelDiaTipocitante(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'orden_del_dia_tipocitante'


class ProyectoDeLeyAutorproyectoley(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    tipo_autor = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    autor_id = models.IntegerField()
    proyecto_ley = models.ForeignKey('ProyectoDeLeyProyectoley', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_autorproyectoley'


class ProyectoDeLeyClasevotacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_clasevotacion'


class ProyectoDeLeyEstadodeproyectodeley(models.Model):
    fecha = models.DateField(blank=True, null=True)
    estado = models.ForeignKey('ProyectoDeLeyEstadoproyectoley', models.DO_NOTHING)
    proyecto = models.ForeignKey('ProyectoDeLeyProyectoley', models.DO_NOTHING)
    gaceta = models.CharField(max_length=50, blank=True, null=True)
    old_id = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)
    camara_id = models.IntegerField(blank=True, null=True)
    numero_titulos = models.IntegerField(blank=True, null=True)
    numero_articulos = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_estadodeproyectodeley'


class ProyectoDeLeyEstadodeproyectodeleyComisiones(models.Model):
    estadodeproyectodeley = models.ForeignKey(ProyectoDeLeyEstadodeproyectodeley, models.DO_NOTHING)
    comision = models.ForeignKey(CongresoComision, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_estadodeproyectodeley_comisiones'
        unique_together = ['estadodeproyectodeley', 'comision']


class ProyectoDeLeyEstadodeproyectodeleyPonentes(models.Model):
    estadodeproyectodeley = models.ForeignKey('ProyectoDeLeyEstadodeproyectodeley', models.DO_NOTHING)
    congresista = models.ForeignKey('CongresoCongresista', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_estadodeproyectodeley_ponentes'
        unique_together = ['estadodeproyectodeley', 'congresista']


class ProyectoDeLeyEstadoproyectoley(models.Model):
    nombre = models.CharField(max_length=50)
    old_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_estadoproyectoley'


class ProyectoDeLeyIniciativa(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_iniciativa'


class ProyectoDeLeyLegislatura(models.Model):
    nombre = models.CharField(max_length=7)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cuatrienio = models.ForeignKey(CongresoPeriodo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_legislatura'


class ProyectoDeLeyOtroautor(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(unique=True, max_length=200)
    imagen = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_otroautor'


class ProyectoDeLeyProyectoley(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    tipo_proyecto = models.ForeignKey('ProyectoDeLeyTipoproyecto', models.DO_NOTHING)
    titulo = models.TextField()
    tema_principal = models.ForeignKey(GeneralTema, related_name='tema_principal', blank=True, null=True)
    tema_secundario = models.ForeignKey(GeneralTema, related_name='tema_secundario', blank=True, null=True)
    sinapsis = models.TextField(blank=True, null=True)
    numero_camara = models.CharField(max_length=10, blank=True, null=True)
    numero_senado = models.CharField(max_length=10, blank=True, null=True)
    estado_actual = models.ForeignKey(ProyectoDeLeyEstadoproyectoley, models.DO_NOTHING, blank=True, null=True)
    fecha_radicacion = models.DateField(blank=True, null=True)
    periodo = models.ForeignKey(CongresoPeriodo, models.DO_NOTHING)
    iniciativa = models.ForeignKey(ProyectoDeLeyIniciativa, models.DO_NOTHING)
    tags = models.CharField(max_length=200, blank=True, null=True)
    old_id = models.IntegerField(blank=True, null=True)
    se_acumula_a = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    camara_id = models.IntegerField(blank=True, null=True)
    legislatura_id = models.IntegerField(blank=True, null=True)
    enlace_a_texto = models.CharField(max_length=200, blank=True, null=True)
    enlace_a_informe_derecho_justo = models.CharField(max_length=200, blank=True, null=True)
    estado_proyecto_ley_actual = models.ForeignKey(ProyectoDeLeyEstadodeproyectodeley, models.DO_NOTHING, blank=True,
                                                   null=True)
    alias = models.CharField(max_length=300, blank=True, null=True)
    importancia = models.FloatField()
    destacado = models.BooleanField()
    alcance = models.IntegerField(blank=True, null=True)
    norma = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_proyectoley'


class ProyectoDeLeyTextosComparacion(models.Model):
    base = models.ForeignKey('ProyectoDeLeyTextosTextoproyectoley', related_name='base')
    modificado = models.ForeignKey('ProyectoDeLeyTextosTextoproyectoley', related_name='modificado')
    orden = models.SmallIntegerField()
    proyecto = models.ForeignKey(ProyectoDeLeyProyectoley, models.DO_NOTHING)
    diferencias_encoded = models.TextField()

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_textos_comparacion'


class ProyectoDeLeyTextosTextoproyectoley(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    proyecto_ley = models.ForeignKey(ProyectoDeLeyProyectoley, models.DO_NOTHING)
    estado_proyecto_ley = models.ForeignKey(ProyectoDeLeyEstadodeproyectodeley, models.DO_NOTHING)
    texto_html = models.TextField(blank=True, null=True)
    texto_plano = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_textos_textoproyectoley'


class ProyectoDeLeyTipoproyecto(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_tipoproyecto'


class ProyectoDeLeyTipovotacion(models.Model):
    nombre = models.CharField(max_length=50)
    procedimental = models.BooleanField()
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_tipovotacion'


class ProyectoDeLeyVotacion(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    fecha = models.DateField()
    proyecto = models.ForeignKey(ProyectoDeLeyProyectoley, models.DO_NOTHING, blank=True, null=True)
    motivo = models.TextField()
    a_favor = models.CharField(max_length=50, blank=True, null=True)
    en_contra = models.CharField(max_length=50, blank=True, null=True)
    votosfavor = models.IntegerField(db_column='votosFavor')  # Field name made lowercase.
    votoscontra = models.IntegerField(db_column='votosContra')  # Field name made lowercase.
    aprobado = models.NullBooleanField()
    tipo_votacion = models.ForeignKey(ProyectoDeLeyTipovotacion, models.DO_NOTHING)
    gaceta = models.CharField(max_length=50, blank=True, null=True)
    acta = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    votacion_en_dia = models.IntegerField(blank=True, null=True)
    destacada = models.BooleanField()
    old_id = models.CharField(max_length=100, blank=True, null=True)
    aprobada = models.IntegerField(blank=True, null=True)
    cuatrienio_id = models.IntegerField(blank=True, null=True)
    votosabstencion = models.IntegerField(db_column='votosAbstencion', blank=True,
                                          null=True)  # Field name made lowercase.
    numero_no_asistencias = models.IntegerField()
    clase_votacion = models.ForeignKey(ProyectoDeLeyClasevotacion, models.DO_NOTHING)
    numero_asistencias = models.IntegerField()
    datos_importacion = models.TextField(blank=True, null=True)
    resultados_importacion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_votacion'


class ProyectoDeLeyVotacionCamaras(models.Model):
    votacion = models.ForeignKey('ProyectoDeLeyVotacion', models.DO_NOTHING)
    camara = models.ForeignKey('CongresoCamara', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_votacion_camaras'
        unique_together = ['votacion', 'camara']


class ProyectoDeLeyVotacionComisiones(models.Model):
    votacion = models.ForeignKey('ProyectoDeLeyVotacion', models.DO_NOTHING)
    comision = models.ForeignKey('CongresoComision', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_votacion_comisiones'
        unique_together = ['votacion', 'comision']


class ProyectoDeLeyVotacionEstadosProyecto(models.Model):
    votacion = models.ForeignKey('ProyectoDeLeyVotacion', models.DO_NOTHING)
    estadodeproyectodeley = models.ForeignKey('ProyectoDeLeyEstadodeproyectodeley', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_votacion_estados_proyecto'
        unique_together = ['votacion', 'estadodeproyectodeley']


class ProyectoDeLeyVotacionpartido(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    numero_votos_si = models.IntegerField()
    numero_votos_no = models.IntegerField()
    numero_votos_abstencion = models.IntegerField()
    opcion_preferida = models.IntegerField(blank=True, null=True)
    partido = models.ForeignKey(CongresoPartido, models.DO_NOTHING)
    votacion = models.ForeignKey(ProyectoDeLeyVotacion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_votacionpartido'


class ProyectoDeLeyVoto(models.Model):
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField(blank=True, null=True)
    votacion = models.ForeignKey(ProyectoDeLeyVotacion, models.DO_NOTHING)
    voto = models.IntegerField()
    congresista = models.ForeignKey(CongresoCongresista, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_voto'


class ProyectoDeLeyVotociudadano(models.Model):
    voto = models.BooleanField()
    votante = models.ForeignKey(CongresoPersona, models.DO_NOTHING)
    proyecto = models.ForeignKey(ProyectoDeLeyProyectoley, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyecto_de_ley_votociudadano'


class ReportesReporte(models.Model):
    nombre = models.CharField(max_length=140)
    descripcion = models.TextField()
    enlace = models.CharField(max_length=200)
    activo = models.BooleanField()
    orden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reportes_reporte'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = ['handle', 'server_url']


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = ['timestamp', 'salt', 'server_url']


'''
class SocialAuthUsersocialauth(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = ['provider', 'uid']


class SocialauthAuthmeta(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    provider = models.CharField(max_length=30)
    is_email_filled = models.BooleanField()
    is_profile_modified = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'socialauth_authmeta'


class SocialauthFacebookuserprofile(models.Model):
    facebook_uid = models.CharField(unique=True, max_length=20)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    profile_image_url = models.CharField(max_length=200, blank=True, null=True)
    profile_image_url_big = models.CharField(max_length=200, blank=True, null=True)
    profile_image_url_small = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    about_me = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialauth_facebookuserprofile'


class SocialauthLinkedinuserprofile(models.Model):
    linkedin_uid = models.CharField(unique=True, max_length=50)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    headline = models.CharField(max_length=120, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    profile_image_url = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialauth_linkedinuserprofile'


class SocialauthOpenidprofile(models.Model):
    openid_key = models.CharField(unique=True, max_length=200)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    is_username_valid = models.BooleanField()
    email = models.CharField(max_length=75)
    nickname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'socialauth_openidprofile'


class SocialauthTwitteruserprofile(models.Model):
    screen_name = models.CharField(unique=True, max_length=200)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    profile_image_url = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialauth_twitteruserprofile'


class SouthMigrationhistory(models.Model):
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'south_migrationhistory'
'''
