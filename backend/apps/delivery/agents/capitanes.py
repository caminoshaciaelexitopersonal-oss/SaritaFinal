import logging
from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import PlanTáctico, TareaDelegada

logger = logging.getLogger(__name__)

class CapitanDeliveryBase(CapitanTemplate):
    """Base para capitanes de delivery que permite ejecución síncrona en este entorno."""
    def delegate(self, plan: PlanTáctico):
        logger.info(f"CAPITÁN ({self.__class__.__name__}): Ejecutando plan {plan.id} de forma síncrona.")
        plan.estado = 'EN_EJECUCION'
        plan.save()

        from .tenientes import (
            TenienteValidacionEmpresa,
            TenienteHabilitacionConductor,
            TenienteControlVehiculos,
            TenienteAsignacionRuta,
            TenienteControlEjecucion,
            TenienteEvidenciasServicio
        )

        roster = {
            "validacion_empresa": TenienteValidacionEmpresa(),
            "habilitacion_conductor": TenienteHabilitacionConductor(),
            "control_vehiculos": TenienteControlVehiculos(),
            "asignacion_ruta": TenienteAsignacionRuta(),
            "control_ejecucion": TenienteControlEjecucion(),
            "evidencias_servicio": TenienteEvidenciasServicio()
        }

        for _, tarea_info in plan.pasos_del_plan.items():
            teniente_name = tarea_info.get("teniente")
            teniente = roster.get(teniente_name)
            if teniente:
                tarea = TareaDelegada.objects.create(
                    plan_tactico=plan,
                    teniente_asignado=teniente_name,
                    descripcion_tarea=tarea_info.get("descripcion", "N/A"),
                    parametros=tarea_info.get("parametros", {}),
                    estado='EN_PROGRESO'
                )
                teniente.execute_task(tarea)

        plan.estado = 'COMPLETADO'
        plan.save()

class CapitanAfiliacionDelivery(CapitanDeliveryBase):
    def _get_tenientes(self) -> dict:
        return {"validacion_empresa": "TenienteValidacionEmpresa"}

    def plan(self, mision) -> PlanTáctico:
        plan = self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
        plan.pasos_del_plan = {
            "paso_1": {
                "teniente": "validacion_empresa",
                "descripcion": "Validar estatus legal y tributario de la empresa",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }
        plan.save()
        return plan

class CapitanGestionConductores(CapitanDeliveryBase):
    def _get_tenientes(self) -> dict:
        return {"habilitacion_conductor": "TenienteHabilitacionConductor"}

    def plan(self, mision) -> PlanTáctico:
        plan = self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
        plan.pasos_del_plan = {
            "paso_1": {
                "teniente": "habilitacion_conductor",
                "descripcion": "Verificar licencia y antecedentes del conductor",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }
        plan.save()
        return plan

class CapitanGestionVehiculos(CapitanDeliveryBase):
    def _get_tenientes(self) -> dict:
        return {"control_vehiculos": "TenienteControlVehiculos"}

    def plan(self, mision) -> PlanTáctico:
        plan = self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
        plan.pasos_del_plan = {
            "paso_1": {
                "teniente": "control_vehiculos",
                "descripcion": "Auditar estado mecánico y documentos del vehículo",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }
        plan.save()
        return plan

class CapitanAsignacionServicios(CapitanDeliveryBase):
    def _get_tenientes(self) -> dict:
        return {"asignacion_ruta": "TenienteAsignacionRuta"}

    def plan(self, mision) -> PlanTáctico:
        plan = self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
        plan.pasos_del_plan = {
            "paso_1": {
                "teniente": "asignacion_ruta",
                "descripcion": "Calcular ruta óptima y asignar conductor disponible",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }
        plan.save()
        return plan

class CapitanEjecucionOperativaDelivery(CapitanDeliveryBase):
    def _get_tenientes(self) -> dict:
        return {"control_ejecucion": "TenienteControlEjecucion"}

    def plan(self, mision) -> PlanTáctico:
        plan = self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
        plan.pasos_del_plan = {
            "paso_1": {
                "teniente": "control_ejecucion",
                "descripcion": "Monitorear eventos de recogida y entrega",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }
        plan.save()
        return plan

class CapitanPagosLiquidacionesDelivery(CapitanDeliveryBase):
    def _get_tenientes(self) -> dict:
        return {"control_ejecucion": "TenienteControlEjecucion"} # Reusando o simplificando

    def plan(self, mision) -> PlanTáctico:
        plan = self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
        plan.pasos_del_plan = {
            "paso_1": {
                "teniente": "control_ejecucion",
                "descripcion": "Disparar intención de pago en monedero",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }
        plan.save()
        return plan

class CapitanAuditoriaDelivery(CapitanDeliveryBase):
    def _get_tenientes(self) -> dict:
        return {"evidencias_servicio": "TenienteEvidenciasServicio"}

    def plan(self, mision) -> PlanTáctico:
        plan = self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
        plan.pasos_del_plan = {
            "paso_1": {
                "teniente": "evidencias_servicio",
                "descripcion": "Generar reporte forense del servicio logístico",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }
        plan.save()
        return plan
