from rest_framework import generics, views, viewsets, status, mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# from dj_rest_auth.registration.views import RegisterView
import asyncio
import threading
from django.contrib.contenttypes.models import ContentType
from django.db import models, transaction
from django.utils import timezone
from asgiref.sync import async_to_sync
import json
from datetime import datetime, timedelta
from itertools import groupby
from operator import attrgetter
from django.db.models.functions import TruncDay
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .models import (
    CustomUser,
    # CategoriaPrestador fue movido a gestion_operativa
    ImagenGaleria,
    ImagenArtesano,
    Publicacion,
    ConsejoConsultivo,
    AtractivoTuristico,
    RutaTuristica,
    ElementoGuardado,
    Video,
    ContenidoMunicipio,
    AgentTask,
    SiteConfiguration,
    MenuItem,
    HomePageComponent,
    AuditLog,
    PaginaInstitucional,
    ImagenAtractivo,
    Artesano,
    RubroArtesano,
    Resena,
    Sugerencia,
    HechoHistorico,
    ScoringRule,
    Notificacion,
    Formulario,
    Pregunta,
    OpcionRespuesta,
    RespuestaUsuario,
    PlantillaVerificacion,
    ItemVerificacion,
    Verificacion,
    RespuestaItemVerificacion,
    AsistenciaCapacitacion,
    TipoDocumentoVerificacion,
    DocumentoVerificacion
)
from .serializers import (
    GaleriaItemSerializer,
    PaginaInstitucionalSerializer,
    ScoringRuleSerializer,
    NotificacionSerializer,
    ArtesanoSerializer,
    ArtesanoUpdateSerializer,
    ImagenGaleriaSerializer,
    ImagenArtesanoSerializer,
    DocumentoVerificacionSerializer,
    TipoDocumentoVerificacionSerializer,
    PublicacionListSerializer,
    PublicacionDetailSerializer,
    VideoSerializer,
    ConsejoConsultivoSerializer,
    AtractivoTuristicoListSerializer,
    AtractivoTuristicoDetailSerializer,
    AtractivoTuristicoWriteSerializer,
    RutaTuristicaListSerializer,
    RutaTuristicaDetailSerializer,
    LocationSerializer,
    ElementoGuardadoSerializer,
    ElementoGuardadoCreateSerializer,
    RubroArtesanoSerializer,
    ArtesanoPublicListSerializer,
    ArtesanoPublicDetailSerializer,
    AdminArtesanoListSerializer,
    AdminArtesanoDetailSerializer,
    UsuarioListSerializer,
    ContenidoMunicipioSerializer,
    AgentCommandSerializer,
    AgentTaskSerializer,
    UserLLMConfigSerializer,
    SiteConfigurationSerializer,
    MenuItemSerializer,
    AdminUserSerializer,
    HomePageComponentSerializer,
    AuditLogSerializer,
    AdminPublicacionSerializer,
    HechoHistoricoSerializer,
    ResenaSerializer,
    ResenaCreateSerializer,
    SugerenciaSerializer,
    SugerenciaAdminSerializer,
    FeedbackProveedorSerializer,
    FelicitacionPublicaSerializer,
    FormularioListSerializer,
    FormularioDetailSerializer,
    PreguntaSerializer,
    OpcionRespuestaSerializer,
    RespuestaUsuarioSerializer,
    RespuestaUsuarioCreateSerializer,
    # PlantillaVerificacionListSerializer,
    # PlantillaVerificacionDetailSerializer,
    # VerificacionListSerializer,
    # VerificacionDetailSerializer,
    # IniciarVerificacionSerializer,
    # GuardarVerificacionSerializer,
    CapacitacionDetailSerializer,
    RegistrarAsistenciaSerializer,
)
from django.utils import timezone
from datetime import timedelta
from .permissions import (
    IsTurista,
    IsAdminOrFuncionario,
    IsAdmin,
    IsAdminOrFuncionarioForUserManagement,
    IsPrestador,
    IsAnyAdminOrDirectivo,
    CanManageAtractivos,
    IsPrestadorOwner
)
# from apps.turismo.models import Reserva
# from apps.prestadores.mi_negocio.modelos.clientes import Cliente
from .filters import AuditLogFilter
from .serializers import DepartmentSerializer, MunicipalitySerializer, EntitySerializer, EntityAdminSerializer
from .models import Department, Municipality, Entity
from .permissions import IsEntityAdmin

