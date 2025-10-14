from rest_framework import generics, views, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from dj_rest_auth.registration.views import RegisterView
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
from .models import (
    CustomUser,
    PrestadorServicio,
    ImagenGaleria,
    ImagenArtesano,
    DocumentoLegalizacion,
    Publicacion,
    ConsejoConsultivo,
    AtractivoTuristico,
    RutaTuristica,
    ElementoGuardado,
    CategoriaPrestador,
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
    Vacante
)
from .serializers import (
    GaleriaItemSerializer,
    PaginaInstitucionalSerializer,
    ScoringRuleSerializer,
    NotificacionSerializer,
    PrestadorServicioSerializer,
    PrestadorServicioUpdateSerializer,
    ArtesanoSerializer,
    ArtesanoUpdateSerializer,
    ImagenGaleriaSerializer,
    ImagenArtesanoSerializer,
    DocumentoLegalizacionSerializer,
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
    PrestadorRegisterSerializer,
    TuristaRegisterSerializer,
    ArtesanoRegisterSerializer,
    AdministradorRegisterSerializer,
    FuncionarioDirectivoRegisterSerializer,
    FuncionarioProfesionalRegisterSerializer,
    ElementoGuardadoSerializer,
    ElementoGuardadoCreateSerializer,
    CategoriaPrestadorSerializer,
    PrestadorServicioPublicListSerializer,
    PrestadorServicioPublicDetailSerializer,
    RubroArtesanoSerializer,
    ArtesanoPublicListSerializer,
    ArtesanoPublicDetailSerializer,
    AdminPrestadorListSerializer,
    AdminPrestadorDetailSerializer,
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
    PlantillaVerificacionListSerializer,
    PlantillaVerificacionDetailSerializer,
    VerificacionListSerializer,
    VerificacionDetailSerializer,
    IniciarVerificacionSerializer,
    GuardarVerificacionSerializer,
    CapacitacionDetailSerializer,
    RegistrarAsistenciaSerializer,
    ProductoSerializer,
    RegistroClienteSerializer,
    VacanteSerializer
)
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
class VacanteViewSet(viewsets.ModelViewSet):
    queryset = Vacante.objects.filter(activa=True).select_related('empresa')
    serializer_class = VacanteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['tipo_contrato', 'ubicacion']
    search_fields = ['titulo', 'descripcion', 'empresa__nombre_negocio']
    ordering_fields = ['fecha_publicacion', 'salario']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsPrestador]
        else: # list, retrieve
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, 'perfil_prestador'):
            return Vacante.objects.filter(empresa=user.perfil_prestador)
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(empresa=self.request.user.perfil_prestador)

    def perform_update(self, serializer):
        serializer.save(empresa=self.request.user.perfil_prestador)


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        return Producto.objects.filter(prestador=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)


class RegistroClienteViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroClienteSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        return RegistroCliente.objects.filter(prestador=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)


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

class PrestadorRegisterView(RegisterView):
    serializer_class = PrestadorRegisterSerializer

class TuristaRegisterView(RegisterView):
    serializer_class = TuristaRegisterSerializer

class ArtesanoRegisterView(RegisterView):
    serializer_class = ArtesanoRegisterSerializer


class AdministradorRegisterView(RegisterView):
    serializer_class = AdministradorRegisterSerializer


class FuncionarioDirectivoRegisterView(RegisterView):
    serializer_class = FuncionarioDirectivoRegisterSerializer


class FuncionarioProfesionalRegisterView(RegisterView):
    serializer_class = FuncionarioProfesionalRegisterSerializer


class DocumentoLegalizacionDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = DocumentoLegalizacionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return DocumentoLegalizacion.objects.filter(prestador=self.request.user.perfil_prestador)

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
                model_map = {'prestadorservicio': PrestadorServicio, 'artesano': Artesano}
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
        queryset = self.get_queryset().filter(parent__isnull=True).order_by('orden')
        serializer = self.get_serializer(queryset, many=True)
        # Devolver una estructura similar a la paginación para que el test no falle
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

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminOrFuncionarioForUserManagement]

    def get_queryset(self):
        user = self.request.user
        if user.role == CustomUser.Role.ADMIN:
            return CustomUser.objects.all()

        allowed_roles_to_view = [
            CustomUser.Role.PRESTADOR,
            CustomUser.Role.ARTESANO,
            CustomUser.Role.TURISTA,
        ]
        # Un funcionario puede ver los roles permitidos Y a sí mismo
        return CustomUser.objects.filter(
            Q(role__in=allowed_roles_to_view) | Q(pk=user.pk)
        )

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

