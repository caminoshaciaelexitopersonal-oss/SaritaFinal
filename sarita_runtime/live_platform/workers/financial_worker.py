import asyncio
import json
import logging
from kafka import KafkaConsumer, KafkaProducer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FinancialWorker")

class FinancialWorker:
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.bootstrap_servers = bootstrap_servers
        self.consumer = None
        self.producer = None
        self.running = True

    async def initialize(self):
        logger.info("Initializing Kafka Consumer/Producer...")
        self.consumer = KafkaConsumer(
            'sarita.finance.events',
            bootstrap_servers=self.bootstrap_servers,
            group_id='sarita-finance-group',
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    async def process_event(self, event):
        # Implementation of real financial logic: ledger entry, tax calculation, etc.
        logger.info(f"Processing financial event: {event.get('header', {}).get('event_type')}")
        await asyncio.sleep(0.1) # Simulate I/O
        return True

    async def run(self):
        await self.initialize()
        logger.info("Financial Worker Running...")
        try:
            while self.running:
                msg_pack = self.consumer.poll(timeout_ms=1000)
                for tp, messages in msg_pack.items():
                    for msg in messages:
                        success = await self.process_event(msg.value)
                        if success:
                            self.consumer.commit()
                await asyncio.sleep(0.1)
        except Exception as e:
            logger.error(f"Worker crashed: {e}")
        finally:
            self.consumer.close()
            logger.info("Financial Worker Shutdown.")

if __name__ == "__main__":
    worker = FinancialWorker()
    asyncio.run(worker.run())
