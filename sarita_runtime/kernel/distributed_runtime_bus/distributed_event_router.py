import logging

class DistributedEventRouter:
    def __init__(self, runtime_bus):
        self.bus = runtime_bus
        self.routing_table = {
            "FINANCE": "sarita.finance.events",
            "AI": "sarita.ai.decisions",
            "GOVERNANCE": "sarita.governance.isolation"
        }

    def route(self, domain, event_type, payload, context):
        topic = self.routing_table.get(domain)
        if topic:
            logging.info(f"Routing {event_type} to topic {topic}")
            return self.bus.publish_event(topic, payload, context)
        return False