class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing departments.
    """
    queryset = Department.objects.all().prefetch_related('municipality_set')
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]

class MunicipalityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing municipalities.
    Can be filtered by department.
    """
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department']


class EntityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing entities.
    """
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = [AllowAny]
class CurrentEntityView(generics.RetrieveAPIView):
    """
    Devuelve la entidad actual basada en el subdominio.
    """
    serializer_class = EntitySerializer
    permission_classes = [AllowAny]

    def get_object(self):
        # El middleware ya ha adjuntado la entidad a la petición.
        # Si no se encuentra ninguna entidad, request.entity será None.
        if not hasattr(self.request, 'entity') or not self.request.entity:
            return None
        return self.request.entity


class EntityAdminView(generics.RetrieveUpdateAPIView):
    """
    Vista para que un Admin de Entidad gestione su propia entidad.
    """
    queryset = Entity.objects.all()
    serializer_class = EntityAdminSerializer
    permission_classes = [IsEntityAdmin]

    def get_object(self):
        # Devuelve la entidad asociada al perfil del usuario.
        # El permiso IsEntityAdmin ya asegura que el perfil y la entidad existen.
        return self.request.user.profile.entity


class FormularioViewSet(viewsets.ModelViewSet):
    queryset = Formulario.objects.all().prefetch_related('preguntas__opciones')
    def get_serializer_class(self):
        if self.action == 'list':
            return FormularioListSerializer
        return FormularioDetailSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAnyAdminOrDirectivo]
        return super().get_permissions()
    def get_queryset(self):
        user = self.request.user
        if not user.is_staff and not user.is_superuser:
            return self.queryset.filter(es_publico=True)
        return self.queryset

class TipoDocumentoVerificacionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para listar los tipos de documentos que se pueden subir.
    """
    queryset = TipoDocumentoVerificacion.objects.filter(activo=True)
    serializer_class = TipoDocumentoVerificacionSerializer
    permission_classes = [IsAuthenticated] # Disponible para cualquier usuario autenticado

class ElementoGuardadoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsTurista]
    def get_queryset(self):
        return ElementoGuardado.objects.filter(usuario=self.request.user)
    def get_serializer_class(self):
        if self.action == 'create':
            return ElementoGuardadoCreateSerializer
        return ElementoGuardadoSerializer
    def get_serializer_context(self):
        return {'request': self.request}

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all().order_by('-fecha_creacion')

    def get_serializer_class(self):
        if self.action == 'create':
            return ResenaCreateSerializer
        return ResenaSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminOrFuncionario]
        return super().get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            queryset = queryset.filter(aprobada=True)
            content_type_str = self.request.query_params.get('content_type')
            object_id_str = self.request.query_params.get('object_id')
            if content_type_str and object_id_str:
                model_map = {'artesano': Artesano}
                Model = model_map.get(content_type_str.lower())
                if Model:
                    try:
                        content_type = ContentType.objects.get_for_model(Model)
                        queryset = queryset.filter(content_type=content_type, object_id=object_id_str)
                    except ContentType.DoesNotExist:
                        return queryset.none()
        return queryset

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=True, methods=['post'], permission_classes=[IsAdminOrFuncionario])
    def approve(self, request, pk=None):
        resena = self.get_object()
        resena.aprobada = True
        resena.save(update_fields=['aprobada'])
        return Response({'status': 'Reseña aprobada con éxito.'}, status=status.HTTP_200_OK)

