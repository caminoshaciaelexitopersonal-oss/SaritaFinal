"""
Módulo de Enrutamiento de Órdenes (Router).

Basado en la intención identificada y el contexto del usuario, este módulo
decide cuál de los agentes Coroneles es el más adecuado para manejar la
orden.
"""

class Router:
    """
    Determina el dominio y el Coronel responsable para una intención dada.
    """

    def __init__(self):
        """
        Inicializa el router. Podría cargar un mapa de rutas o reglas.
        """
        # Mapa que asocia entidades (o intenciones) a un dominio/Coronel
        self.routing_table = {
            "invoice": "comercial",
            "product": "comercial",
            "client": "comercial",
            "inventory": "operativo",
            "reservation": "operativo",
            "document": "archivistico",
            "financial_report": "financiero",
            "balance_sheet": "contable"
            # ... y así sucesivamente
        }
        print("Router: Tabla de enrutamiento cargada. Listo para dirigir órdenes.")

    def determine_coronel(self, intent: dict) -> str:
        """
        Analiza la intención y devuelve el nombre del Coronel responsable.

        Args:
            intent (dict): La intención estructurada del IntentParser.

        Returns:
            str: El identificador del Coronel (ej. "coronel_comercial").
        """
        entity = intent.get("entity")

        print(f"ROUTER: Buscando destino para la entidad '{entity}'")

        domain = self.routing_table.get(entity, "default") # 'default' podría ser un Coronel de fallback

        if domain == "default":
            print("ROUTER: No se encontró una ruta específica. Usando Coronel por defecto.")
            # Podrías tener una lógica más compleja aquí, por ejemplo,
            # usar un LLM para decidir en casos ambiguos.

        target_coronel = f"coronel_{domain}"
        print(f"ROUTER: Destino determinado: {target_coronel}")

        return target_coronel
