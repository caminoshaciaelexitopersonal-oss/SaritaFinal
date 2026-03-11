# from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
# from apps.prestadores.models import CategoriaPrestador
from .models import (
    CustomUser, ImagenGaleria, ImagenArtesano, Publicacion,
    ConsejoConsultivo, AtractivoTuristico, ImagenAtractivo, RutaTuristica, ImagenRutaTuristica, ElementoGuardado, ContentType,
    Video, ContenidoMunicipio, AgentTask, SiteConfiguration, MenuItem,
    HomePageComponent, AuditLog, PaginaInstitucional, ImagenPaginaInstitucional, HechoHistorico, Artesano, RubroArtesano,
    Resena, Sugerencia, ScoringRule, Notificacion,
    Formulario, Pregunta, OpcionRespuesta, RespuestaUsuario,
    PlantillaVerificacion, TipoDocumentoVerificacion, DocumentoVerificacion,
    ItemVerificacion,
    Verificacion,
    RespuestaItemVerificacion,
    AsistenciaCapacitacion,
    PerfilAdministrador,
    PerfilFuncionarioDirectivo,
    PerfilFuncionarioProfesional,
    UserLLMConfig,
    Department,
    Municipality,
    Entity,
    Profile
)
from django.db import transaction
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
# from apps.prestadores.mi_negocio.serializers.productos import ProductoSerializer
# from apps.turismo.serializers import RutaTuristicaSerializer

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ['id', 'name', 'slug']

class EntityAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ['name', 'logo', 'primary_color', 'settings']

class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ['id', 'name']

class DepartmentSerializer(serializers.ModelSerializer):
    municipalities = MunicipalitySerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'municipalities']


# --- Serializadores para Formularios Dinámicos ---

class OpcionRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcionRespuesta
        fields = ['id', 'texto_opcion', 'orden']


class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionRespuestaSerializer(many=True, read_only=True)

    class Meta:
        model = Pregunta
        fields = ['id', 'texto_pregunta', 'tipo_pregunta', 'es_requerida', 'orden', 'ayuda', 'slug', 'opciones']


class FormularioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = ['id', 'titulo', 'descripcion', 'es_publico']


class FormularioDetailSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True, read_only=True)

    class Meta:
        model = Formulario
        fields = ['id', 'titulo', 'descripcion', 'es_publico', 'preguntas']


class RespuestaUsuarioSerializer(serializers.ModelSerializer):
    pregunta_texto = serializers.CharField(source='pregunta.texto_pregunta', read_only=True)
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = RespuestaUsuario
        fields = ['id', 'pregunta', 'pregunta_texto', 'usuario_username', 'respuesta', 'fecha_respuesta']


class RespuestaUsuarioCreateSerializer(serializers.Serializer):
    respuestas = serializers.DictField(
        child=serializers.JSONField(),
        help_text="Diccionario con `pregunta_id` como clave y la respuesta como valor."
    )
    formulario_id = serializers.IntegerField()

    def validate(self, data):
        formulario_id = data.get('formulario_id')
        respuestas_data = data.get('respuestas', {})
        try:
            formulario = Formulario.objects.prefetch_related('preguntas').get(id=formulario_id)
        except Formulario.DoesNotExist:
            raise serializers.ValidationError({"formulario_id": "El formulario especificado no existe."})
        preguntas_requeridas = {p.id: p for p in formulario.preguntas.filter(es_requerida=True)}
        for pregunta_id, pregunta in preguntas_requeridas.items():
            respuesta = respuestas_data.get(str(pregunta_id))
            if respuesta is None or (isinstance(respuesta, str) and not respuesta.strip()) or (isinstance(respuesta, list) and not respuesta):
                raise serializers.ValidationError({
                    "respuestas": f"Falta una respuesta para la pregunta requerida: '{pregunta.texto_pregunta}' (ID: {pregunta_id})."
                })
        data['formulario'] = formulario
        return data

    @transaction.atomic
    def save(self, **kwargs):
        formulario = self.validated_data['formulario']
        respuestas_data = self.validated_data['respuestas']
        usuario = self.context['request'].user
        preguntas_del_formulario = {str(p.id): p for p in formulario.preguntas.all()}
        for pregunta_id_str, respuesta_valor in respuestas_data.items():
            if pregunta_id_str in preguntas_del_formulario:
                pregunta = preguntas_del_formulario[pregunta_id_str]
                respuesta_json = respuesta_valor
                RespuestaUsuario.objects.update_or_create(
                    usuario=usuario,
                    pregunta=pregunta,
                    defaults={'respuesta': respuesta_json}
                )
        return {"status": "success", "message": "Respuestas guardadas correctamente."}


class HechoHistoricoSerializer(serializers.ModelSerializer):
    imagen_url = serializers.ImageField(source='imagen', read_only=True)
    class Meta:
        model = HechoHistorico
        fields = ['id', 'ano', 'titulo', 'descripcion', 'imagen', 'imagen_url', 'es_publicado']
        extra_kwargs = {'imagen': {'write_only': True, 'required': False}}


class GaleriaItemSerializer(serializers.Serializer):
    id = serializers.CharField()
    tipo = serializers.CharField()
    url = serializers.URLField()
    thumbnail_url = serializers.URLField()
    titulo = serializers.CharField()
    descripcion = serializers.CharField(required=False, allow_blank=True)


