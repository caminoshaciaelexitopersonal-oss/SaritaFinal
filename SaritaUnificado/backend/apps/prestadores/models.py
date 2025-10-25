# SaritaUnificado/backend/apps/prestadores/models.py

"""
Este archivo sirve como el punto de entrada principal para que Django
descubra todos los modelos relacionados con la app 'prestadores', que ahora
están organizados en una arquitectura modular bajo 'mi_negocio'.
"""

# --- Módulos Genéricos de Gestión Operativa ---

# Módulo de Perfil del Prestador (Refactorizado)
from .mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil, CategoriaPrestador

# Módulo de Clientes (CRM) (Refactorizado)
from .mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Cliente

# Módulo de Productos y Servicios (Pendiente de refactorización completa)
# from .mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import *

# Módulo de Reservas (Pendiente de refactorización completa)
# from .mi_negocio.gestion_operativa.modulos_genericos.reservas.models import *

# ... (Se añadirán más importaciones a medida que se refactoricen los demás módulos)
