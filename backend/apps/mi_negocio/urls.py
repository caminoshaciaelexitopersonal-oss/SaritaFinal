
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.mi_negocio.gestion_operativa.modulos_genericos.clientes.views import ClienteViewSet
from api.views import PlaceholderView

app_name = 'mi_negocio'

router = DefaultRouter()
router.register(r'operativa/clientes', ClienteViewSet, basename='cliente')

urlpatterns = [
    path('', include(router.urls)),
    # Rutas de marcador de posición para los otros módulos
    path('comercial/', PlaceholderView.as_view(), name='comercial-placeholder'),
    path('contable/', PlaceholderView.as_view(), name='contable-placeholder'),
    path('financiera/', PlaceholderView.as_view(), name='financiera-placeholder'),
    path('archivistica/', PlaceholderView.as_view(), name='archivistica-placeholder'),
]
