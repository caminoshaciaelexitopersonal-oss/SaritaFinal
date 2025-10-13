import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .fields import EncryptedTextField


def prestador_directory_path(instance, filename):
    # Asegurarse de que el username existe antes de crear la ruta
    username = instance.usuario.username if instance.usuario else 'default'
    return f'prestadores/{username}/{filename}'

def galeria_directory_path(instance, filename):
    # Asegurarse de que el username existe en la ruta anidada
    username = instance.prestador.usuario.username if instance.prestador and instance.prestador.usuario else 'default'
    return f'prestadores/{username}/galeria/{filename}'

def documentos_directory_path(instance, filename):
    return f'prestadores/{instance.prestador.usuario.username}/documentos/{filename}'

def atractivo_directory_path(instance, filename):
    return f'atractivos/{instance.atractivo.slug}/{filename}'

def homepage_component_directory_path(instance, filename):
    return f'homepage_components/{uuid.uuid4()}_{filename}'

def artesano_directory_path(instance, filename):
    return f'artesanos/{instance.usuario.username}/{filename}'

def galeria_artesano_directory_path(instance, filename):
    return f'artesanos/{instance.artesano.usuario.username}/galeria/{filename}'

def site_config_directory_path(instance, filename):
    return f'site_config/{filename}'

class Departamento(models.Model):
    codigo_departamento = models.CharField(max_length=10, primary_key=True)
    nombre_departamento = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_departamento

class Municipio(models.Model):
    codigo_municipio = models.CharField(max_length=10, primary_key=True)
    nombre_municipio = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='municipios')

    def __str__(self):
        return f"{self.nombre_municipio}, {self.departamento.nombre_departamento}"

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", _("Administrador General")
        ADMIN_DEPENDENCIA = "ADMIN_DEPENDENCIA", _("Administrador de Dependencia")
        FUNCIONARIO_DIRECTIVO = "FUNCIONARIO_DIRECTIVO", _("Funcionario Directivo")
        FUNCIONARIO_PROFESIONAL = "FUNCIONARIO_PROFESIONAL", _("Funcionario Profesional")
        FUNCIONARIO_TECNICO = "FUNCIONARIO_TECNICO", _("Funcionario Técnico")
        PRESTADOR = "PRESTADOR", _("Prestador de Servicio")
        ARTESANO = "ARTESANO", _("Artesano")
        CONSEJO_CONSULTIVO_TURISMO = "CONSEJO_CONSULTIVO_TURISMO", _("Consejo Consultivo de Turismo")
        TURISTA = "TURISTA", _("Turista")

    class AIProvider(models.TextChoices):
        OPENAI = "OPENAI", _("OpenAI")
        GOOGLE = "GOOGLE", _("Google")
        GROQ = "GROQ", _("Groq")

    base_role = Role.TURISTA
    role = models.CharField(_("Rol"), max_length=50, choices=Role.choices)

    # --- Campos de Caracterización del Turista ---
    class Origen(models.TextChoices):
        LOCAL = "LOCAL", _("Puerto Gaitán")
        REGIONAL = "REGIONAL", _("Meta")
        NACIONAL = "NACIONAL", _("Nacional (Otro Departamento)")
        EXTRANJERO = "EXTRANJERO", _("Extranjero")

    origen = models.CharField(
        _("Origen del Turista"),
        max_length=20,
        choices=Origen.choices,
        blank=True,
        null=True,
        help_text=_("Indica la procedencia del turista.")
    )
    pais_origen = models.CharField(
        _("País de Origen"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("País de origen, si el turista es extranjero.")
    )

    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True)
    empresa_asociada = models.ForeignKey('PrestadorServicio', on_delete=models.SET_NULL, blank=True, null=True, related_name='empleados_customuser')

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.is_superuser:
                self.role = self.Role.ADMIN
            elif not self.role:
                self.role = self.base_role
        super().save(*args, **kwargs)

class UserLLMConfig(models.Model):
    """
    Almacena la configuración de LLM personalizada para un usuario.
    """
    class Provider(models.TextChoices):
        SYSTEM_DEFAULT = "SYSTEM_DEFAULT", _("Usar Configuración del Sistema")
        GROQ = "GROQ", _("Groq Personalizado")
        PHI3_LOCAL = "PHI3_LOCAL", _("Modelo Local Phi-3 Mini")
        PHI4_LOCAL = "PHI4_LOCAL", _("Modelo Local Phi-4")

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="llm_config",
        verbose_name=_("Usuario")
    )
    provider = models.CharField(
        _("Proveedor"),
        max_length=50,
        choices=Provider.choices,
        default=Provider.SYSTEM_DEFAULT,
        help_text=_("El proveedor de LLM que el usuario prefiere usar.")
    )
    api_key = EncryptedTextField(
        _("Clave de API Personalizada"),
        blank=True,
        null=True,
        help_text=_("La clave de API para el proveedor seleccionado (ej. Groq). Se almacena de forma segura.")
    )
    created_at = models.DateTimeField(_("Fecha de Creación"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Última Actualización"), auto_now=True)

    def __str__(self):
        return f"Configuración LLM para {self.user.username}"

    class Meta:
        verbose_name = "Configuración LLM de Usuario"
        verbose_name_plural = "Configuraciones LLM de Usuarios"


class CategoriaPrestador(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="Versión del nombre amigable para URLs")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Categoría de Prestador"
        verbose_name_plural = "Categorías de Prestadores"


class PrestadorServicio(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="perfil_prestador")
    categoria = models.ForeignKey(CategoriaPrestador, on_delete=models.SET_NULL, null=True, related_name="prestadores")
    nombre_negocio = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    foto_principal = models.ImageField(upload_to=prestador_directory_path, blank=True, null=True, help_text="Una foto representativa del negocio o servicio.")
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email_contacto = models.EmailField(max_length=254, blank=True, null=True)
    red_social_facebook = models.URLField(blank=True, null=True)
    red_social_instagram = models.URLField(blank=True, null=True)
    red_social_tiktok = models.URLField(blank=True, null=True)
    red_social_whatsapp = models.CharField(max_length=20, blank=True, null=True, help_text="Número de WhatsApp con código de país")

    nit = models.CharField(max_length=20, unique=True, blank=True, null=True)
    tipo_prestador = models.CharField(max_length=255, blank=True, null=True)
    tipo_prestador_otro = models.CharField(max_length=255, blank=True, null=True)
    es_formal = models.BooleanField(default=True)
    rnt = models.CharField(max_length=50, blank=True, null=True)
    registrada_por_usuario = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='empresas_registradas')

    # --- Campos de Ubicación Estructurados ---
    direccion = models.CharField(_("Dirección"), max_length=255, blank=True, null=True)
    latitud = models.FloatField(_("Latitud"), blank=True, null=True)
    longitud = models.FloatField(_("Longitud"), blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)

    promociones_ofertas = models.TextField(blank=True, null=True, help_text="Detalles de promociones, menús, paquetes, etc.")
    aprobado = models.BooleanField(default=False, help_text="El administrador debe aprobar este perfil para que sea visible.")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True) 

    # --- Scoring Fields ---
    puntuacion_verificacion = models.PositiveIntegerField(default=0, help_text="Puntaje acumulado de verificaciones de cumplimiento.")
    puntuacion_capacitacion = models.PositiveIntegerField(default=0, help_text="Puntaje acumulado por asistencia a capacitaciones.")
    puntuacion_reseñas = models.PositiveIntegerField(default=0, help_text="Puntaje acumulado por reseñas de turistas.")
    puntuacion_formularios = models.PositiveIntegerField(default=0, help_text="Puntaje por completar formularios de caracterización.")
    puntuacion_total = models.PositiveIntegerField(default=0, db_index=True, help_text="Puntaje total para posicionamiento. Se calcula automáticamente.")

    def __str__(self):
        return self.nombre_negocio

    def recalcular_puntuacion_total(self):
        """
        Calcula la puntuación total y guarda todos los campos de puntuación
        parciales y el total en una sola operación de base de datos.
        """
        self.puntuacion_total = (
            getattr(self, 'puntuacion_verificacion', 0) +
            getattr(self, 'puntuacion_capacitacion', 0) +
            getattr(self, 'puntuacion_reseñas', 0) +
            getattr(self, 'puntuacion_formularios', 0)
        )
        self.save(update_fields=[
            'puntuacion_verificacion',
            'puntuacion_capacitacion',
            'puntuacion_reseñas',
            'puntuacion_formularios',
            'puntuacion_total'
        ])

    class Meta:
        verbose_name = "Prestador de Servicio"
        verbose_name_plural = "Prestadores de Servicios"