class FelicitacionesPublicasView(generics.ListAPIView):
    queryset = Sugerencia.objects.filter(
        tipo_mensaje=Sugerencia.TipoMensaje.FELICITACION,
        es_publico=True
    ).order_by('-fecha_envio')
    serializer_class = FelicitacionPublicaSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class SugerenciaViewSet(viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Sugerencia.objects.all()
    serializer_class = SugerenciaSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(usuario=self.request.user)
        else:
            serializer.save()

class SugerenciaAdminViewSet(viewsets.ModelViewSet):
    queryset = Sugerencia.objects.all().order_by('-fecha_envio')
    serializer_class = SugerenciaAdminSerializer
    permission_classes = [IsAdminOrFuncionario]
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['mensaje', 'nombre_remitente', 'email_remitente', 'usuario__username']
    ordering_fields = ['fecha_envio', 'estado', 'tipo_mensaje']

# Minimal ViewSets to fix startup errors
class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [IsAuthenticated]

class AtractivoTuristicoViewSet(viewsets.ModelViewSet):
    queryset = AtractivoTuristico.objects.all()
    serializer_class = AtractivoTuristicoListSerializer
    permission_classes = [AllowAny]

class RutaTuristicaViewSet(viewsets.ModelViewSet):
    queryset = RutaTuristica.objects.all()
    serializer_class = RutaTuristicaListSerializer
    permission_classes = [AllowAny]

class HechoHistoricoViewSet(viewsets.ModelViewSet):
    queryset = HechoHistorico.objects.all()
    serializer_class = HechoHistoricoSerializer
    permission_classes = [AllowAny]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdmin]  # Solo los admins pueden modificar el menú

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        # 1. Obtener todos los items en una sola consulta para eficiencia.
        all_items = self.get_queryset().order_by('orden')

        # 2. Construir un diccionario para acceder fácilmente a cada item por su ID.
        items_map = {item.id: item for item in all_items}

        # 3. Construir el árbol: adjuntar cada item a su padre.
        root_items = []
        for item in all_items:
            # Inicializar un atributo 'children' para evitar errores si no tiene hijos.
            if not hasattr(item, 'children_data'):
                item.children_data = []

            if item.parent_id:
                parent = items_map.get(item.parent_id)
                if parent:
                    # Inicializar 'children_data' en el padre si no existe.
                    if not hasattr(parent, 'children_data'):
                        parent.children_data = []
                    parent.children_data.append(item)
            else:
                # Si no tiene padre, es un item raíz.
                root_items.append(item)

        # 4. Serializar solo los items raíz. El serializador se encargará de los hijos.
        serializer = self.get_serializer(root_items, many=True)
        return Response({'count': len(serializer.data), 'next': None, 'previous': None, 'results': serializer.data})

    @action(detail=False, methods=['post'])
    @transaction.atomic
    def reorder(self, request, *args, **kwargs):
        # El test envía una lista de diccionarios, cada uno con 'id' y 'children'
        def process_level(items, parent=None):
            for index, item_data in enumerate(items):
                item_id = item_data.get('id')
                # Asegurarse de que el item existe antes de intentar actualizarlo
                try:
                    menu_item = MenuItem.objects.get(pk=item_id)
                    menu_item.orden = index
                    menu_item.parent = parent
                    menu_item.save()

                    if 'children' in item_data and item_data['children']:
                        process_level(item_data['children'], parent=menu_item)
                except MenuItem.DoesNotExist:
                    # Si un item no existe, simplemente lo ignoramos para no romper la transacción
                    continue

        process_level(request.data)
        return Response({'status': 'Menú reordenado con éxito'})

class ContenidoMunicipioViewSet(viewsets.ModelViewSet):
    queryset = ContenidoMunicipio.objects.all()
    serializer_class = ContenidoMunicipioSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminOrFuncionario()]
        return [AllowAny()]

class PaginaInstitucionalViewSet(viewsets.ModelViewSet):
    queryset = PaginaInstitucional.objects.all()
    serializer_class = PaginaInstitucionalSerializer
    permission_classes = [AllowAny]

