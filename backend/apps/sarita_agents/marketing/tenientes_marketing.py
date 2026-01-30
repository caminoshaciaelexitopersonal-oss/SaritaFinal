# backend/apps/sarita_agents/agents/marketing/tenientes_marketing.py
import logging
from apps.sarita_agents.agents.teniente_template import TenienteTemplate
from api.models import CustomUser
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

logger = logging.getLogger(__name__)

class TenienteCalificacion(TenienteTemplate):
    """Identifica el tipo de usuario y su nivel digital."""
    def perform_action(self, parametros: dict):
        text = parametros.get("text", "").lower()
        # Lógica heurística de calificación
        tipo = "curioso"
        if "vender" in text or "negocio" in text or "prestador" in text:
            tipo = "prestador"
        elif "gobierno" in text or "plataforma" in text or "secretaria" in text:
            tipo = "gobierno"

        return {"tipo_usuario": tipo, "score_calificacion": 0.8}

class TenienteDolor(TenienteTemplate):
    """Detecta el problema principal del prospecto."""
    def perform_action(self, parametros: dict):
        text = parametros.get("text", "").lower()
        dolor = "desorden"
        if "dinero" in text or "precio" in text or "perder" in text:
            dolor = "perdida_financiera"
        elif "tiempo" in text or "lento" in text:
            dolor = "falta_tiempo"

        return {"dolor_detectado": dolor}

class TenienteOferta(TenienteTemplate):
    """Sugiere un plan basado en la calificación y el dolor."""
    def perform_action(self, parametros: dict):
        tipo = parametros.get("tipo_usuario", "prestador")
        dolor = parametros.get("dolor_detectado", "desorden")

        oferta = "Plan Básico"
        if tipo == "gobierno":
            oferta = "Sarita Governance Pro"
        elif dolor == "perdida_financiera":
            oferta = "Plan Premium (Enfoque Rentabilidad)"

        return {"oferta_sugerida": oferta, "valor_diferencial": "Sarita organiza tus ventas y evita que pierdas dinero."}

class TenienteObjeciones(TenienteTemplate):
    """Maneja dudas comunes."""
    def perform_action(self, parametros: dict):
        objecion = parametros.get("objecion", "ninguna")
        respuesta = "Entiendo. Sarita está diseñada para ser intuitiva y ahorrarte tiempo desde el primer día."

        if "caro" in objecion:
            respuesta = "Más que un gasto, es una inversión que se paga sola al recuperar ventas perdidas por desorden."

        return {"respuesta_objecion": respuesta}

class TenienteCierre(TenienteTemplate):
    """Ejecuta el registro o suscripción simulada."""
    def perform_action(self, parametros: dict):
        # En Phase 4-M, esto podría crear un lead o un usuario pre-registrado
        email = parametros.get("email")
        if not email:
            return {"status": "AWAITING_EMAIL", "message": "Necesito tu correo para crear la cuenta."}

        return {"status": "CONVERSION_READY", "email": email, "action": "onboarding_triggered"}