class DetallesHotel(models.Model):
    prestador = models.OneToOneField(PrestadorServicio, on_delete=models.CASCADE, related_name="detalles_hotel", limit_choices_to={'categoria__slug': 'hoteles'})
    reporte_ocupacion_nacional = models.PositiveIntegerField(default=0, help_text="Exclusivo para hoteles")
    reporte_ocupacion_internacional = models.PositiveIntegerField(default=0, help_text="Exclusivo para hoteles")

    def __str__(self):
        return f"Detalles de Hotel para {self.prestador.nombre_negocio}"

    class Meta:
        verbose_name = "Detalles de Hotel"
        verbose_name_plural = "Detalles de Hoteles"


class RubroArtesano(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="Versión del nombre amigable para URLs")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Rubro de Artesano"
        verbose_name_plural = "Rubros de Artesanos"


class Artesano(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="perfil_artesano")
    rubro = models.ForeignKey(RubroArtesano, on_delete=models.SET_NULL, null=True, related_name="artesanos")
    nombre_taller = models.CharField(max_length=200, help_text="Nombre del taller o marca personal del artesano.")
    nombre_artesano = models.CharField(max_length=200, help_text="Nombre completo del artesano.")
    descripcion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email_contacto = models.EmailField(max_length=254, blank=True, null=True)
    foto_principal = models.ImageField(upload_to=artesano_directory_path, blank=True, null=True, help_text="Una foto representativa del artesano o sus productos.")
    red_social_facebook = models.URLField(blank=True, null=True)
    red_social_instagram = models.URLField(blank=True, null=True)
    red_social_tiktok = models.URLField(blank=True, null=True)
    red_social_whatsapp = models.CharField(max_length=20, blank=True, null=True, help_text="Número de WhatsApp con código de país")

    # --- Campos de Ubicación Estructurados ---
    direccion = models.CharField(_("Dirección"), max_length=255, blank=True, null=True)
    latitud = models.FloatField(_("Latitud"), blank=True, null=True)
    longitud = models.FloatField(_("Longitud"), blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)

    aprobado = models.BooleanField(default=False, help_text="El administrador debe aprobar este perfil para que sea visible.")

    # --- Scoring Fields ---
    puntuacion_capacitacion = models.PositiveIntegerField(default=0, help_text="Puntaje acumulado por asistencia a capacitaciones.")
    puntuacion_reseñas = models.PositiveIntegerField(default=0, help_text="Puntaje acumulado por reseñas de turistas.")
    puntuacion_formularios = models.PositiveIntegerField(default=0, help_text="Puntaje por completar formularios de caracterización.")
    puntuacion_total = models.PositiveIntegerField(default=0, db_index=True, help_text="Puntaje total para posicionamiento. Se calcula automáticamente.")

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_taller

    def recalcular_puntuacion_total(self):
        """
        Calcula la puntuación total y guarda todos los campos de puntuación
        parciales y el total en una sola operación de base de datos.
        """
        self.puntuacion_total = (
            getattr(self, 'puntuacion_capacitacion', 0) +
            getattr(self, 'puntuacion_reseñas', 0) +
            getattr(self, 'puntuacion_formularios', 0)
        )
        self.save(update_fields=[
            'puntuacion_capacitacion',
            'puntuacion_reseñas',
            'puntuacion_formularios',
            'puntuacion_total'
        ])

    class Meta:
        verbose_name = "Artesano"
        verbose_name_plural = "Artesanos"


class PerfilAdministrador(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="perfil_administrador")
    cargo = models.CharField(_("Cargo"), max_length=150, blank=True, null=True)
    dependencia_asignada = models.CharField(_("Dependencia Asignada"), max_length=150, blank=True, null=True)
    nivel_acceso = models.CharField(_("Nivel de Acceso"), max_length=150, blank=True, null=True)

    def __str__(self):
        return f"Perfil de Administrador para {self.usuario.username}"

    class Meta:
        verbose_name = "Perfil de Administrador"
        verbose_name_plural = "Perfiles de Administradores"


class PerfilFuncionarioDirectivo(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="perfil_funcionario_directivo")
    dependencia = models.CharField(_("Dependencia"), max_length=150, blank=True, null=True)
    nivel_direccion = models.CharField(_("Nivel de Dirección"), max_length=150, blank=True, null=True)
    area_funcional = models.CharField(_("Área Funcional"), max_length=150, blank=True, null=True)

    def __str__(self):
        return f"Perfil de Funcionario Directivo para {self.usuario.username}"

    class Meta:
        verbose_name = "Perfil de Funcionario Directivo"
        verbose_name_plural = "Perfiles de Funcionarios Directivos"


class PerfilFuncionarioProfesional(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="perfil_funcionario_profesional")
    dependencia = models.CharField(_("Dependencia"), max_length=150, blank=True, null=True)
    profesion = models.CharField(_("Profesión"), max_length=150, blank=True, null=True)
    area_asignada = models.CharField(_("Área Asignada"), max_length=150, blank=True, null=True)

    def __str__(self):
        return f"Perfil de Funcionario Profesional para {self.usuario.username}"

    class Meta:
        verbose_name = "Perfil de Funcionario Profesional"
        verbose_name_plural = "Perfiles de Funcionarios Profesionales"


class ImagenArtesano(models.Model):
    artesano = models.ForeignKey(Artesano, on_delete=models.CASCADE, related_name="galeria_imagenes")
    imagen = models.ImageField(upload_to=galeria_artesano_directory_path)
    alt_text = models.CharField(max_length=255, blank=True, help_text="Texto alternativo para accesibilidad")
    def __str__(self):
        return f"Imagen de {self.artesano.nombre_taller}"


class ImagenGaleria(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name="galeria_imagenes")
    imagen = models.ImageField(upload_to=galeria_directory_path)
    alt_text = models.CharField(max_length=255, blank=True, help_text="Texto alternativo para accesibilidad")
    def __str__(self):
        return f"Imagen de {self.prestador.nombre_negocio}"


class DocumentoLegalizacion(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name="documentos_legalizacion")
    documento = models.FileField(upload_to=documentos_directory_path)
    nombre_documento = models.CharField(max_length=100)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombre_documento} de {self.prestador.nombre_negocio}"


