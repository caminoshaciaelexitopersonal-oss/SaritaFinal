import logging

class DeterministicInterruptDispatcher:
    """
    Dispatches interrupt handling tasks registered in UnifiedExecutionGraph.
    """
    def __init__(self, graph):
        self.graph = graph

    def handle_irq_event(self, irq_id: int, epoch: int):
        logging.info(f"IRQ Dispatcher: Registering IRQ {irq_id} in Epoch {epoch}")
        # Material registration of the IRQ physical hit
        self.graph.register_material_execution(f"IRQ-{irq_id}-{epoch}", {"type": "IRQ_HIT", "irq_id": irq_id})
        return True