class ImagenPaginaInstitucionalSerializer(serializers.ModelSerializer):
    imagen_url = serializers.ImageField(source='imagen', read_only=True)
    class Meta:
        model = ImagenPaginaInstitucional
        fields = ['id', 'imagen_url', 'alt_text', 'orden']


class PaginaInstitucionalSerializer(serializers.ModelSerializer):
    banner_url = serializers.ImageField(source='banner', read_only=True)
    actualizado_por_username = serializers.CharField(source='actualizado_por.username', read_only=True)
    galeria_imagenes = ImagenPaginaInstitucionalSerializer(many=True, read_only=True)

    class Meta:
        model = PaginaInstitucional
        fields = [
            'id', 'nombre', 'slug', 'titulo_banner', 'subtitulo_banner',
            'banner', 'banner_url', 'contenido_principal', 'programas_proyectos',
            'estrategias_apoyo', 'politicas_locales', 'convenios_asociaciones',
            'informes_resultados', 'actualizado_por_username', 'fecha_actualizacion',
            'galeria_imagenes'
        ]
        extra_kwargs = {'banner': {'write_only': True, 'required': False}}


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'email', 'role')

class UsuarioListSerializer(serializers.ModelSerializer):
    nombre_display = serializers.SerializerMethodField()
    rol_display = serializers.CharField(source='get_role_display', read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'nombre_display', 'role', 'rol_display']
    def get_nombre_display(self, obj):
        if hasattr(obj, 'perfil_prestador') and obj.perfil_prestador.nombre_negocio:
            return obj.perfil_prestador.nombre_negocio
        return obj.get_full_name() or obj.username


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance


# --------------------- Módulo de Puntuación ---------------------

class ScoringRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoringRule
        fields = '__all__'


class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = ['id', 'mensaje', 'leido', 'fecha_creacion', 'url']


# --- Serializador para la Configuración de IA del Usuario ---

class UserLLMConfigSerializer(serializers.ModelSerializer):
    """
    Serializer para que los usuarios gestionen su propia configuración de LLM.
    La clave API se enmascara para la lectura y es de solo escritura.
    """
    api_key = serializers.CharField(
        write_only=True,
        required=False,
        allow_blank=True,
        style={'input_type': 'password'},
        help_text="Proporcione su clave de API. No se mostrará después de guardarla."
    )
    provider_display = serializers.CharField(source='get_provider_display', read_only=True)
    api_key_saved = serializers.SerializerMethodField()

    class Meta:
        model = UserLLMConfig
        fields = [
            'provider',
            'provider_display',
            'api_key',
            'api_key_saved',
            'updated_at'
        ]
        read_only_fields = ['updated_at']

    def get_api_key_saved(self, instance):
        """Devuelve true si la clave API tiene un valor guardado."""
        return bool(instance.api_key and instance.api_key.value)

    def to_representation(self, instance):
        """Añade las opciones de proveedor para facilitar el renderizado en el frontend."""
        representation = super().to_representation(instance)
        representation['provider_options'] = [
            {'value': choice[0], 'label': choice[1]}
            for choice in UserLLMConfig.Provider.choices
        ]
        return representation

    def update(self, instance, validated_data):
        """
        Si la api_key no se envía en la petición o está vacía,
        se mantiene el valor existente en la base de datos.
        """
        # Si la clave no está en los datos, o es una cadena vacía, no la actualizamos.
        if 'api_key' not in validated_data or not validated_data.get('api_key'):
            validated_data.pop('api_key', None)

        return super().update(instance, validated_data)


class ProviderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProfile
        fields = ('id', 'nombre_comercial', 'provider_type', 'is_verified')


class ArtesanoForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artesano
        fields = ('id', 'nombre_taller', 'aprobado')


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializador polimórfico que puede manejar diferentes tipos de perfiles de usuario.
    """
    perfil_prestador = ProviderProfileSerializer(read_only=True, source='user.perfil_prestador')
    perfil_artesano = ArtesanoForUserSerializer(read_only=True, source='user.perfil_artesano')
    # Añadir otros perfiles aquí (ej. perfil_turista) si existen

    class Meta:
        model = Profile
        fields = ('department', 'municipality', 'perfil_prestador', 'perfil_artesano')


class CustomUserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'email', 'role', 'profile')

class AdminPrestadorSerializer(serializers.ModelSerializer):
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = ProviderProfile
        fields = ('id', 'nombre_comercial', 'usuario_username', 'categoria_nombre')


class CustomLoginSerializer(LoginSerializer):
    """
    Serializador de Login personalizado para permitir iniciar sesión
    con email como 'username'.
    """
    username = None

class CustomRegisterSerializer(RegisterSerializer):
    """
    Serializador de Registro personalizado para eliminar el requisito de 'username'.
    El 'username' se autogenerará a partir del email.
    """
    username = None

    def get_cleaned_data(self):
        # Sobrescribimos para asegurar que no se pida el username
        data = super().get_cleaned_data()
        data.pop('username', None)
        return data

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.username = self.validated_data.get('email', '')
        user.save()
        return user

from rest_framework.authtoken.models import Token
from rest_framework import serializers

class CustomTokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
    user = CustomUserDetailSerializer(read_only=True)