class Publicacion(models.Model):
    class Tipo(models.TextChoices):
        EVENTO = "EVENTO", _("Evento")
        NOTICIA = "NOTICIA", _("Noticia")
        BLOG = "BLOG", _("Blog")
        CAPACITACION = "CAPACITACION", _("Capacitación")

    class Status(models.TextChoices):
        BORRADOR = "BORRADOR", _("Borrador")
        PENDIENTE_DIRECTIVO = "PENDIENTE_DIRECTIVO", _("Pendiente de Aprobación por Directivo")
        PENDIENTE_ADMIN = "PENDIENTE_ADMIN", _("Pendiente de Aprobación por Administrador")
        PUBLICADO = "PUBLICADO", _("Publicado")

    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    contenido = models.TextField()
    imagen_principal = models.ImageField(upload_to='publicaciones/', blank=True, null=True)
    autor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="publicaciones")

    class SubCategoria(models.TextChoices):
        CULTURAL = "CULTURAL", _("Cultural")
        DEPORTIVO = "DEPORTIVO", _("Deportivo")
        RELIGIOSO = "RELIGIOSO", _("Religioso")
        CIVICO = "CIVICO", _("Cívico")
        OTRO = "OTRO", _("Otro")
    subcategoria_evento = models.CharField(_("Subcategoría de Evento"), max_length=50, choices=SubCategoria.choices, blank=True, null=True, help_text="Clasificación específica solo para eventos.")

    fecha_evento_inicio = models.DateTimeField(blank=True, null=True)
    fecha_evento_fin = models.DateTimeField(blank=True, null=True)
    puntos_asistencia = models.PositiveIntegerField(default=0, help_text="Puntos otorgados por asistir a esta capacitación (solo si tipo=CAPACITACION).")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    estado = models.CharField(
        _("Estado de Publicación"),
        max_length=20,
        choices=Status.choices,
        default=Status.BORRADOR,
        db_index=True,
        help_text="Estado del flujo de aprobación de la publicación."
    )

    def __str__(self):
        return f"[{self.get_tipo_display()}] {self.titulo}"

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-fecha_publicacion']


class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    url_youtube = models.URLField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    es_publicado = models.BooleanField(default=False, help_text="Marcar para que el video sea visible en el sitio web público.")
    def __str__(self):
        return self.titulo


class ConsejoConsultivo(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    documento_adjunto = models.FileField(upload_to='consejo_consultivo/', blank=True, null=True, help_text="Documento opcional (PDF, Word, etc.)")
    es_publicado = models.BooleanField(default=False, help_text="Marcar para que el contenido sea visible en el sitio web público.")
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Publicación del Consejo Consultivo"
        verbose_name_plural = "Publicaciones del Consejo Consultivo"
        ordering = ['-fecha_publicacion']


class AtractivoTuristico(models.Model):
    class CategoriaColor(models.TextChoices):
        AMARILLO = "AMARILLO", _("Cultural/Histórico")
        ROJO = "ROJO", _("Urbano/Parque")
        BLANCO = "BLANCO", _("Natural")
    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True, help_text="Versión del nombre amigable para URLs")
    descripcion = models.TextField()
    como_llegar = models.TextField(help_text="Instrucciones sobre cómo llegar al atractivo.")

    # --- Campos de Ubicación Estructurados ---
    direccion = models.CharField(_("Dirección"), max_length=255, blank=True, null=True)
    latitud = models.FloatField(_("Latitud"), blank=True, null=True)
    longitud = models.FloatField(_("Longitud"), blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)

    categoria_color = models.CharField(_("Categoría de Color"), max_length=10, choices=CategoriaColor.choices)

    imagen_principal = models.ImageField(upload_to=atractivo_directory_path, blank=True, null=True, help_text="Imagen principal que se mostrará en listados y cabeceras.")
    horario_funcionamiento = models.TextField(_("Horario de Funcionamiento"), blank=True, help_text="Ej: Lunes a Viernes de 9am a 5pm. Fines de semana de 10am a 6pm.")
    tarifas = models.TextField(_("Tarifas"), blank=True, help_text="Información sobre precios de entrada. Ej: Adultos: $10, Niños: $5, Grupos: 10% de descuento.")
    recomendaciones = models.TextField(_("Recomendaciones"), blank=True, help_text="Sugerencias para los visitantes. Ej: Llevar ropa cómoda, protector solar, agua.")
    accesibilidad = models.TextField(_("Accesibilidad"), blank=True, help_text="Información sobre acceso para personas con movilidad reducida, rampas, etc.")
    informacion_contacto = models.TextField(_("Información de Contacto"), blank=True, help_text="Teléfonos, correos electrónicos o persona de contacto.")

    autor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, help_text="Usuario que creó el registro (Funcionario, Guía, etc.).")
    es_publicado = models.BooleanField(_("Publicado"), default=False, help_text="Marcar para que el atractivo sea visible en el sitio web público.")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Atractivo Turístico"
        verbose_name_plural = "Atractivos Turísticos"
        ordering = ['nombre']


class ImagenAtractivo(models.Model):
    atractivo = models.ForeignKey(AtractivoTuristico, on_delete=models.CASCADE, related_name="imagenes")
    imagen = models.ImageField(upload_to=atractivo_directory_path)
    alt_text = models.CharField(max_length=255, blank=True, help_text="Texto alternativo para accesibilidad y SEO")
    def __str__(self):
        return f"Imagen de {self.atractivo.nombre}"


def ruta_turistica_directory_path(instance, filename):
    return f'rutas_turisticas/{instance.slug}/{filename}'

class RutaTuristica(models.Model):
    nombre = models.CharField(_("Nombre de la Ruta"), max_length=200, unique=True)
    slug = models.SlugField(_("Slug"), max_length=220, unique=True, help_text="Versión del nombre amigable para URLs")
    descripcion = models.TextField(_("Descripción de la Ruta"))
    imagen_principal = models.ImageField(_("Imagen Principal"), upload_to=ruta_turistica_directory_path, help_text="Imagen principal que se mostrará en listados y cabeceras.")

    atractivos = models.ManyToManyField(AtractivoTuristico, related_name="rutas", blank=True, verbose_name=_("Atractivos en la Ruta"))
    prestadores = models.ManyToManyField(PrestadorServicio, related_name="rutas", blank=True, verbose_name=_("Prestadores en la Ruta"))

    es_publicado = models.BooleanField(_("Publicado"), default=False, help_text="Marcar para que la ruta sea visible en el sitio web público.")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Ruta Turística"
        verbose_name_plural = "Rutas Turísticas"
        ordering = ['nombre']

class ImagenRutaTuristica(models.Model):
    ruta = models.ForeignKey(RutaTuristica, on_delete=models.CASCADE, related_name="imagenes")
    imagen = models.ImageField(upload_to=ruta_turistica_directory_path)
    alt_text = models.CharField(max_length=255, blank=True, help_text="Texto alternativo para accesibilidad y SEO")

    def __str__(self):
        return f"Imagen de {self.ruta.nombre}"


class ElementoGuardado(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='elementos_guardados', limit_choices_to={'role': CustomUser.Role.TURISTA})
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    fecha_guardado = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.usuario.username} guardó {self.content_object}'
    class Meta:
        unique_together = ('usuario', 'content_type', 'object_id')
        ordering = ['-fecha_guardado']


def pagina_institucional_banner_path(instance, filename):
    return f'paginas_institucionales/{instance.slug}/{filename}'


class PaginaInstitucional(models.Model):
    nombre = models.CharField(_("Nombre de la Página"), max_length=150, unique=True)
    slug = models.SlugField(_("Slug"), max_length=150, unique=True, help_text="Identificador único para la URL. Ej: secretaria-turismo")
    titulo_banner = models.CharField(_("Título del Banner"), max_length=200, help_text="Título principal que se superpone en el banner.")
    subtitulo_banner = models.CharField(_("Subtítulo del Banner"), max_length=300, blank=True, null=True)
    banner = models.ImageField(_("Imagen de Banner"), upload_to=pagina_institucional_banner_path, help_text="Imagen principal que se mostrará en la parte superior de la página.")
    contenido_principal = models.TextField(_("Contenido Principal (Objetivos y Funciones)"), blank=True, help_text="Acepta formato Markdown.")
    programas_proyectos = models.TextField(_("Programas y Proyectos"), blank=True, help_text="Para la Secretaría. Acepta formato Markdown.")
    estrategias_apoyo = models.TextField(_("Estrategias de Apoyo"), blank=True, help_text="Para la Secretaría. Acepta formato Markdown.")
    politicas_locales = models.TextField(_("Políticas Locales de Turismo"), blank=True, help_text="Para la Dirección. Acepta formato Markdown.")
    convenios_asociaciones = models.TextField(_("Convenios y Asociaciones"), blank=True, help_text="Para la Dirección. Acepta formato Markdown.")
    informes_resultados = models.TextField(_("Informes de Resultados"), blank=True, help_text="Para la Dirección. Acepta formato Markdown.")
    actualizado_por = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role__in': [CustomUser.Role.ADMIN, CustomUser.Role.FUNCIONARIO_DIRECTIVO, CustomUser.Role.FUNCIONARIO_PROFESIONAL]})
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Página Institucional"
        verbose_name_plural = "Páginas Institucionales"
        ordering = ['nombre']


