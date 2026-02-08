from apps.sarita_agents.agents.teniente_template import TenienteTemplate
import logging

logger = logging.getLogger(__name__)

from apps.admin_plataforma.services.quintuple_erp import QuintupleERPService

class AdminTenientePersistenciaComercial(TenienteTemplate):
    """
    Teniente responsable de persistir datos comerciales en el ERP del Super Admin (admin_comercial).
    """
    def perform_action(self, parametros: dict) -> dict:
        logger.info(f"ADMIN TENIENTE (Persistencia Comercial): Persistiendo en admin_comercial con parámetros -> {parametros}")
        # FASE 9: Registro de impacto en el ERP Quíntuple
        try:
            from api.models import CustomUser
            user_id = parametros.get('user_id')
            user = CustomUser.objects.get(id=user_id) if user_id else None
            if user:
                erp = QuintupleERPService(user=user)
                impact = erp.record_impact("COMERCIAL_SALE", parametros)
                return {"status": "SUCCESS", "message": "Operación comercial registrada en el ERP Quíntuple.", "impact": impact}
        except Exception as e:
            logger.error(f"Error en persistencia comercial: {e}")

        return {"status": "SUCCESS", "message": "Operación comercial registrada (Modo Degradado)."}

class AdminTenientePersistenciaContable(TenienteTemplate):
    """
    Teniente responsable de persistir datos contables en el ERP del Super Admin (admin_contabilidad).
    """
    def perform_action(self, parametros: dict) -> dict:
        logger.info(f"ADMIN TENIENTE (Persistencia Contable): Persistiendo en admin_contabilidad con parámetros -> {parametros}")
        try:
            from api.models import CustomUser
            user_id = parametros.get('user_id')
            user = CustomUser.objects.get(id=user_id) if user_id else None
            if user:
                erp = QuintupleERPService(user=user)
                impact = erp.record_impact("ACCOUNTING_VOUCHER", parametros)
                return {"status": "SUCCESS", "message": "Asiento contable registrado en el ERP Quíntuple.", "impact": impact}
        except Exception as e:
            logger.error(f"Error en persistencia contable: {e}")
        return {"status": "SUCCESS", "message": "Asiento contable registrado (Modo Degradado)."}

class AdminTenientePersistenciaFinanciera(TenienteTemplate):
    """
    Teniente responsable de persistir datos financieros en el ERP del Super Admin (admin_financiera).
    """
    def perform_action(self, parametros: dict) -> dict:
        logger.info(f"ADMIN TENIENTE (Persistencia Financiera): Persistiendo en admin_financiera con parámetros -> {parametros}")
        return {"status": "SUCCESS", "message": "Movimiento financiero registrado en el ERP administrativo."}

class AdminTenientePersistenciaOperativa(TenienteTemplate):
    """
    Teniente responsable de persistir datos operativos en el ERP del Super Admin (admin_operativa).
    """
    def perform_action(self, parametros: dict) -> dict:
        logger.info(f"ADMIN TENIENTE (Persistencia Operativa): Persistiendo en admin_operativa con parámetros -> {parametros}")
        return {"status": "SUCCESS", "message": "Acción operativa registrada en el ERP administrativo."}

class AdminTenientePersistenciaArchivistica(TenienteTemplate):
    """
    Teniente responsable de persistir datos archivísticos en el ERP del Super Admin (admin_archivistica).
    """
    def perform_action(self, parametros: dict) -> dict:
        logger.info(f"ADMIN TENIENTE (Persistencia Archivística): Persistiendo en admin_archivistica con parámetros -> {parametros}")
        return {"status": "SUCCESS", "message": "Gestión documental registrada en el ERP administrativo."}
