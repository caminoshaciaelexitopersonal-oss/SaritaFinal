import logging
from typing import Dict, Any, Optional, List
from enum import IntEnum
from django.db import transaction
from api.models import CustomUser
from apps.admin_plataforma.models import GovernanceAuditLog, GovernancePolicy
from api.services import DefenseService

logger = logging.getLogger(__name__)

class AuthorityLevel(IntEnum):
    OPERATIONAL = 1
    DELEGATED = 2
    SOVEREIGN = 3

class GovernanceIntention:
    """
    Representa una intención abstracta de negocio con su contrato y nivel de autoridad.
    """
    def __init__(self, name: str, domain: str, required_role: str, required_params: list = None, min_authority: AuthorityLevel = AuthorityLevel.OPERATIONAL):
        self.name = name
        self.domain = domain
        self.required_role = required_role
        self.required_params = required_params or []
        self.min_authority = min_authority

class GovernanceKernel:
    """
    El Núcleo de Gobernanza Central de Sarita.
    Responsable de validar autoridad, resolver intenciones y coordinar flujos.
    """

    _registry: Dict[str, GovernanceIntention] = {}

    @classmethod
    def register_intention(cls, intention: GovernanceIntention):
        cls._registry[intention.name] = intention
        logger.info(f"KERNEL: Intención '{intention.name}' registrada en el dominio '{intention.domain}'.")

    def __init__(self, user: CustomUser):
        self.user = user

    def get_current_systemic_state(self):
        """Fase Z-GOVERNANCE-LIVE: Retorna el estado operativo actual."""
        from apps.governance_live.models import SystemicState
        state = SystemicState.objects.filter(is_active=True).first()
        return state.current_level if state else 'NORMAL'

    def get_meta_standard_metadata(self) -> Dict[str, Any]:
        """FASE META: Retorna la metadata del estándar civilizatorio."""
        return {
            "name": "SARITA Standard",
            "category": "Infraestructura de Gobernanza Algorítmica Civilizatoria",
            "status": "LEGADO_PROTEGIDO",
            "principles": [
                "Soberanía Humana Absoluta",
                "Trazabilidad Forense e Inmutabilidad",
                "Reversibilidad y Desaceleración Algorítmica",
                "Compartimentación Jurisdiccional",
                "Neutralidad Política y Estabilidad Institucional",
                "Transparencia XAI (Cadena de Decisión)",
                "Autonomía Regulada por Capas",
                "Bien Público Civilizatorio (Anti-Privatización)",
                "Ética de Datos y Privacidad Soberana",
                "Preservación del Legado y Transmisión Generacional"
            ],
            "compliance_metrics": {
                "active_treaties": 5, # TIT, TNA, TNID, TSDS, LEGADO
                "audit_integrity": "SHA-256_CHAINED",
                "human_supremacy_level": "SOVEREIGN_MANDATORY",
                "legacy_protection": "ACTIVE"
            }
        }

    def transition_systemic_state(self, new_level: str, reason: str, context: dict = None):
        """Fase Z-GOVERNANCE-LIVE: Cambia el estado operativo del sistema."""
        if not self.user.is_superuser:
            raise PermissionError("Solo la Autoridad Soberana puede cambiar el estado sistémico.")

        from apps.governance_live.models import SystemicState
        # Desactivar estados anteriores
        SystemicState.objects.filter(is_active=True).update(is_active=False)

        new_state = SystemicState.objects.create(
            current_level=new_level,
            authorized_by=self.user,
            reason=reason,
            context_data=context or {}
        )
        logger.warning(f"KERNEL: Transición de Estado Sistémico a '{new_level}' por {self.user.username}")

        # Auditoría especial de cambio de estado
        self._log_audit(
            GovernanceIntention("SYSTEM_STATE_TRANSITION", "governance", self.user.role, min_authority=AuthorityLevel.SOVEREIGN),
            {"new_level": new_level, "reason": reason},
            {"status": "TRANSITIONED"}
        )
        return new_state

    def validate_interop_mandate(self, signal_type: str, node_id: str, direction: str = 'OUTGOING') -> bool:
        """
        Z-TRUST-IMPLEMENTATION: Valida si existe un mandato legal/técnico (Tratado)
        que autorice el intercambio de esta señal con el nodo especificado.
        """
        from apps.operational_treaties.models import OperationalTreaty

        # 1. Buscar tratados activos que incluyan al nodo
        active_treaties = OperationalTreaty.objects.filter(
            is_active=True,
            participating_nodes__contains=node_id
        )

        for treaty in active_treaties:
            # 2. Verificar si el tipo de señal está permitido
            if signal_type in treaty.signal_types_allowed:
                # 3. Verificar permisos de dirección
                required_perm = 'EMIT_SIGNALS' if direction == 'OUTGOING' else 'RECEIVE_SIGNALS'
                if treaty.permissions_granted.get(required_perm, False):
                    logger.info(f"KERNEL: Mandato VALIDADO para '{signal_type}' con {node_id} vía {treaty.name}")
                    return True

        logger.error(f"KERNEL: Mandato RECHAZADO para '{signal_type}' con {node_id}. Sin tratado habilitante.")
        return False

    def resolve_and_execute(self, intention_name: str, parameters: Dict[str, Any], bypass_policy: bool = False) -> Dict[str, Any]:
        """
        Punto de entrada único para ejecutar intenciones.
        """
        logger.info(f"KERNEL: Recibida intención '{intention_name}' de usuario {self.user.username}")

        # 0. EVALUACIÓN DE LEGADO (FASE LEGADO) - PRIORIDAD MÁXIMA
        intention_obj = self._registry.get(intention_name)
        if intention_obj:
            self._evaluate_legacy_protections(intention_obj, parameters)

        # Z-GOVERNANCE-LIVE: Verificación de Restricciones por Estado Sistémico
        current_state = self.get_current_systemic_state()
        if current_state in ['CONTAINMENT', 'PARTIAL_DECOUPLING', 'TOTAL_DECOUPLING'] and not self.user.is_superuser:
            logger.warning(f"KERNEL: Bloqueo por Estado '{current_state}'. Intención '{intention_name}' RECHAZADA.")
            raise PermissionError(f"SISTEMA EN MODO {current_state}: La autonomía delegada está restringida para preservar la integridad nacional.")

        # Z-GOVERNANCE-LIVE: Barreras Anti-Deriva (Protección contra expansión de mandato)
        intention = self._registry.get(intention_name)
        if intention and hasattr(self.user, 'is_agent') and self.user.is_agent:
            # Si el usuario es un agente (Funcionario Digital), validamos su dominio asignado
            if intention.domain != self.user.agent_domain and not self.user.is_superuser:
                logger.error(f"ANTI-DRIFT: Agente de '{self.user.agent_domain}' intentó acceder a '{intention.domain}'. BLOQUEADO.")
                raise PermissionError(f"DERIVA DETECTADA: El Funcionario Digital de '{self.user.agent_domain}' no tiene mandato para operar en el dominio '{intention.domain}'.")

        # Z-OPERATIONAL: Protocolo de Desaceleración Algorítmica (PDA)
        # Si existe una política de desaceleración activa, forzamos intervención humana en intenciones de nivel DELEGATED
        pda_active = GovernancePolicy.objects.filter(name="ALGORITHMIC_DECELERATION_PROTOCOL", is_active=True).exists()
        if pda_active:
            intention = self._registry.get(intention_name)
            if intention and intention.min_authority == AuthorityLevel.DELEGATED and not self.user.is_superuser:
                logger.warning(f"PDA: Intención '{intention_name}' bloqueada por Desaceleración Algorítmica. Requiere Autoridad Soberana.")
                raise PermissionError("PROTOCOLO DE DESACELERACIÓN ACTIVO: Esta acción delegada ha sido suspendida temporalmente para preservar la estabilidad. Requiere autorización manual del SuperAdmin.")

        # S-0.5: Verificación de MODO ATAQUE (Congelamiento Sistémico)
        attack_mode = GovernancePolicy.objects.filter(name="SYSTEM_ATTACK_MODE", is_active=True).exists()
        if attack_mode and not self.user.is_superuser:
            # En modo ataque, solo el SuperAdmin (Autoridad Soberana) puede ejecutar acciones Críticas
            # El resto de usuarios están bloqueados para prevenir propagación de compromiso.
            logger.warning(f"S-0: Intención '{intention_name}' RECHAZADA. Sistema en MODO ATAQUE.")
            raise PermissionError("SISTEMA CONGELADO: Se ha detectado una amenaza activa. Todas las operaciones de escritura están suspendidas por seguridad institucional.")

        # 1. Resolver intención
        intention = self._registry.get(intention_name)
        if not intention:
            # S-0.3: Intento de inyectar intención desconocida es una amenaza
            DefenseService.neutralize_threat(
                user=self.user,
                attack_vector="INVALID_INTENTION_INJECTION",
                payload={"intention_name": intention_name, "params": parameters},
                headers={}, # Deberían pasarse desde la vista
                threat_level='HIGH'
            )
            raise ValueError(f"Intención '{intention_name}' no reconocida por el núcleo de gobernanza. Acción registrada.")

        # 2. Validar Contrato (Requisitos de parámetros)
        self._validate_contract(intention, parameters)

        # 3. Validar Autoridad Soberana
        try:
            self._validate_authority(intention)
        except PermissionError as e:
            # S-0.3: Violación de autoridad en el Kernel es una amenaza interna/externa
            DefenseService.neutralize_threat(
                user=self.user,
                attack_vector="GOVERNANCE_AUTHORITY_VIOLATION",
                payload={"intention_name": intention_name, "error": str(e)},
                headers={},
                threat_level='CRITICAL'
            )
            raise e

        # 5. Evaluar Políticas Globales (Motor de Políticas)
        if not bypass_policy:
            self._evaluate_policies(intention, parameters)

        # 5. Coordinar y Ejecutar
        try:
            with transaction.atomic():
                result = self._dispatch(intention, parameters)

                # 4. Auditoría Sistémica Unificada
                self._log_audit(intention, parameters, result)

                return result
        except Exception as e:
            logger.error(f"KERNEL: Error ejecutando '{intention_name}': {str(e)}")
            self._log_audit(intention, parameters, {}, success=False, error_message=str(e))
            raise e

    def _validate_contract(self, intention: GovernanceIntention, parameters: Dict[str, Any]):
        """
        Valida que los parámetros cumplan con el contrato de la intención.
        """
        missing = [p for p in intention.required_params if p not in parameters]
        if missing:
            raise ValueError(f"Contrato violado para '{intention.name}': Faltan parámetros requeridos: {missing}")

    def _validate_authority(self, intention: GovernanceIntention):
        """
        Verifica el nivel de autoridad y rol del usuario.
        """
        # El SuperAdmin ostenta Autoridad Soberana absoluta
        if self.user.is_superuser:
            return True

        # Validar jerarquía mínima requerida
        user_authority = self._get_user_authority_level()
        if user_authority < intention.min_authority:
            raise PermissionError(f"Nivel de autoridad insuficiente. Requerido: {intention.min_authority.name}")

        if self.user.role != intention.required_role:
             raise PermissionError(f"El usuario no tiene el rol '{intention.required_role}' requerido para '{intention.name}'.")

        return True

    def _get_user_authority_level(self) -> AuthorityLevel:
        if self.user.is_superuser:
            return AuthorityLevel.SOVEREIGN
        if self.user.role in [CustomUser.Role.ADMIN, CustomUser.Role.FUNCIONARIO_DIRECTIVO]:
            return AuthorityLevel.DELEGATED
        return AuthorityLevel.OPERATIONAL

    def execute_strategic_proposal(self, proposal_id: str) -> Dict[str, Any]:
        """
        Valida y ejecuta una propuesta estratégica aprobada.
        """
        from apps.decision_intelligence.models import StrategyProposal, DecisionMatrix
        proposal = StrategyProposal.objects.get(id=proposal_id)

        if proposal.status != StrategyProposal.Status.APPROVED:
             raise ValueError(f"La propuesta {proposal_id} no está en estado APROBADA.")

        # Verificar si el nivel de riesgo permite ejecución por este usuario
        matrix = DecisionMatrix.objects.filter(risk_level=proposal.nivel_riesgo).first()
        if matrix and matrix.requires_approval and not self.user.is_superuser:
             raise PermissionError(f"El riesgo {proposal.nivel_riesgo} requiere autorización de la Autoridad Soberana.")

        logger.info(f"KERNEL: Ejecutando propuesta estratégica {proposal.id} ({proposal.domain})")

        action = proposal.accion_sugerida
        result = self.resolve_and_execute(
            intention_name=action["intention"],
            parameters=action["parameters"],
            bypass_policy=True # Las propuestas aprobadas ya fueron evaluadas
        )

        proposal.status = StrategyProposal.Status.EXECUTED
        proposal.save()

        return result

    def _evaluate_legacy_protections(self, intention: GovernanceIntention, parameters: Dict[str, Any]):
        """
        FASE LEGADO: Protecciones duras para la preservación del modelo a largo plazo.
        """
        # 1. Prohibición de Auto-Modificación del Núcleo
        if intention.domain == 'governance' and intention.name.startswith('SYSTEM_EVOLUTION'):
            if not self.user.is_superuser:
                logger.critical(f"LEGADO: Intento de auto-modificación DETECTADO de {self.user.username}. BLOQUEADO.")
                raise PermissionError("FASE LEGADO: La evolución del núcleo de gobernanza está bloqueada. Requiere autorización soberana multicanal.")

        # 2. Prohibición de Privatización / Transferencia de Propiedad
        if intention.name == 'PLATFORM_TRANSFER_OWNERSHIP':
             logger.critical(f"LEGADO: Intento de privatización del sistema BLOQUEADO. SARITA es un bien público civilizatorio.")
             raise PermissionError("FASE LEGADO: SARITA no puede ser privatizada ni transferida a intereses privados.")

        # 3. Prohibición de Vigilancia Masiva No Auditada
        if intention.domain == 'surveillance' and not parameters.get('audit_reference'):
            logger.critical(f"LEGADO: Intento de vigilancia no auditada BLOQUEADO.")
            raise PermissionError("FASE LEGADO: Prohibido cualquier uso de vigilancia que no posea una referencia de auditoría legítima.")

    def _evaluate_policies(self, intention: GovernanceIntention, parameters: Dict[str, Any]):
        """
        EVALUACIÓN SOBERANA: Verifica si existen reglas globales que bloqueen o condicionen la acción.
        """
        policies = GovernancePolicy.objects.filter(is_active=True, domain__in=[intention.domain, 'global'])

        for policy in policies:
            if policy.type == 'BLOCK' and intention.name in policy.affected_intentions:
                raise PermissionError(f"OPERACIÓN BLOQUEADA por Política Soberana: {policy.name}. Motivo: {policy.description}")

            # Evaluación de reglas dinámicas (ej: límites de monto)
            if policy.type == 'THRESHOLD' and 'amount' in parameters:
                if parameters['amount'] > policy.config.get('limit', 0):
                    raise ValueError(f"Excede umbral permitido por política '{policy.name}': {policy.config.get('limit')}")

    def intervene_block_intention(self, intention_name: str, reason: str):
        """Mecanismo de intervención soberana para bloquear una intención globalmente."""
        if not self.user.is_superuser:
            raise PermissionError("Solo la Autoridad Soberana puede ejecutar bloqueos sistémicos.")

        GovernancePolicy.objects.update_or_create(
            name=f"BLOQUEO_SOBERANO_{intention_name}",
            defaults={
                'description': reason,
                'type': 'BLOCK',
                'domain': 'global',
                'affected_intentions': [intention_name],
                'is_active': True
            }
        )
        logger.warning(f"INTERVENCIÓN SOBERANA: Bloqueada intención '{intention_name}' por {self.user.username}")

    def intervene_authorize_critical(self, intention_name: str, parameters: Dict[str, Any]):
        """Permite al SuperAdmin forzar la ejecución de una intención ignorando bloqueos no soberanos."""
        if not self.user.is_superuser:
            raise PermissionError("Solo la Autoridad Soberana puede autorizar operaciones críticas manualmente.")

        logger.info(f"INTERVENCIÓN SOBERANA: Autorización manual de '{intention_name}'")
        # Saltamos validación de políticas y autoridad regular
        with transaction.atomic():
            result = self._dispatch(self._registry[intention_name], parameters)
            self._log_audit(
                self._registry[intention_name],
                parameters,
                result,
                success=True,
                error_message="AUTORIZACIÓN_SOBERANA_MANUAL",
                is_sovereign=True
            )
            return result

    def _dispatch(self, intention: GovernanceIntention, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la ejecución al servicio de dominio correspondiente.
        """
        from .gestion_plataforma_service import GestionPlataformaService
        service = GestionPlataformaService(admin_user=self.user)

        if intention.name == "PLATFORM_CREATE_PLAN":
            plan = service.crear_plan(
                nombre=parameters["nombre"],
                precio=parameters["precio"],
                frecuencia=parameters["frecuencia"],
                descripcion=parameters.get("descripcion", "")
            )
            return {"status": "SUCCESS", "id": plan.id, "message": f"Plan '{plan.nombre}' creado.", "instance": plan}

        # Futuras intenciones se mapean aquí
        return {"status": "SUCCESS", "message": f"Intención '{intention.name}' procesada correctamente."}

    def _log_audit(self, intention: GovernanceIntention, parameters: Dict[str, Any], result: Dict[str, Any], success: bool = True, error_message: str = None, is_sovereign: bool = False):
        """
        Registra la acción en el log de auditoría sistémica con Hardening RC-S (Hashes).
        """
        import hashlib
        import json

        try:
             # Obtener el hash del registro anterior para encadenamiento
             last_log = GovernanceAuditLog.objects.order_by('-timestamp').first()
             previous_hash = last_log.integrity_hash if last_log else "SARITA_GENESIS_BLOCK"

             # Crear log base
             log_entry = GovernanceAuditLog(
                 usuario=self.user,
                 intencion=intention.name,
                 parametros=parameters,
                 resultado=result,
                 success=success,
                 error_message=error_message,
                 es_intervencion_soberana=is_sovereign,
                 previous_hash=previous_hash
             )

             # Calcular Integrity Hash (RC-S Hardening)
             payload = f"{log_entry.intencion}{json.dumps(log_entry.parametros)}{log_entry.timestamp}{previous_hash}{success}"
             log_entry.integrity_hash = hashlib.sha256(payload.encode()).hexdigest()

             log_entry.save()
             logger.info(f"AUDIT KERNEL (RC-S): Usuario={self.user.username}, Acción={intention.name}, Hash={log_entry.integrity_hash[:8]}")
        except Exception as e:
            logger.error(f"Error al registrar auditoría en el Kernel: {e}")

# --- REGISTRO DE INTENCIONES INICIALES (Fase 3.5 + Refuerzo Fase 3) ---

# Dominio: Plataforma
GovernanceKernel.register_intention(GovernanceIntention(
    name="PLATFORM_CREATE_PLAN",
    domain="plataforma",
    required_role=CustomUser.Role.ADMIN,
    required_params=["nombre", "precio", "frecuencia"],
    min_authority=AuthorityLevel.DELEGATED
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="PLATFORM_SUSPEND_USER",
    domain="plataforma",
    required_role=CustomUser.Role.ADMIN,
    required_params=["user_id", "motivo"],
    min_authority=AuthorityLevel.SOVEREIGN # Solo SuperAdmin o nivel muy alto
))

# Dominio: ERP Sistémico (Comercial)
GovernanceKernel.register_intention(GovernanceIntention(
    name="ERP_CONFIRM_SALE",
    domain="comercial",
    required_role=CustomUser.Role.ADMIN,
    required_params=["operacion_id"],
    min_authority=AuthorityLevel.OPERATIONAL
))

# Dominio: ERP Sistémico (Contable)
GovernanceKernel.register_intention(GovernanceIntention(
    name="ERP_GENERATE_BALANCE",
    domain="contable",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED
))

# Dominio: Seguridad y Salud (SG-SST)
GovernanceKernel.register_intention(GovernanceIntention(
    name="SST_REGISTER_INCIDENT",
    domain="seguridad_civil",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.OPERATIONAL,
    required_params=["tipo", "gravedad", "descripcion"]
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="SST_BLOCK_OPERATION",
    domain="seguridad_civil",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED,
    required_params=["proceso_id", "motivo"]
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="SST_UPDATE_RISK_MATRIX",
    domain="planeacion",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED
))

# Dominio: FASE LEGADO
GovernanceKernel.register_intention(GovernanceIntention(
    name="GENERATE_LEGACY_BUNDLE",
    domain="governance",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.SOVEREIGN
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="PLATFORM_TRANSFER_OWNERSHIP",
    domain="plataforma",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.SOVEREIGN
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="SYSTEM_EVOLUTION_HARDENING",
    domain="governance",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.SOVEREIGN
))

# Dominio: FASE META
GovernanceKernel.register_intention(GovernanceIntention(
    name="QUERY_META_STANDARD",
    domain="governance",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.OPERATIONAL
))

# --- DOMINIOS INSTITUCIONALES (Fase Z-INSTITUTIONAL) ---

# Dominio: Hacienda / Finanzas Públicas
GovernanceKernel.register_intention(GovernanceIntention(
    name="PUBLIC_BUDGET_OPTIMIZATION",
    domain="hacienda",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.SOVEREIGN
))

# Dominio: Planeación Nacional
GovernanceKernel.register_intention(GovernanceIntention(
    name="TERRITORIAL_IMPACT_SIMULATION",
    domain="planeacion",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED
))

# Dominio: Seguridad Civil
GovernanceKernel.register_intention(GovernanceIntention(
    name="CIVIL_DEFENSE_ALERT",
    domain="seguridad_civil",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.OPERATIONAL
))

# Dominio: Gestión Territorial
GovernanceKernel.register_intention(GovernanceIntention(
    name="LAND_USE_AUDIT",
    domain="gestion_territorial",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="ERP_CREATE_VOUCHER",
    domain="contable",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.OPERATIONAL,
    required_params=["valor", "concepto"]
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="ERP_VIEW_SALES_STATS",
    domain="comercial",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.OPERATIONAL
))

# Dominio: Autonomía IA (Fase F-F)
GovernanceKernel.register_intention(GovernanceIntention(
    name="PRIORITIZE_CRITICAL_LEADS",
    domain="comercial",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED # Autonomía actúa con autoridad delegada
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="OPTIMIZE_MARKETING_BUDGET",
    domain="comercial",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="ERP_VIEW_CASH_FLOW",
    domain="financiero",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.OPERATIONAL
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="ERP_MANAGE_RESOURCES",
    domain="operativo",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="ERP_SEARCH_DOCUMENT",
    domain="archivistico",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.OPERATIONAL,
    required_params=["query"]
))

# Dominio: Decision Intelligence (Nuevas intenciones propuestas por IA)
GovernanceKernel.register_intention(GovernanceIntention(
    name="PLATFORM_UPDATE_PLAN",
    domain="plataforma",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="PLATFORM_OPTIMIZE_RESOURCES",
    domain="plataforma",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="PLATFORM_UPDATE_WEB_CMS",
    domain="plataforma",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="PLATFORM_UPDATE_LEGAL",
    domain="plataforma",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.SOVEREIGN
))

# Dominio: Inteligencia Operativa
GovernanceKernel.register_intention(GovernanceIntention(
    name="ONBOARDING_PRESTADOR",
    domain="prestadores",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.OPERATIONAL
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="AUDITORIA_GLOBAL",
    domain="administrador_general",
    required_role=CustomUser.Role.ADMIN,
    min_authority=AuthorityLevel.DELEGATED
))