from django.db.models import Q
from dj_rest_auth.views import UserDetailsView

# from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from .serializers import AdminPrestadorSerializer

class CustomUserDetailsView(UserDetailsView):
    """
    Sobrescribe la UserDetailsView de dj-rest-auth para optimizar la consulta
    del usuario y sus perfiles asociados.
    """
    def get_queryset(self):
        # Utiliza select_related para traer los perfiles en una sola consulta
        return CustomUser.objects.select_related(
            'profile',
            'perfil_prestador',
            'perfil_artesano'
        )

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminOrFuncionarioForUserManagement]

    def get_queryset(self):
        user = self.request.user
        queryset = CustomUser.objects.all().order_by('pk') # Añadir ordenamiento

        if user.role == CustomUser.Role.ADMIN:
            return queryset

        # La prueba especifica que un funcionario solo ve prestadores y turistas.
        allowed_roles_to_view = [
            CustomUser.Role.PRESTADOR,
            CustomUser.Role.TURISTA,
        ]
        # Un funcionario puede ver los roles permitidos Y a sí mismo
        return queryset.filter(
            Q(role__in=allowed_roles_to_view) | Q(pk=user.pk)
        )

# class AdminPrestadorViewSet(viewsets.ModelViewSet):
#     queryset = ProviderProfile.objects.all()
#     serializer_class = AdminPrestadorSerializer
#     permission_classes = [IsAdminOrFuncionario]

class AdminPublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = AdminPublicacionSerializer
    permission_classes = [IsAdminOrFuncionario]

    @action(detail=True, methods=['post'], permission_classes=[IsAnyAdminOrDirectivo])
    def approve(self, request, pk=None):
        publicacion = self.get_object()
        if publicacion.estado == 'PENDIENTE_DIRECTIVO' and request.user.role == 'FUNCIONARIO_DIRECTIVO':
            publicacion.estado = 'PENDIENTE_ADMIN'
            publicacion.save()
            return Response({'status': 'Aprobado por directivo, pendiente de admin'})
        if publicacion.estado == 'PENDIENTE_ADMIN' and request.user.role == 'ADMIN':
            publicacion.estado = 'PUBLICADO'
            publicacion.save()
            return Response({'status': 'Publicación aprobada y publicada'})
        return Response({'error': 'No tiene permiso para esta acción o estado incorrecto'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[IsAnyAdminOrDirectivo])
    def reject(self, request, pk=None):
        publicacion = self.get_object()
        publicacion.estado = 'BORRADOR'
        publicacion.save()
        return Response({'status': 'Publicación rechazada y devuelta a borrador'})

    @action(detail=True, methods=['post'], permission_classes=[IsAdminOrFuncionario])
    def submit_for_approval(self, request, pk=None):
        publicacion = self.get_object()
        publicacion.estado = 'PENDIENTE_DIRECTIVO'
        publicacion.save()
        return Response({'status': 'Publicación enviada para aprobación'})

class HomePageComponentViewSet(viewsets.ModelViewSet):
    queryset = HomePageComponent.objects.all()
    serializer_class = HomePageComponentSerializer
    permission_classes = [AllowAny]

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAdmin]

class ScoringRuleViewSet(viewsets.ModelViewSet):
    queryset = ScoringRule.objects.all()
    serializer_class = ScoringRuleSerializer
    permission_classes = [IsAdmin]

class AdminArtesanoViewSet(viewsets.ModelViewSet):
    queryset = Artesano.objects.all()
    serializer_class = AdminArtesanoDetailSerializer
    permission_classes = [IsAdminOrFuncionario]

# class PlantillaVerificacionViewSet(viewsets.ModelViewSet):
#     queryset = PlantillaVerificacion.objects.all()
#     serializer_class = PlantillaVerificacionListSerializer
#     permission_classes = [IsAdminOrFuncionario]

