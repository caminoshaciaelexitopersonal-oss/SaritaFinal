# SaritaUnificado/backend/apps/prestadores/mi_negocio/urls.py
from django.urls import path, include

app_name = 'mi_negocio'

urlpatterns = [
    # --- Gestión Operativa ---
    # Incluye las rutas de todos los módulos genéricos (Perfil, Clientes, etc.)
    path('operativa/genericos/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.urls')),

    # (Aquí se añadirán las rutas para módulos especializados en el futuro)
    # path('operativa/especializados/', include('...urls_especializados')),

    # --- Módulos de Gestión ---
    path('comercial/', include('apps.comercial.urls')),
    path('contable/', include(('apps.contabilidad.urls', 'contabilidad_api'), namespace='contabilidad_api')),
    path('financiera/', include('apps.financiera.urls')),
    path('archivistica/', include('apps.prestadores.mi_negocio.gestion_archivistica.urls')),
]
