import json
from kafka import KafkaProducer

class SaritaEventProducer:
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            acks='all',
            retries=5
        )

    def produce(self, topic, event_type, payload, trace_id, tenant_id):
        event = {
            "header": {
                "trace_id": trace_id,
                "tenant_id": tenant_id,
                "event_type": event_type,
                "timestamp": "2024-05-22T00:00:00Z"
            },
            "payload": payload
        }
        future = self.producer.send(topic, event)
        return future.get(timeout=10)

if __name__ == "__main__":
    p = SaritaEventProducer()
    res = p.produce(
        "sarita.finance.events",
        "PAYMENT_INITIATED",
        {"amount": 100.50, "currency": "USD"},
        "trace-abc-123",
        "tenant-master"
    )
    print(f"Event sent: {res}")
