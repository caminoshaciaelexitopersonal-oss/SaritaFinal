"""
Módulo de Gestión de Contexto.

Este componente se encarga de recopilar, gestionar y enriquecer el contexto
relacionado con una orden. El contexto es crucial para que los agentes tomen
decisiones precisas.
"""

class ContextManager:
    """
    Gestiona el contexto del usuario, la sesión y el sistema.
    """

    def __init__(self):
        """
        Inicializa el gestor de contexto.
        """
        self.current_context = {}
        print("Gestor de Contexto: Activo.")

    def build_context(self, user_metadata: dict, session_data: dict = None) -> dict:
        """
        Construye un contexto completo a partir de varias fuentes.

        Args:
            user_metadata (dict): Información estática del usuario (ID, rol, tenant).
            session_data (dict, optional): Datos de la sesión actual (historial reciente, etc.).

        Returns:
            dict: Un objeto de contexto unificado.
        """
        print(f"CONTEXT: Construyendo contexto para el usuario: {user_metadata.get('user_id')}")

        # Copia base de los metadatos del usuario
        self.current_context = user_metadata.copy()

        # Enriquecer con información del sistema
        # Ejemplo: Obtener permisos detallados basados en el rol
        permissions = self._get_permissions_for_role(self.current_context.get("rol"))
        self.current_context['permissions'] = permissions

        # Incorporar datos de la sesión si existen
        if session_data:
            self.current_context.update(session_data)

        print(f"CONTEXT: Contexto final construido: {self.current_context}")
        return self.current_context

    def get_context(self) -> dict:
        """
        Devuelve el contexto actual.
        """
        return self.current_context

    def _get_permissions_for_role(self, role: str) -> list:
        """
        Simulación de una función que obtiene permisos basados en el rol.
        """
        if role == "empresario":
            return ["create_invoice", "view_products", "manage_inventory"]
        elif role == "gobernanza":
            return ["view_reports", "approve_requests"]
        elif role == "turista":
            return ["view_destinations", "make_reservations"]
        return ["guest"]

# Puedes expandir esto para cargar contexto desde la base de datos,
# una caché, o un servicio de perfiles de usuario.
