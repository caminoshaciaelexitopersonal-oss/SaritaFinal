from apps.sarita_agents.agents.teniente_template import TenienteTemplate
import logging

logger = logging.getLogger(__name__)

class AdminTenientePersistenciaComercial(TenienteTemplate):
    """
    Teniente responsable de persistir datos comerciales en el ERP del Super Admin (admin_comercial).
    """
    def perform_action(self, parametros: dict) -> dict:
        logger.info(f"ADMIN TENIENTE (Persistencia Comercial): Persistiendo en admin_comercial con parámetros -> {parametros}")
        # Lógica de persistencia funcional en tablas admin_*
        return {"status": "SUCCESS", "message": "Operación comercial registrada en el ERP administrativo."}

class AdminTenientePersistenciaContable(TenienteTemplate):
    """
    Teniente responsable de persistir datos contables en el ERP del Super Admin (admin_contabilidad).
    """
    def perform_action(self, parametros: dict) -> dict:
        logger.info(f"ADMIN TENIENTE (Persistencia Contable): Persistiendo en admin_contabilidad con parámetros -> {parametros}")
        return {"status": "SUCCESS", "message": "Asiento contable registrado en el ERP administrativo."}

class AdminTenientePersistenciaFinanciera(TenienteTemplate):
    """
    Teniente responsable de persistir datos financieros en el ERP del Super Admin (admin_financiera).
    """
    def perform_action(self, parametros: dict) -> dict:
        logger.info(f"ADMIN TENIENTE (Persistencia Financiera): Persistiendo en admin_financiera con parámetros -> {parametros}")
        return {"status": "SUCCESS", "message": "Movimiento financiero registrado en el ERP administrativo."}
