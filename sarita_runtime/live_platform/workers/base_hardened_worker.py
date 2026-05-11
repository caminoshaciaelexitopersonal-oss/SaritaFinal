import asyncio
import json
import logging
from kafka import KafkaConsumer
from opentelemetry import trace

logger = logging.getLogger("HardenedWorker")

class BaseWorker:
    def __init__(self, topic, group_id):
        self.topic = topic
        self.group_id = group_id
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=['localhost:9092'],
            group_id=self.group_id,
            enable_auto_commit=False,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        self.tracer = trace.get_tracer(__name__)

    async def run(self):
        logger.info(f"Worker {self.group_id} started on topic {self.topic}")
        while True:
            msg_pack = self.consumer.poll(timeout_ms=1000)
            for tp, messages in msg_pack.items():
                for msg in messages:
                    with self.tracer.start_as_current_span("process_event") as span:
                        success = await self.safe_process(msg.value, span)
                        if success:
                            self.consumer.commit()
            await asyncio.sleep(0.1)

    async def safe_process(self, event, span):
        try:
            # Implement Circuit Breaker logic here
            return await self.handle_event(event)
        except Exception as e:
            logger.error(f"Process Error: {e}")
            # Send to DLQ logic
            return False

    async def handle_event(self, event):
        raise NotImplementedError("Subclasses must implement handle_event")
