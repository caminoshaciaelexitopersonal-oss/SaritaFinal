# SaritaUnificado/backend/apps/prestadores/models.py

# Este archivo sirve como el punto de entrada principal para que Django
# descubra todos los modelos relacionados con la app 'prestadores'.

# Importa todos los modelos desde sus respectivos paquetes consolidados.
from .mi_negocio.gestion_operativa.modulos_genericos.models import *
from .mi_negocio.gestion_operativa.modulos_genericos.perfil.models import * # Importación directa del módulo refactorizado
from .mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import * # Importación directa del módulo refactorizado
from .mi_negocio.gestion_operativa.modulos_genericos.inventario.models import * # Importación directa del módulo refactorizado
from .mi_negocio.gestion_operativa.modulos_genericos.costos.models import * # Importación directa del módulo refactorizado
from .mi_negocio.gestion_operativa.modulos_genericos.reservas.models import * # Importación directa del módulo refactorizado
from .mi_negocio.gestion_operativa.modulos_genericos.soporte.models import * # Importación directa del módulo refactorizado
from .mi_negocio.gestion_operativa.modulos_especializados.models import *
 
