
from django.urls import path, include

# URLs del Panel de Administración de "Mi Negocio"
# Este archivo agrupa las rutas de los diferentes módulos de gestión
# para que el administrador pueda supervisarlos.

urlpatterns = [
    # path('gestion-comercial/', include('apps.admin_panel.gestion_comercial.urls')),
    # path('gestion-financiera/', include('apps.admin_panel.gestion_financiera.urls')),
    # NOTA: Los siguientes módulos se añadirán a medida que se creen sus archivos urls.py
    # path('gestion-contable/', include('apps.admin_panel.gestion_contable.urls')),
    # path('gestion-archivistica/', include('apps.admin_panel.gestion_archivistica.urls')),
    # path('gestion-operativa/', include('apps.admin_panel.gestion_operativa.urls')),
]
