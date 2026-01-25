# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/capitanes/dummy_capitan.py
from typing import Dict, Any

class DummyCapitan:
    """
    Un capitán de marcador de posición para probar el flujo de delegación.
    """
    def __init__(self, coronel):
        self.coronel = coronel
        print(f"CAPITÁN (DummyCapitan): Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simula el manejo de una orden.
        """
        print(f"CAPITÁN (DummyCapitan): Orden recibida -> {order}")

        report = {
            "captain": self.__class__.__name__,
            "order_id": order.get('id', 'N/A'),
            "status": "SIMULATED_SUCCESS",
            "details": "La orden fue recibida y procesada por el capitán dummy."
        }

        return report