def pagina_institucional_galeria_path(instance, filename):
    return f'paginas_institucionales/{instance.pagina.slug}/galeria/{filename}'


class ImagenPaginaInstitucional(models.Model):
    pagina = models.ForeignKey(PaginaInstitucional, on_delete=models.CASCADE, related_name="galeria_imagenes")
    imagen = models.ImageField(_("Imagen de Galería"), upload_to=pagina_institucional_galeria_path)
    alt_text = models.CharField(max_length=255, blank=True, help_text="Texto alternativo para accesibilidad y SEO")
    orden = models.PositiveIntegerField(default=0, help_text="Orden de la imagen en el slider.")

    class Meta:
        verbose_name = "Imagen de Página Institucional"
        verbose_name_plural = "Imágenes de Página Institucional"
        ordering = ['orden']

    def __str__(self):
        return f"Imagen para {self.pagina.nombre}"


class ContenidoMunicipio(models.Model):
    class Seccion(models.TextChoices):
        INTRODUCCION = "INTRODUCCION", _("Introducción General")
        UBICACION_CLIMA = "UBICACION_CLIMA", _("Ubicación y Clima")
        ALOJAMIENTO = "ALOJAMIENTO", _("Alojamiento y Hotelería")
        COMO_LLEGAR = "COMO_LLEGAR", _("¿Cómo Llegar?")
        CONTACTOS = "CONTACTOS", _("Contactos de Interés")
        FINANZAS = "FINANZAS", _("Entidades Financieras")
        SECRETARIA_TURISMO = "SECRETARIA_TURISMO", _("Secretaría de Turismo y Desarrollo Económico")
        DIRECTORIO_FUNCIONARIOS = "DIRECTORIO_FUNCIONARIOS", _("Directorio - Funcionarios y Dependencias")
        DIRECTORIO_ENLACES = "DIRECTORIO_ENLACES", _("Directorio - Enlaces de Interés")
        OTRA = "OTRA", _("Otra Sección")
    seccion = models.CharField(_("Sección Temática"), max_length=50, choices=Seccion.choices, help_text="Agrupa el contenido bajo una categoría temática.")
    titulo = models.CharField(_("Título del Bloque"), max_length=255, help_text="El título principal que se mostrará para este bloque de contenido.")
    contenido = models.TextField(_("Contenido del Bloque"), help_text="El contenido principal. Se recomienda usar formato Markdown para el texto.")
    orden = models.PositiveIntegerField(default=0, db_index=True, help_text="Define el orden de aparición de los bloques en la página (0 primero, 1 después, etc.).")
    actualizado_por = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role__in': [CustomUser.Role.ADMIN, CustomUser.Role.FUNCIONARIO_DIRECTIVO, CustomUser.Role.FUNCIONARIO_PROFESIONAL]}, help_text="Último usuario que modificó este contenido.")
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    es_publicado = models.BooleanField(default=False, help_text="Marcar para que el contenido sea visible en el sitio web público.")
    def __str__(self):
        return f"{self.get_seccion_display()} - {self.titulo}"
    class Meta:
        verbose_name = "Contenido del Municipio"
        verbose_name_plural = "Contenidos del Municipio"
        ordering = ['orden', 'titulo']


