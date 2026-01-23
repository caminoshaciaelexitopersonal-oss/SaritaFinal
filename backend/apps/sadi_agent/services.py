# sadi_agent/services.py

import json
from .models import SadiAuditLog

# Importación de los servicios "Ejecutores"
# from apps.cart.services import CartService
# from apps.orders.services import OrderService
# from apps.payments.services import PaymentService
from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService

# NOTA: La lógica de publicaciones aún reside en el ViewSet.
# Se instanciará cuando sea necesario.
from api.views import AdminPublicacionViewSet


class SadiOrquestadorService:
    """
    Servicio central que orquesta el procesamiento de comandos de voz.
    """

    def __init__(self):
        # Mapeo de intenciones a las funciones de servicio correspondientes.
        # Esto centraliza el enrutamiento de comandos.
        self.COMMAND_MAP = {
            # Gestión de Contenidos (Simulado por ahora)
            'PUBLICAR_PAGINA': self.handle_not_implemented,
            'OCULTAR_PAGINA': self.handle_not_implemented,

            # Gestión de Planes
            'CREAR_PLAN': self.handle_crear_plan,
            'DESACTIVAR_PLAN': self.handle_not_implemented,

            # Gestión de Publicaciones
            'APROBAR_PUBLICACION': self.handle_aprobar_publicacion,
            'RECHAZAR_PUBLICACION': self.handle_rechazar_publicacion,
        }

    def process_voice_command(self, texto_comando: str, usuario):
        """
        Punto de entrada principal para procesar un comando de voz.
        """
        log_entry = SadiAuditLog.objects.create(
            usuario=usuario,
            comando_original=texto_comando,
            resultado="Iniciando procesamiento..."
        )

        try:
            # 1. Clasificación de Intención (Simulación con LLM)
            # En una implementación real, aquí iría la llamada a langchain.
            # Por ahora, simulamos la respuesta del LLM basada en palabras clave.
            parsed_action = self._simulated_llm_parse(texto_comando)
            log_entry.accion_ejecutada = parsed_action
            log_entry.save()

            intent = parsed_action.get("accion")
            params = parsed_action.get("parametros", {})

            if not intent or intent not in self.COMMAND_MAP:
                raise ValueError("No se pudo determinar la intención del comando.")

            # 2. Validación de Permisos (Simplificado)
            # En un sistema real, esto sería más robusto.
            if not usuario.is_staff:
                raise PermissionError("El usuario no tiene permisos para ejecutar comandos de SADI.")

            # 3. Mapeo y Ejecución
            handler_method = self.COMMAND_MAP[intent]

            # 4. Gestión de Confirmación (Añadir en el futuro)
            # if self._is_critical(intent):
            #     return self._request_confirmation(log_entry, handler_method, **params)

            resultado = handler_method(usuario=usuario, **params)

            log_entry.resultado = json.dumps({"status": "success", "message": resultado})
            log_entry.save()

            return resultado

        except Exception as e:
            log_entry.resultado = json.dumps({"status": "error", "message": str(e)})
            log_entry.save()
            return f"Error al procesar el comando: {str(e)}"

    def _simulated_llm_parse(self, texto: str) -> dict:
        """
        Simula la clasificación de intención y extracción de parámetros de un LLM.
        """
        texto = texto.lower()
        if "crear" in texto and "plan" in texto:
            # Ejemplo: "crear plan premium con precio 29.99 mensual"
            parts = texto.split()
            nombre = parts[parts.index("plan") + 1]
            precio = parts[parts.index("precio") + 1]
            frecuencia = parts[parts.index(precio) + 1].upper()
            return {"accion": "CREAR_PLAN", "parametros": {"nombre": nombre, "precio": precio, "frecuencia": frecuencia}}

        if "aprobar" in texto and "publicación" in texto:
            parts = texto.split()
            pub_id = int(parts[parts.index("publicación") + 1])
            return {"accion": "APROBAR_PUBLICACION", "parametros": {"publicacion_id": pub_id}}

        if "rechazar" in texto and "publicación" in texto:
            parts = texto.split()
            pub_id = int(parts[parts.index("publicación") + 1])
            return {"accion": "RECHAZAR_PUBLICACION", "parametros": {"publicacion_id": pub_id}}

        return {}

    # --- Handlers de Comandos ---

    def handle_crear_plan(self, usuario, nombre: str, precio: str, frecuencia: str):
        """Ejecutor para la creación de planes."""
        service = GestionPlataformaService(admin_user=usuario)
        plan = service.crear_plan(nombre=nombre, precio=precio, frecuencia=frecuencia)
        return f"Plan '{plan.nombre}' creado con éxito con ID {plan.id}."

    def handle_aprobar_publicacion(self, usuario, publicacion_id: int):
        """Ejecutor para aprobar publicaciones."""
        viewset = AdminPublicacionViewSet()
        viewset.request = type('Request', (), {'user': usuario})() # Mock request
        viewset.kwargs = {'pk': publicacion_id}
        viewset.approve(viewset.request)
        return f"Publicación {publicacion_id} aprobada."

    def handle_rechazar_publicacion(self, usuario, publicacion_id: int):
        """Ejecutor para rechazar publicaciones."""
        viewset = AdminPublicacionViewSet()
        viewset.request = type('Request', (), {'user': usuario})() # Mock request
        viewset.kwargs = {'pk': publicacion_id}
        viewset.reject(viewset.request)
        return f"Publicación {publicacion_id} rechazada."

    def handle_not_implemented(self, **kwargs):
        return "Funcionalidad no implementada todavía."


# Instancia única del servicio
sadi_orquestador_service = SadiOrquestadorService()
