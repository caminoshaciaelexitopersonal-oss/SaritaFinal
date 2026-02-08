# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios/cumplimiento/sargentos/sargento_impacto_erp.py

from .......sargento_template import SargentoTemplate
from apps.admin_plataforma.services.quintuple_erp import QuintupleERPService
from api.models import CustomUser

class SargentoImpactoERP(SargentoTemplate):
    """
    Sargento de Impacto ERP.
    Función atómica: Propagar el evento comercial a las 5 dimensiones del ERP.
    """
    def perform_atomic_action(self, action_data: dict):
        user_id = action_data.get("user_id")
        event_type = action_data.get("event_type", "COMERCIAL_EVENT")
        payload = action_data.get("payload", {})

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise ValueError(f"Usuario {user_id} no encontrado para impacto ERP.")

        erp_service = QuintupleERPService(user=user)
        impact_result = erp_service.record_impact(event_type, payload)

        return impact_result