class AgentTask(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", _("Pendiente")
        RUNNING = "RUNNING", _("En Ejecución")
        COMPLETED = "COMPLETED", _("Completada")
        FAILED = "FAILED", _("Fallida")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='agent_tasks')
    command = models.TextField(_("Comando del Usuario"), help_text="El comando en lenguaje natural que inició la tarea.")
    status = models.CharField(_("Estado de la Tarea"), max_length=20, choices=Status.choices, default=Status.PENDING, db_index=True)
    report = models.TextField(_("Informe Final"), blank=True, null=True, help_text="El informe final generado por el agente al completar la tarea.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Tarea {self.id} ({self.get_status_display()}) para {self.user.username if self.user else 'Anónimo'}"
    class Meta:
        verbose_name = "Tarea de Agente"
        verbose_name_plural = "Tareas de Agentes"
        ordering = ['-created_at']

class AuditLog(models.Model):
    class Action(models.TextChoices):
        USER_CREATE = "USER_CREATE", _("Usuario Creado")
        USER_UPDATE = "USER_UPDATE", _("Usuario Actualizado")
        USER_DELETE = "USER_DELETE", _("Usuario Eliminado")
        MENU_CREATE = "MENU_CREATE", _("Elemento de Menú Creado")
        MENU_UPDATE = "MENU_UPDATE", _("Elemento de Menú Actualizado")
        MENU_DELETE = "MENU_DELETE", _("Elemento de Menú Eliminado")
        SITE_CONFIG_UPDATE = "SITE_CONFIG_UPDATE", _("Configuración del Sitio Actualizada")
        COMPONENT_CREATE = "COMPONENT_CREATE", _("Componente de Inicio Creado")
        COMPONENT_UPDATE = "COMPONENT_UPDATE", _("Componente de Inicio Actualizado")
        COMPONENT_DELETE = "COMPONENT_DELETE", _("Componente de Inicio Eliminado")
        COMPONENT_REORDER = "COMPONENT_REORDER", _("Componentes de Inicio Reordenados")
        CONTENIDO_CREATE = "CONTENIDO_CREATE", _("Contenido de Municipio Creado")
        CONTENIDO_UPDATE = "CONTENIDO_UPDATE", _("Contenido de Municipio Actualizado")
        CONTENIDO_DELETE = "CONTENIDO_DELETE", _("Contenido de Municipio Eliminado")
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_logs', verbose_name=_("Usuario"))
    action = models.CharField(_("Acción"), max_length=50, choices=Action.choices, db_index=True)
    details = models.TextField(_("Detalles"), blank=True, null=True, help_text="Descripción detallada de la acción o los datos cambiados (ej. en formato JSON).")
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(_("Fecha y Hora"), auto_now_add=True, db_index=True)
    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {self.user} realizó {self.get_action_display()}"
    class Meta:
        verbose_name = "Registro de Auditoría"
        verbose_name_plural = "Registros de Auditoría"
        ordering = ['-timestamp']


class HomePageComponent(models.Model):
    class ComponentType(models.TextChoices):
        BANNER = "BANNER", _("Banner Principal")
        SLIDER = "SLIDER", _("Slider Secundario")
        CARD = "CARD", _("Tarjeta de Información")
    component_type = models.CharField(_("Tipo de Componente"), max_length=20, choices=ComponentType.choices, default=ComponentType.BANNER)
    title = models.CharField(_("Título"), max_length=200)
    subtitle = models.CharField(_("Subtítulo"), max_length=300, blank=True, null=True)
    image = models.ImageField(_("Imagen"), upload_to=homepage_component_directory_path, help_text="Imagen principal para el componente.")
    link_url = models.URLField(_("URL de Destino"), blank=True, null=True, help_text="El enlace al que dirigirá el componente al hacer clic.")
    order = models.PositiveIntegerField(_("Orden"), default=0, db_index=True, help_text="Orden de visualización (0 primero, 1 después...).")
    is_active = models.BooleanField(_("Activo"), default=True, db_index=True, help_text="Marcar para que el componente sea visible en la página de inicio.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"[{self.get_component_type_display()}] {self.title}"
    class Meta:
        verbose_name = "Componente de Página de Inicio"
        verbose_name_plural = "Componentes de Página de Inicio"
        ordering = ['order']


class SiteConfiguration(models.Model):
    nombre_entidad_principal = models.CharField(_("Nombre de la Entidad Principal"), max_length=100, default='Alcaldía de', help_text="Primera línea del nombre de la entidad (ej. 'Alcaldía de')")
    nombre_entidad_secundaria = models.CharField(_("Nombre de la Entidad Secundaria"), max_length=100, default='Puerto Gaitán', help_text="Segunda línea del nombre de la entidad (ej. 'Puerto Gaitán')")
    nombre_secretaria = models.CharField(_("Nombre de la Secretaría"), max_length=150, blank=True, default="Secretaría de Turismo y Desarrollo Económico")
    nombre_direccion = models.CharField(_("Nombre de la Dirección"), max_length=150, blank=True, default="Dirección de Turismo")
    logo = models.FileField(_("Logo del Sitio"), upload_to=site_config_directory_path, blank=True, null=True, help_text="Logo principal que aparece en la cabecera. Preferiblemente en formato SVG.")

    direccion = models.CharField(_("Dirección"), max_length=255, blank=True)
    horario_atencion = models.CharField(_("Horario de Atención"), max_length=255, blank=True)
    telefono_conmutador = models.CharField(_("Teléfono Conmutador"), max_length=50, blank=True)
    telefono_movil = models.CharField(_("Teléfono Móvil"), max_length=50, blank=True)
    linea_gratuita = models.CharField(_("Línea de Atención Gratuita"), max_length=50, blank=True)
    linea_anticorrupcion = models.CharField(_("Línea Anticorrupción"), max_length=50, blank=True)
    correo_institucional = models.EmailField(_("Correo Institucional"), blank=True)
    correo_notificaciones = models.EmailField(_("Correo de Notificaciones Judiciales"), blank=True)
    social_facebook = models.URLField(_("Facebook URL"), blank=True)
    social_twitter = models.URLField(_("Twitter URL"), blank=True)
    social_youtube = models.URLField(_("YouTube URL"), blank=True)
    social_instagram = models.URLField(_("Instagram URL"), blank=True)
    seccion_publicaciones_activa = models.BooleanField(_("Sección de Publicaciones (Eventos/Noticias) Activa"), default=True, help_text="Marcar para mostrar la sección de publicaciones en el sitio web.")
    seccion_atractivos_activa = models.BooleanField(_("Sección de Atractivos Turísticos Activa"), default=True, help_text="Marcar para mostrar la sección de atractivos turísticos.")
    seccion_prestadores_activa = models.BooleanField(_("Sección de Prestadores de Servicios Activa"), default=True, help_text="Marcar para mostrar el directorio de prestadores de servicios.")
    google_maps_api_key = EncryptedTextField(_("Google Maps API Key"), blank=True, null=True, help_text="Clave de API de Google Maps para todo el sitio.")

    # --- Configuración de LLMs del Sistema ---
    groq_api_key = EncryptedTextField(_("Groq API Key"), blank=True, null=True, help_text="Clave de API para el proveedor Groq.")
    openai_api_key = EncryptedTextField(_("OpenAI API Key"), blank=True, null=True, help_text="Clave de API para el proveedor OpenAI.")
    google_api_key = EncryptedTextField(_("Google API Key"), blank=True, null=True, help_text="Clave de API para el proveedor Google (Gemini).")

    # --- Configuración del Router LLM ---
    llm_routing_token_threshold = models.PositiveIntegerField(
        _("Umbral de Tokens para Router LLM"),
        default=1500,
        help_text="Número de tokens en el historial de conversación para escalar al LLM avanzado (ej: Groq)."
    )

    def __str__(self):
        return "Configuración General del Sitio"
    def save(self, *args, **kwargs):
        self.pk = 1
        super(SiteConfiguration, self).save(*args, **kwargs)
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    class Meta:
        verbose_name = "Configuración del Sitio"
        verbose_name_plural = "Configuración del Sitio"


class MenuItem(models.Model):
    nombre = models.CharField(_("Nombre del Enlace"), max_length=100)
    url = models.CharField(_("URL o Ruta"), max_length=255, help_text="Ruta interna (ej: /quienes-somos) o URL completa (ej: https://...).")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name=_("Menú Padre"), help_text="Dejar en blanco si es un elemento del menú principal.")
    orden = models.PositiveIntegerField(default=0, db_index=True, help_text="Orden de aparición (0 primero, 1 después, etc.).")
    def __str__(self):
        if self.parent:
            return f"{self.parent.nombre} -> {self.nombre}"
        return self.nombre
    class Meta:
        verbose_name = "Elemento de Menú"
        verbose_name_plural = "Elementos de Menú"
        ordering = ['orden']


def hecho_historico_directory_path(instance, filename):
    return f'historia/{uuid.uuid4()}_{filename}'


class HechoHistorico(models.Model):
    ano = models.IntegerField(_("Año del Acontecimiento"))
    titulo = models.CharField(_("Título del Hecho"), max_length=200)
    descripcion = models.TextField(_("Descripción"))
    imagen = models.ImageField(_("Imagen Ilustrativa"), upload_to=hecho_historico_directory_path, blank=True, null=True, help_text="Imagen opcional para ilustrar el hecho histórico.")
    es_publicado = models.BooleanField(_("Publicado"), default=False, help_text="Marcar para que sea visible en la línea de tiempo pública.")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.ano}: {self.titulo}"
    class Meta:
        verbose_name = "Hecho Histórico"
        verbose_name_plural = "Hechos Históricos"
        ordering = ['ano']


from django.core.validators import MinValueValidator, MaxValueValidator

class Resena(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resenas_hechas')
    calificacion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], help_text="Calificación de 1 a 5 estrellas.")
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aprobada = models.BooleanField(default=False, help_text="Las reseñas deben ser aprobadas por un administrador para ser visibles.")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        return f"Reseña de {self.usuario.username} sobre {self.content_object} ({self.calificacion} estrellas)"
    class Meta:
        verbose_name = "Reseña y Calificación"
        verbose_name_plural = "Reseñas y Calificaciones"
        ordering = ['-fecha_creacion']
        unique_together = ('usuario', 'content_type', 'object_id')


class Sugerencia(models.Model):
    class TipoMensaje(models.TextChoices):
        SUGERENCIA = 'SUGERENCIA', _('Sugerencia')
        QUEJA = 'QUEJA', _('Queja')
        FELICITACION = 'FELICITACION', _('Felicitación')
    class Estado(models.TextChoices):
        RECIBIDO = 'RECIBIDO', _('Recibido')
        EN_REVISION = 'EN_REVISION', _('En Revisión')
        ATENDIDO = 'ATENDIDO', _('Atendido')
    nombre_remitente = models.CharField(max_length=150, blank=True, help_text="Nombre (si el usuario no está autenticado).")
    email_remitente = models.EmailField(blank=True, help_text="Email de contacto (si el usuario no está autenticado).")
    usuario = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='sugerencias_hechas')
    tipo_mensaje = models.CharField(max_length=20, choices=TipoMensaje.choices, default=TipoMensaje.SUGERENCIA)
    mensaje = models.TextField()
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.RECIBIDO)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    es_publico = models.BooleanField(default=False, help_text="Marcar si esta sugerencia/felicitación puede ser mostrada públicamente.")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        remitente = self.usuario.username if self.usuario else self.nombre_remitente or "Anónimo"
        return f"[{self.get_tipo_mensaje_display()}] de {remitente} - {self.fecha_envio.strftime('%Y-%m-%d')}"
    class Meta:
        verbose_name = "Sugerencia o Felicitación"
        verbose_name_plural = "Sugerencias y Felicitaciones"
        ordering = ['-fecha_envio']
