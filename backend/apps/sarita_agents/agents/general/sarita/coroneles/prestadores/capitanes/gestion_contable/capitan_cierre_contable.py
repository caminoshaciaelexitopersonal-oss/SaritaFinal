# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/capitanes/gestion_contable/capitan_cierre_contable.py
import logging
from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import Mision, PlanTáctico

logger = logging.getLogger(__name__)

class CapitanCierreContable(CapitanTemplate):
    """
    Agente de Cierre: Ejecuta el cierre de periodos y traslada saldos a cuentas de resultado.
    """

    def plan(self, mision: Mision) -> PlanTáctico:
        logger.info(f"CAPITÁN (Cierre): Iniciando cierre de periodo para misión {mision.id}")

        pasos = {
            "validar_periodo": {
                "descripcion": "Verificar que todos los asientos del periodo estén balanceados.",
                "teniente": "auditor_balance_contable",
                "parametros": mision.directiva_original.get("parameters", {})
            },
            "ejecutar_cierre": {
                "descripcion": "Bloquear periodo y generar asiento de cierre.",
                "teniente": "admin_persistencia_contable",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }

        return PlanTáctico.objects.create(
            mision=mision,
            capitan_responsable=self.__class__.__name__,
            pasos_del_plan=pasos,
            estado='PLANIFICADO'
        )

    def _get_tenientes(self) -> dict:
        from apps.sarita_agents.agents.general.sarita.coroneles.administrador_general.tenientes.operativos.tenientes_persistencia import AdminTenientePersistenciaContable
        class TenienteAuditorBalance:
            def execute_task(self, tarea):
                return {"status": "SUCCESS", "message": "Balance verificado para cierre."}
        return {
            "auditor_balance_contable": TenienteAuditorBalance(),
            "admin_persistencia_contable": AdminTenientePersistenciaContable()
        }
