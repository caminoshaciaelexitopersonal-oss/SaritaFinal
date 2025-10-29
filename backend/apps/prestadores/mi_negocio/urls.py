# SaritaUnificado/backend/apps/prestadores/mi_negocio/urls.py
from django.urls import path, include

app_name = 'mi_negocio'

urlpatterns = [
    # --- Gestión Operativa ---
    # Incluye las rutas de todos los módulos genéricos (Perfil, Clientes, etc.)
    path('operativa/genericos/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.urls')),

    # (Aquí se añadirán las rutas para módulos especializados en el futuro)
    # path('operativa/especializados/', include('...urls_especializados')),

    # --- Marcadores de posición para futuras gestiones ---
    path('comercial/', include('apps.prestadores.mi_negocio.gestion_comercial.urls')),
    path('contable/', include('apps.prestadores.mi_negocio.gestion_contable.urls')),
    path('financiera/', include('apps.prestadores.mi_negocio.gestion_financiera.urls')),
    path('archivistica/', include('apps.prestadores.mi_negocio.gestion_archivistica.urls')),
    path('nomina/', include('apps.nomina.urls')),
]