# class VerificacionViewSet(viewsets.ModelViewSet):
#     queryset = Verificacion.objects.all()
#     serializer_class = VerificacionListSerializer
#     permission_classes = [IsAuthenticated]

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = [IsAnyAdminOrDirectivo]

class OpcionRespuestaViewSet(viewsets.ModelViewSet):
    queryset = OpcionRespuesta.objects.all()
    serializer_class = OpcionRespuestaSerializer
    permission_classes = [IsAnyAdminOrDirectivo]

class SiteConfigurationView(generics.RetrieveUpdateAPIView):
    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigurationSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'POST']:
            return [IsAdmin()]
        return [AllowAny()]

    def get_object(self):
        return SiteConfiguration.load()

class ArtesanoProfileView(generics.RetrieveUpdateAPIView):
    queryset = Artesano.objects.all()
    serializer_class = ArtesanoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.artesano

class PrestadorResenaViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite a un prestador ver y responder a las reseñas de su negocio.
    """
    serializer_class = ResenaSerializer
    permission_classes = [IsAuthenticated, IsPrestador]

class PrestadorResenaUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    Permite a un prestador actualizar (específicamente, responder) una reseña.
    """
    serializer_class = ResenaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    queryset = Resena.objects.all()

    def get_queryset(self):
        # Asegurarse de que el prestador solo pueda responder a sus propias reseñas
        return Resena.objects.none()

    def partial_update(self, request, *args, **kwargs):
        # Solo permitir la actualización del campo 'respuesta_prestador'
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Asegurarse de que solo se actualice el campo permitido
        if 'respuesta_prestador' in serializer.validated_data:
            instance.respuesta_prestador = serializer.validated_data['respuesta_prestador']
            instance.save(update_fields=['respuesta_prestador'])
            return Response(serializer.data)
        else:
            return Response({"error": "Solo se puede actualizar la respuesta del prestador."}, status=status.HTTP_400_BAD_REQUEST)

class FeedbackProveedorView(generics.ListAPIView):
    queryset = Sugerencia.objects.none()
    serializer_class = FeedbackProveedorSerializer
    permission_classes = [IsAuthenticated]

class UserLLMConfigView(generics.RetrieveUpdateAPIView):
    """
    Vista para que un usuario vea y actualice su propia configuración de LLM.
    """
    serializer_class = UserLLMConfigSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # get_or_create asegura que cada usuario tenga una configuración de LLM,
        # creándola con los valores por defecto si no existe.
        llm_config, created = UserLLMConfig.objects.get_or_create(user=self.request.user)
        return llm_config

class ImagenGaleriaView(generics.ListCreateAPIView):
    queryset = ImagenGaleria.objects.all()
    serializer_class = ImagenGaleriaSerializer
    permission_classes = [IsAuthenticated]

class ImagenArtesanoView(generics.ListCreateAPIView):
    queryset = ImagenArtesano.objects.all()
    serializer_class = ImagenArtesanoSerializer
    permission_classes = [IsAuthenticated]

class RespuestaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = RespuestaUsuario.objects.all()
    serializer_class = RespuestaUsuarioSerializer
    permission_classes = [IsAuthenticated]

class PublicacionListView(generics.ListAPIView):
    serializer_class = PublicacionListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Publicacion.objects.filter(estado='PUBLICADO')

class PublicacionDetailView(generics.RetrieveAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionDetailSerializer
    permission_classes = [AllowAny]

class ConsejoConsultivoListView(generics.ListAPIView):
    queryset = ConsejoConsultivo.objects.all()
    serializer_class = ConsejoConsultivoSerializer
    permission_classes = [AllowAny]

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]

class LocationListView(generics.ListAPIView):
    queryset = Artesano.objects.none() # Placeholder
    serializer_class = LocationSerializer
    permission_classes = [AllowAny]

class GaleriaListView(generics.ListAPIView):
    queryset = ImagenGaleria.objects.all()  # Placeholder
    serializer_class = GaleriaItemSerializer
    permission_classes = [AllowAny]

