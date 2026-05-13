import json
import logging
from kafka import KafkaProducer, KafkaConsumer
from opentelemetry import trace

class KafkaRuntimeBus:
    def __init__(self, brokers=['localhost:9092']):
        self.producer = KafkaProducer(
            bootstrap_servers=brokers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            acks='all'
        )
        self.tracer = trace.get_tracer(__name__)

    def publish_event(self, topic, payload, context_headers):
        # 50.1 - Real Kafka event publication with propagation
        with self.tracer.start_as_current_span("kafka_publish") as span:
            event = {
                "headers": {
                    "trace_id": context_headers.get('trace_id'),
                    "tenant_id": context_headers.get('tenant_id'),
                    "workflow_id": context_headers.get('workflow_id'),
                    "correlation_id": context_headers.get('correlation_id')
                },
                "payload": payload
            }
            self.producer.send(topic, event)
            logging.info(f"REAL_EVENT_PUBLISHED: {topic}")
            return True

    def create_consumer(self, topics, group_id):
        return KafkaConsumer(
            *topics,
            bootstrap_servers=['localhost:9092'],
            group_id=group_id,
            enable_auto_commit=False,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
