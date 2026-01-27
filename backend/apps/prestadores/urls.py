from django.urls import path, include
from rest_framework.routers import DefaultRouter
 
from backend.views import AdminPrestadorViewSet

# Router para las vistas de administración (fuera de 'Mi Negocio')
admin_router = DefaultRouter()
admin_router.register(r'admin/prestadores', AdminPrestadorViewSet, basename='adminprestador')

urlpatterns = [
    # Incluir las URLs de administración
    path('', include(admin_router.urls)),
    # Incluir las URLs del panel 'Mi Negocio'
    path('mi-negocio/', include(('apps.prestadores.mi_negocio.urls', 'mi_negocio'), namespace='mi_negocio')),
 
]
 