# from agents.corps.turismo_coronel import get_turismo_coronel_graph
class AgentChatView(views.APIView):
    permission_classes = [AllowAny]  # El agente está diseñado para manejar usuarios invitados

    async def post(self, request, *args, **kwargs):
        # user_message = request.data.get('message', '')
        # if not user_message:
        #     return Response({'error': 'No se proporcionó ningún mensaje.'}, status=status.HTTP_400_BAD_REQUEST)
        # # Obtener el historial de la conversación de la sesión, o inicializarlo si no existe.
        # conversation_history = request.session.get('conversation_history', [])
        # try:
        #     agent = get_turismo_coronel_graph()
        #     # Preparar el diccionario de entrada para el agente, incluyendo el contexto.
        #     agent_input = {
        #         "general_order": user_message,
        #         "app_context": {
        #             "user": request.user,
        #             "entity": getattr(request, 'entity', None)  # Pasar la entidad del middleware
        #         },
        #         "conversation_history": conversation_history
        #     }
        #     # Invocar al agente de forma asíncrona.
        #     final_state = await agent.ainvoke(agent_input)
        #     # Extraer el informe final y el historial actualizado del estado de respuesta.
        #     response_message = final_state.get('final_report', 'No se pudo generar una respuesta.')
        #     # Guardar el historial actualizado en la sesión para el próximo turno.
        #     request.session['conversation_history'] = final_state.get('conversation_history', [])
        #     return Response({'reply': response_message})
        # except Exception as e:
        #     # Es una buena práctica registrar la excepción para la depuración.
        #     import logging
        #     logging.error(f"Error en AgentChatView: {e}", exc_info=True)
        return Response({'error': 'Funcionalidad de agente temporalmente deshabilitada.'},
                        status=status.HTTP_503_SERVICE_UNAVAILABLE)


class AgentTaskStatusView(generics.RetrieveAPIView):
    queryset = AgentTask.objects.all()
    serializer_class = AgentTaskSerializer
    permission_classes = [IsAuthenticated]


class AnalyticsDataView(views.APIView):
    permission_classes = [IsAdminOrFuncionario]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Datos de analítica."})
class AdminUsuarioListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioListSerializer
    permission_classes = [IsAdminOrFuncionario]

class RubroArtesanoListView(generics.ListAPIView):
    queryset = RubroArtesano.objects.all().order_by('nombre')
    serializer_class = RubroArtesanoSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        cache_key = 'rubros_artesanos_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        cache.set(cache_key, data, 60 * 60) # Cache por 1 hora
        return Response(data)

class ArtesanoPublicListView(generics.ListAPIView):
    queryset = Artesano.objects.all()
    serializer_class = ArtesanoPublicListSerializer
    permission_classes = [AllowAny]

class ArtesanoPublicDetailView(generics.RetrieveAPIView):
    queryset = Artesano.objects.all()
    serializer_class = ArtesanoPublicDetailSerializer
    permission_classes = [AllowAny]

class DetailedStatisticsView(views.APIView):
    permission_classes = [IsAdmin]
    def get(self, request, *args, **kwargs):
        return Response({"message": "Datos de estadísticas detalladas."})

class ExportExcelView(views.APIView):
    permission_classes = [IsAdmin]

    def get(self, request, *args, **kwargs):
        return Response(
            {"error": "Esta funcionalidad aún no está implementada."},
            status=status.HTTP_501_NOT_IMPLEMENTED
        )

class ImagenArtesanoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImagenArtesanoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'artesano'):
            return ImagenArtesano.objects.filter(artesano=user.artesano)
        return ImagenArtesano.objects.none()

class ImagenGaleriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImagenGaleriaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ImagenGaleria.objects.none()

class PlaceholderView(views.APIView):
    """
    Vista de marcador de posición para módulos futuros.
    Devuelve 204 No Content.
    """
    permission_classes = [IsAuthenticated, IsPrestador]

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)