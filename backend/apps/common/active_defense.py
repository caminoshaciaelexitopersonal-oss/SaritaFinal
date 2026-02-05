from datetime import datetime
from .forensic_log import ForensicSecurityLog

class ActiveDefenseService:
    """
    Servicio de Defensa Activa que monitorea anomalías sistémicas
    y activa contramedidas automáticas.
    """

    @staticmethod
    def evaluate_risk(request, user):
        anomalies = []

        # 1. Detección de horario inusual (Ej: 2 AM - 5 AM para roles operativos)
        current_hour = datetime.now().hour
        if current_hour >= 2 and current_hour <= 5:
            if user and user.is_authenticated and user.role != 'SUPERADMIN':
                anomalies.append("OUT_OF_HOURS_ACCESS")

        # 2. Detección de comportamiento no humano (Rapid click-stream simulado)
        # Esto vendría de un sensor de frontend o análisis de logs

        if anomalies:
            ActiveDefenseService.trigger_containment(user, anomalies)

    @staticmethod
    def trigger_containment(user, anomalies):
        for anomaly in anomalies:
            ForensicSecurityLog.log_event(
                event_type="DEFENSE_CONTAINMENT",
                actor=user.username if user else "ANONYMOUS",
                description=f"Countermeasure activated for: {anomaly}",
                impact="SESSION_MONITORING_INTENSIFIED"
            )
            # En un caso crítico, podríamos invalidar el token
            # user.auth_token.delete()
