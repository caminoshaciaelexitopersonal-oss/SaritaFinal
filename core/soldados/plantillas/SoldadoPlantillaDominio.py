# core/soldados/plantillas/SoldadoPlantillaDominio.py

from apps.sarita_agents.agents.soldado_n6_oro_v2 import SoldadoN6OroV2
from django.db import models
from typing import Dict, Any

class SoldadoPlantillaDominio(SoldadoN6OroV2):
    """
    PLANTILLA OBLIGATORIA PARA NUEVOS SOLDADOS N6 ORO V2.
    Siga esta estructura para garantizar la certificación automática.
    """

    # 1. Definición de Identidad
    domain = "nombre_del_dominio" # Ej: 'contabilidad'
    subdomain = "nombre_del_subdominio" # Ej: 'ingresos'
    aggregate_root = "NombreDelModelo" # Ej: 'JournalEntry'

    # 2. Seguridad y Gobernanza
    required_permissions = ["dominio.accion_especifica"]
    event_name = "DOMINIO_ACCION_COMPLETADA"

    # 3. Lógica de Negocio Atómica
    def perform_atomic_action(self, params: Dict[str, Any]) -> models.Model:
        """
        Implemente aquí la escritura real en la base de datos.
        Esta sección se ejecuta dentro de transaction.atomic().
        """
        # entity = MyModel.objects.create(...)
        # return entity
        raise NotImplementedError("Debe implementar la lógica real del dominio.")

    # 4. Validaciones Determinísticas (Opcional pero Recomendado)
    def validate_preconditions(self, params: Dict[str, Any]):
        """
        Verifique estados previos aquí.
        Si algo falla, lance raise DeterministicValidationError.
        """
        # if not params.get('data'): raise Exception("Faltan datos")
        pass