# --------------------- Modelos de Formularios Dinámicos ---------------------

class Formulario(models.Model):
    """
    Define la estructura de un formulario dinámico que los administradores pueden crear.
    Este modelo consolida los campos encontrados en ambas ramas.
    """
    # nombre/título del formulario
    nombre = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255, blank=True, help_text="Campo opcional: título amigable. Si está vacío, se usará 'nombre'.")
    descripcion = models.TextField(blank=True)

    # Asociación genérica para vincular el formulario a cualquier modelo
    # (CategoriaPrestador, AtractivoTuristico, Artesano, etc.)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="El tipo de entidad al que se asocia este formulario."
    )
    object_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="El ID de la entidad específica a la que se asocia."
    )
    content_object = GenericForeignKey('content_type', 'object_id')

    # creador y permisos / visibilidad
    creado_por = models.ForeignKey(
        CustomUser if CustomUser else settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='formularios_creados',
        help_text="Usuario que creó el formulario (puede ser null si se importó/seed)."
    )
    es_publico = models.BooleanField(default=False, help_text="Indica si el formulario es visible para los prestadores.")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        display_title = self.titulo or self.nombre
        if self.content_object:
            return f"{display_title} (para {self.content_object})"
        return display_title

    class Meta:
        verbose_name = "Formulario Dinámico"
        verbose_name_plural = "Formularios Dinámicos"
        unique_together = ('nombre', 'content_type', 'object_id')


class Pregunta(models.Model):
    """
    Define una pregunta dentro de un formulario.
    """
    class TipoPregunta(models.TextChoices):
        TEXTO_CORTO = 'TEXTO_CORTO', 'Texto Corto'
        TEXTO_LARGO = 'TEXTO_LARGO', 'Texto Largo'
        NUMERO = 'NUMERO', 'Número'
        FECHA = 'FECHA', 'Fecha'
        SELECCION_UNICA = 'SELECCION_UNICA', 'Selección Única'
        SELECCION_MULTIPLE = 'SELECCION_MULTIPLE', 'Selección Múltiple'
        CHECKBOX = 'CHECKBOX', 'Casilla de Verificación (Sí/No)'
        EMAIL = 'EMAIL', 'Correo Electrónico'
        URL = 'URL', 'Enlace (URL)'

    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, related_name='preguntas')
    texto_pregunta = models.CharField(max_length=500)
    tipo_pregunta = models.CharField(max_length=50, choices=TipoPregunta.choices)
    es_requerida = models.BooleanField(default=False)
    orden = models.PositiveIntegerField(default=0, help_text="Orden de la pregunta en el formulario")
    ayuda = models.CharField(max_length=255, blank=True, help_text="Texto de ayuda/placeholder para quien responde")
    slug = models.SlugField(max_length=255, blank=True, help_text="Identificador único opcional para la pregunta (útil al guardar respuestas)")

    def __str__(self):
        return self.texto_pregunta

    class Meta:
        verbose_name = "Pregunta de Formulario"
        verbose_name_plural = "Preguntas de Formulario"
        ordering = ['orden']


class OpcionRespuesta(models.Model):
    """
    Define una opción para preguntas de selección única o múltiple.
    """
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto_opcion = models.CharField(max_length=255)
    orden = models.PositiveIntegerField(default=0, help_text="Orden de la opción en la pregunta")
    valor_interno = models.CharField(max_length=255, blank=True, help_text="Valor interno (opcional) para almacenamiento")

    def __str__(self):
        return self.texto_opcion

    class Meta:
        verbose_name = "Opción de Respuesta"
        verbose_name_plural = "Opciones de Respuesta"
        ordering = ['orden']


class RespuestaUsuario(models.Model):
    """
    Almacena la respuesta de un usuario a una pregunta específica de un formulario.
    Este modelo es genérico y se vincula directamente con el CustomUser.
    """
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='respuestas_formulario')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')

    # Campo unificado para la respuesta, utilizando JSON para flexibilidad.
    # Para respuestas simples (texto, número), se puede guardar como {"value": "respuesta"}.
    # Para selección múltiple, se puede guardar como {"values": [opcion1, opcion2]}.
    respuesta = models.JSONField(default=dict, help_text="Respuesta del usuario en formato JSON.")

    fecha_respuesta = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Respuesta de {self.usuario.username} a '{self.pregunta.texto_pregunta}'"

    class Meta:
        verbose_name = "Respuesta de Usuario a Formulario"
        verbose_name_plural = "Respuestas de Usuarios a Formularios"
        unique_together = ('usuario', 'pregunta')


# --------------------- Módulo de Verificación de Cumplimiento ---------------------

class PlantillaVerificacion(models.Model):
    """
    Una plantilla o checklist para un tipo específico de verificación.
    Ej: "Plantilla para Restaurantes", "Plantilla para Hoteles".
    """
    nombre = models.CharField(max_length=255, unique=True, help_text="Nombre único para la plantilla, ej: 'Verificación para Guías de Turismo'")
    descripcion = models.TextField(blank=True, help_text="Descripción detallada de la finalidad de esta plantilla.")
    categoria_prestador = models.ForeignKey(
        CategoriaPrestador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='plantillas_verificacion',
        help_text="Asocia esta plantilla a una categoría de prestador específica (opcional)."
    )
    creado_por = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='plantillas_creadas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Plantilla de Verificación"
        verbose_name_plural = "Plantillas de Verificación"
        ordering = ['nombre']

class ItemVerificacion(models.Model):
    """
    Un requisito o ítem individual dentro de una PlantillaVerificacion.
    Ej: "¿Cuenta con RNT vigente?", "¿Tiene extintores al día?".
    """
    plantilla = models.ForeignKey(PlantillaVerificacion, on_delete=models.CASCADE, related_name='items')
    texto_requisito = models.CharField(max_length=500, help_text="El texto del requisito a verificar.")
    puntaje = models.PositiveIntegerField(default=1, help_text="Puntos que otorga este ítem si se cumple.")
    orden = models.PositiveIntegerField(default=0, help_text="Orden del ítem en la plantilla.")
    es_obligatorio = models.BooleanField(default=True, help_text="Indica si este ítem es fundamental para la evaluación.")

    def __str__(self):
        return f"{self.texto_requisito} ({self.puntaje} pts)"

    class Meta:
        verbose_name = "Ítem de Verificación"
        verbose_name_plural = "Ítems de Verificación"
        ordering = ['orden']


class Verificacion(models.Model):
    """
    Una instancia de una verificación realizada a un prestador de servicios.
    Contiene la información general de la visita y el resultado.
    """
    plantilla_usada = models.ForeignKey(PlantillaVerificacion, on_delete=models.PROTECT, related_name='verificaciones_realizadas')
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='verificaciones_recibidas')
    funcionario_evaluador = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='verificaciones_realizadas',
        limit_choices_to={'role__in': [CustomUser.Role.ADMIN, CustomUser.Role.FUNCIONARIO_DIRECTIVO, CustomUser.Role.FUNCIONARIO_PROFESIONAL]}
    )
    fecha_visita = models.DateField(help_text="Fecha en que se realizó la visita de verificación.")
    puntaje_obtenido = models.PositiveIntegerField(default=0, help_text="Puntaje total calculado para esta verificación.")
    observaciones_generales = models.TextField(blank=True, help_text="Observaciones y comentarios del funcionario evaluador.")
    recomendaciones = models.TextField(blank=True, help_text="Recomendaciones para el prestador de servicios.")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Verificación a {self.prestador.nombre_negocio} el {self.fecha_visita}"

    class Meta:
        verbose_name = "Verificación de Cumplimiento"
        verbose_name_plural = "Verificaciones de Cumplimiento"
        ordering = ['-fecha_visita']