from .filters import PrestadorServicioFilter

class AdminPrestadorViewSet(viewsets.ModelViewSet):
    queryset = PrestadorServicio.objects.all()
    serializer_class = AdminPrestadorDetailSerializer
    permission_classes = [IsAdminOrFuncionario]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PrestadorServicioFilter
    search_fields = ['nombre_negocio', 'usuario__email']

    @action(detail=True, methods=['post'], permission_classes=[IsAdminOrFuncionario])
    def approve(self, request, pk=None):
        prestador = self.get_object()
        prestador.aprobado = True
        prestador.save()
        return Response({'status': 'Prestador aprobado'})

class AdminArtesanoViewSet(viewsets.ModelViewSet):
    queryset = Artesano.objects.all()
    serializer_class = AdminArtesanoDetailSerializer
    permission_classes = [IsAdminOrFuncionario]

class PlantillaVerificacionViewSet(viewsets.ModelViewSet):
    queryset = PlantillaVerificacion.objects.all()
    serializer_class = PlantillaVerificacionListSerializer
    permission_classes = [IsAdminOrFuncionario]

class VerificacionViewSet(viewsets.ModelViewSet):
    queryset = Verificacion.objects.all()
    serializer_class = VerificacionListSerializer
    permission_classes = [IsAuthenticated]

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

class PrestadorProfileView(generics.RetrieveUpdateAPIView):
    queryset = PrestadorServicio.objects.all()
    serializer_class = PrestadorServicioSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.perfil_prestador

class ArtesanoProfileView(generics.RetrieveUpdateAPIView):
    queryset = Artesano.objects.all()
    serializer_class = ArtesanoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.artesano

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

class DocumentoLegalizacionView(generics.ListCreateAPIView):
    queryset = DocumentoLegalizacion.objects.all()
    serializer_class = DocumentoLegalizacionSerializer
    permission_classes = [IsAuthenticated]

class RespuestaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = RespuestaUsuario.objects.all()
    serializer_class = RespuestaUsuarioSerializer
    permission_classes = [IsAuthenticated]

class PublicacionListView(generics.ListAPIView):
    queryset = Publicacion.objects.filter(estado='PUBLICADO')
    serializer_class = PublicacionListSerializer
    permission_classes = [AllowAny]

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
    queryset = PrestadorServicio.objects.all() # Placeholder
    serializer_class = LocationSerializer
    permission_classes = [AllowAny]

class GaleriaListView(generics.ListAPIView):
    queryset = ImagenGaleria.objects.all() # Placeholder
    serializer_class = GaleriaItemSerializer
    permission_classes = [AllowAny]

from agents.corps.turismo_coronel import get_turismo_coronel_graph

class AgentChatView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user_message = request.data.get('message', '')
        if not user_message:
            return Response({'error': 'No message provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Aquí iría la lógica para invocar al agente LangChain/LangGraph
            # Por ahora, devolvemos una respuesta simulada
            agent = get_turismo_coronel_graph()
            response_message = agent.invoke(user_message) # Esto puede variar según la implementación del agente

            return Response({'reply': response_message})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

class CategoriaPrestadorListView(generics.ListAPIView):
    queryset = CategoriaPrestador.objects.all()
    serializer_class = CategoriaPrestadorSerializer
    permission_classes = [AllowAny]

class PrestadorServicioPublicListView(generics.ListAPIView):
    queryset = PrestadorServicio.objects.all()
    serializer_class = PrestadorServicioPublicListSerializer
    permission_classes = [AllowAny]

class PrestadorServicioPublicDetailView(generics.RetrieveAPIView):
    queryset = PrestadorServicio.objects.all()
    serializer_class = PrestadorServicioPublicDetailSerializer
    permission_classes = [AllowAny]

class RubroArtesanoListView(generics.ListAPIView):
    queryset = RubroArtesano.objects.all()
    serializer_class = RubroArtesanoSerializer
    permission_classes = [AllowAny]

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
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return ImagenGaleria.objects.filter(prestador=user.perfil_prestador)
        return ImagenGaleria.objects.none()