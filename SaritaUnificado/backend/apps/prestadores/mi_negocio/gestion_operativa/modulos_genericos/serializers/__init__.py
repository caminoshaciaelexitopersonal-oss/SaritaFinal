# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/serializers/__init__.py
from ..perfil.serializers import PerfilSerializer
from ..productos_servicios.serializers import ProductoServicioSerializer
from ..crm.serializers import ClienteSerializer
from ..costos.serializers import CostoSerializer
from ..inventario.serializers import InventarioSerializer
from ..reservas.serializers import ReservaSerializer
from ..rat.serializers import RegistroActividadTuristicaSerializer
from ..soporte.serializers import TicketSoporteSerializer
# La siguiente línea se mantiene si 'configuracion' no se refactoriza aún
from .configuracion import ConfiguracionPrestadorSerializer
# La siguiente línea se mantiene si 'reportes' no se refactoriza aún
from .reportes import ReporteSerializer