class RespuestaItemVerificacion(models.Model):
    """
    La respuesta específica a un ítem de verificación para una instancia de Verificacion.
    """
    verificacion = models.ForeignKey(Verificacion, on_delete=models.CASCADE, related_name='respuestas_items')
    item_original = models.ForeignKey(ItemVerificacion, on_delete=models.PROTECT, related_name='respuestas_dadas')
    cumple = models.BooleanField(default=False, help_text="Marcar si el prestador cumple con este requisito.")
    justificacion = models.CharField(max_length=255, blank=True, help_text="Justificación o número de soporte si es necesario (ej. N° de resolución).")

    def __str__(self):
        return f"Respuesta a '{self.item_original.texto_requisito}' para {self.verificacion.prestador.nombre_negocio}"

    class Meta:
        verbose_name = "Respuesta a Ítem de Verificación"
        verbose_name_plural = "Respuestas a Ítems de Verificación"
        unique_together = ('verificacion', 'item_original')

 # --------------------- Módulo de Capacitaciones ---------------------

class AsistenciaCapacitacion(models.Model):
    """
    Registra la asistencia de un usuario (Prestador o Artesano) a una capacitación.
    """
    capacitacion = models.ForeignKey(
        Publicacion,
        on_delete=models.CASCADE,
        related_name='asistentes',
        limit_choices_to={'tipo': Publicacion.Tipo.CAPACITACION}
    )
    usuario = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='asistencias_capacitaciones',
        limit_choices_to={'role__in': [CustomUser.Role.PRESTADOR, CustomUser.Role.ARTESANO]}
    )
    fecha_asistencia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Asistencia de {self.usuario.username} a {self.capacitacion.titulo}"

    class Meta:
        verbose_name = "Asistencia a Capacitación"
        verbose_name_plural = "Asistencias a Capacitaciones"
        unique_together = ('capacitacion', 'usuario')

# --------------------- Módulo de Puntuación ---------------------

class ScoringRule(models.Model):
    """
    Singleton para almacenar las reglas de puntuación del sistema.
    Permite a los administradores gestionar los valores desde el panel.
    """
    puntos_asistencia_capacitacion = models.PositiveIntegerField(default=10, help_text="Puntos otorgados por cada asistencia a una capacitación.")
    puntos_por_estrella_reseña = models.PositiveIntegerField(default=2, help_text="Puntos a multiplicar por cada estrella en una reseña aprobada (ej. 5 estrellas = 5 * 2 = 10 puntos).")
    puntos_completar_formulario = models.PositiveIntegerField(default=5, help_text="Puntos otorgados por cada formulario de caracterización completado.")

    def __str__(self):
        return "Reglas de Puntuación del Sistema"

    def save(self, *args, **kwargs):
        self.pk = 1
        super(ScoringRule, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        verbose_name = "Reglas de Puntuación"
        verbose_name_plural = "Reglas de Puntuación"


# --------------------- Módulo de Notificaciones ---------------------

class Notificacion(models.Model):
    """
    Representa una notificación para un usuario dentro del sistema.
    """
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notificaciones', help_text="El usuario que recibe la notificación.")
    mensaje = models.CharField(max_length=255, help_text="El texto de la notificación.")
    leido = models.BooleanField(default=False, db_index=True, help_text="Indica si el usuario ha leído la notificación.")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Enlace opcional para redirigir al usuario al hacer clic
    url = models.CharField(max_length=500, blank=True, null=True, help_text="URL a la que se redirige al hacer clic.")

    # Relación genérica para vincular la notificación a un objeto específico (ej. una Publicacion)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Notificación para {self.usuario.username}: {self.mensaje[:30]}..."

    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"
        ordering = ['-fecha_creacion']

# --- Modelos de Turismo API ---
class VacanteEmpleo(models.Model):
    titulo_vacante = models.CharField(max_length=255)
    descripcion = models.TextField()
    requisitos = models.TextField(blank=True, null=True)
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, blank=True, null=True)
    nombre_empleador_alternativo = models.CharField(max_length=255, blank=True, null=True)
    tipo_contrato = models.CharField(max_length=100, blank=True, null=True)
    salario_rango = models.CharField(max_length=100, blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    activa = models.BooleanField(default=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    publicada_por_usuario = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.titulo_vacante

class TuristaRegistro(models.Model):
    fecha_encuesta = models.DateField()
    nombre_turista = models.CharField(max_length=255, blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    rango_edad = models.CharField(max_length=50, blank=True, null=True)
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    pais_residencia = models.CharField(max_length=100, blank=True, null=True)
    depto_origen = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True, related_name='turistas_depto_origen')
    municipio_origen = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True, related_name='turistas_origen')
    motivo_viaje = models.CharField(max_length=255, blank=True, null=True)
    otro_motivo_viaje = models.CharField(max_length=255, blank=True, null=True)
    municipio_encuestado = models.ForeignKey(Municipio, on_delete=models.PROTECT, related_name='encuestas_realizadas')
    registrado_por_usuario = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)

class EncuestaPercepcion(models.Model):
    turista_registro = models.OneToOneField(TuristaRegistro, on_delete=models.CASCADE, primary_key=True)
    volveria = models.IntegerField(blank=True, null=True)
    experiencia_general_positiva = models.IntegerField(blank=True, null=True)
    fecha_valoracion = models.DateTimeField(auto_now_add=True)

class DiagnosticoTerritorial(models.Model):
    municipio = models.OneToOneField(Municipio, on_delete=models.CASCADE, primary_key=True)
    anio_diagnostico = models.IntegerField()
    dimension_1_infraestructura = models.FloatField(blank=True, null=True)
    dimension_2_sostenibilidad = models.FloatField(blank=True, null=True)
    resultado_total = models.FloatField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    registrado_por_usuario = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)

class IniciativaTuristica(models.Model):
    nombre_iniciativa = models.CharField(max_length=255)
    tipo_iniciativa = models.CharField(max_length=100, blank=True, null=True) # Plan, Programa, Proyecto
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True) # Formulación, Ejecución, Terminado
    presupuesto = models.FloatField(blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre_iniciativa

class EventoTuristico(models.Model):
    nombre_evento = models.CharField(max_length=255)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    publicado = models.BooleanField(default=False)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre_evento

class RecursoReservable(models.Model):
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE)
    nombre_recurso = models.CharField(max_length=255)
    tipo_recurso = models.CharField(max_length=100) # Ej: Habitación, Tour, Mesa
    capacidad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.FloatField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_recurso} ({self.empresa.nombre_negocio})"

class LegacyReserva(models.Model):
    recurso = models.ForeignKey(RecursoReservable, on_delete=models.PROTECT)
    cliente = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=100) # Ej: Confirmada, Cancelada, Completada
    monto_final = models.FloatField(blank=True, null=True)
    promocion = models.ForeignKey('Promocion', on_delete=models.SET_NULL, blank=True, null=True)

