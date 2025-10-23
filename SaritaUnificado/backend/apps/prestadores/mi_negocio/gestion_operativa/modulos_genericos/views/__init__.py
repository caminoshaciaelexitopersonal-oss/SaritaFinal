# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/__init__.py
from ..perfil.views import PerfilViewSet
from ..productos_servicios.views import ProductoServicioViewSet
from ..crm.views import ClienteViewSet
from ..costos.views import CostoViewSet
from ..inventario.views import InventarioViewSet
from ..reservas.views import ReservaViewSet
from ..rat.views import RegistroActividadTuristicaViewSet
from ..soporte.views import TicketSoporteViewSet
# La siguiente línea se mantiene si 'configuracion' no se refactoriza aún
from .configuracion import ConfiguracionPrestadorViewSet
# La siguiente línea se mantiene si 'reportes' no se refactoriza aún
from .reportes import ReporteViewSet