class Promocion(models.Model):
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE)
    codigo_promocion = models.CharField(max_length=50, unique=True, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo_descuento = models.CharField(max_length=50) # "porcentaje" o "fijo"
    valor_descuento = models.FloatField()
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

class Pago(models.Model):
    reserva = models.ForeignKey(LegacyReserva, on_delete=models.CASCADE)
    monto = models.FloatField()
    metodo_pago = models.CharField(max_length=100, blank=True, null=True)
    estado_pago = models.CharField(max_length=100, blank=True, null=True)
    fecha_pago = models.DateTimeField(auto_now_add=True)

class ReglaPrecio(models.Model):
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE)
    nombre_regla = models.CharField(max_length=255)
    tipo_regla = models.CharField(max_length=100) # "temporada", "dia_semana", "demanda"
    valor_ajuste = models.FloatField() # Puede ser un porcentaje (ej. 1.2 para +20%) o un monto fijo
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    dias_semana = models.CharField(max_length=20, blank=True, null=True) # "1,2,3,4,5" para L-V

    def __str__(self):
        return self.nombre_regla

class RestauranteMesa(models.Model):
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE)
    nombre_mesa = models.CharField(max_length=100) # Ej: "Mesa 5", "Barra 1"
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=50) # "Libre", "Ocupada", "Reservada"

    def __str__(self):
        return self.nombre_mesa

class RestauranteMenuProducto(models.Model):
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField()
    categoria = models.CharField(max_length=100, blank=True, null=True) # "Entradas", "Platos Fuertes", "Bebidas"
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_producto

class RestaurantePedido(models.Model):
    mesa = models.ForeignKey(RestauranteMesa, on_delete=models.PROTECT)
    mesero = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    estado = models.CharField(max_length=50) # "Abierto", "Enviado a Cocina", "Cerrado"
    total = models.FloatField(blank=True, null=True)
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)

class RestaurantePedidoItem(models.Model):
    pedido = models.ForeignKey(RestaurantePedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(RestauranteMenuProducto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    estado = models.CharField(max_length=50) # "Pedido", "En Preparación", "Entregado"
    notas = models.TextField(blank=True, null=True)

class AgenciaPaquete(models.Model):
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE)
    nombre_paquete = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio_total = models.FloatField()
    duracion_dias = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_paquete

class PaqueteServicio(models.Model):
    paquete = models.ForeignKey(AgenciaPaquete, on_delete=models.CASCADE)
    tipo_servicio = models.CharField(max_length=100) # "hotel", "tour", "transporte"
    id_servicio_especifico = models.IntegerField()
    descripcion_servicio = models.TextField(blank=True, null=True)

class AgenciaReservaPaquete(models.Model):
    paquete = models.ForeignKey(AgenciaPaquete, on_delete=models.PROTECT)
    cliente = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    fecha_inicio = models.DateField()
    numero_personas = models.IntegerField()
    estado = models.CharField(max_length=50) # "Confirmada", "Cancelada", "Completada"

class GuiaPerfil(models.Model):
    guia = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    idiomas = models.CharField(max_length=255, blank=True, null=True) # "Español,Inglés"
    especialidades = models.CharField(max_length=255, blank=True, null=True) # "Historia,Naturaleza"
    certificaciones = models.TextField(blank=True, null=True)
    tarifa_por_hora = models.FloatField(blank=True, null=True)

class GuiaDisponibilidad(models.Model):
    guia = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha = models.DateField()
    disponible = models.BooleanField(default=True)

class GuiaReservaTour(models.Model):
    guia = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='tours_guiados')
    cliente = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='tours_contratados')
    fecha_hora_inicio = models.DateTimeField()
    duracion_horas = models.IntegerField()
    estado = models.CharField(max_length=50) # "Solicitada", "Confirmada", "Cancelada"

class InventarioTipoItem(models.Model):
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE)
    nombre_tipo = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    stock_minimo_deseado = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre_tipo

class InventarioItemIndividual(models.Model):
    tipo_item = models.ForeignKey(InventarioTipoItem, on_delete=models.CASCADE)
    estado = models.CharField(max_length=100)
    fecha_compra = models.DateField(blank=True, null=True)
    veces_usado = models.IntegerField(default=0)
    fecha_ultimo_mantenimiento = models.DateField(blank=True, null=True)
    notas_mantenimiento = models.TextField(blank=True, null=True)

class ProductoEventoEmpresa(models.Model):
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=50) # 'Producto' o 'Evento'
    precio = models.FloatField(blank=True, null=True)
    fecha_evento = models.DateField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class RegistroCliente(models.Model):
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE)
    nacionalidad = models.CharField(max_length=50) # 'Nacional' o 'Extranjero'
    cantidad = models.IntegerField(default=1)
    fecha_registro = models.DateField()

# --- Modelos del Plan de Desarrollo ---

class DireccionMunicipalDeTurismo(models.Model):
    nombre = models.CharField(max_length=255)
    municipio = models.OneToOneField(Municipio, on_delete=models.CASCADE)
    funcionarios_asignados = models.ManyToManyField(CustomUser, blank=True)

    def __str__(self):
        return self.nombre

class DireccionDepartamentalDeTurismo(models.Model):
    nombre = models.CharField(max_length=255)
    departamento = models.OneToOneField(Departamento, on_delete=models.CASCADE)
    dependencias_municipales = models.ManyToManyField(DireccionMunicipalDeTurismo, blank=True)

    def __str__(self):
        return self.nombre

class ServicioTuristico(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='servicios')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.TextField(blank=True, help_text="Ej: 'Lunes a Viernes de 9am a 5pm'")

    class Meta:
        verbose_name = "Servicio Turístico"
        verbose_name_plural = "Servicios Turísticos"

    def __str__(self):
        return f"{self.nombre} - {self.prestador.nombre_negocio}"

class Booking(models.Model):
    servicio = models.ForeignKey(ServicioTuristico, on_delete=models.CASCADE, related_name='bookings')
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings_realizadas')
    fecha_reserva = models.DateTimeField()
    cantidad_personas = models.PositiveIntegerField(default=1)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class EstadoReserva(models.TextChoices):
        PENDIENTE = "PENDIENTE", _("Pendiente")
        CONFIRMADA = "CONFIRMADA", _("Confirmada")
        CANCELADA = "CANCELADA", _("Cancelada")
        COMPLETADA = "COMPLETADA", _("Completada")

    estado = models.CharField(max_length=20, choices=EstadoReserva.choices, default=EstadoReserva.PENDIENTE)

    def __str__(self):
        return f"Booking de {self.cliente.username} para {self.servicio.nombre} el {self.fecha_reserva}"

class Factura(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='factura')
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='facturas_emitidas')
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='facturas_recibidas')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateTimeField(auto_now_add=True)

    class MetodoPago(models.TextChoices):
        EFECTIVO = "EFECTIVO", _("Efectivo")
        TARJETA = "TARJETA", _("Tarjeta de Crédito/Débito")
        TRANSFERENCIA = "TRANSFERENCIA", _("Transferencia Bancaria")

    metodo_pago = models.CharField(max_length=20, choices=MetodoPago.choices)

    def __str__(self):
        return f"Factura {self.id} para {self.cliente.username}"

class Empleado(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='perfil_empleado')
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='empleados')
    cargo = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.cargo}"

class Nomina(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='nominas')
    periodo_pago_inicio = models.DateField()
    periodo_pago_fin = models.DateField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    deducciones = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonificaciones = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()

    def __str__(self):
        return f"Nómina de {self.empleado} para {self.periodo_pago_inicio} a {self.periodo_pago_fin}"

class ReporteSGSST(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='reportes_sgsst')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_reporte = models.DateField()
    acciones_correctivas = models.TextField(blank=True)

    class EstadoReporte(models.TextChoices):
        ABIERTO = "ABIERTO", _("Abierto")
        EN_PROGRESO = "EN_PROGRESO", _("En Progreso")
        CERRADO = "CERRADO", _("Cerrado")

    estado = models.CharField(max_length=20, choices=EstadoReporte.choices, default=EstadoReporte.ABIERTO)

    def __str__(self):
        return f"Reporte SG-SST: {self.titulo} - {self.prestador.nombre_negocio}"