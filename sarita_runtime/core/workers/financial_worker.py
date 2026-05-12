import asyncio
import json
import logging
import os
import psycopg2
from kafka import KafkaConsumer
from opentelemetry import trace

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RealFinancialWorker")

class FinancialWorker:
    def __init__(self):
        self.db_url = os.getenv("DATABASE_URL")
        self.kafka_brokers = os.getenv("KAFKA_BROKERS", "localhost:9092")
        self.consumer = KafkaConsumer(
            'sarita.finance.events',
            bootstrap_servers=self.kafka_brokers,
            group_id='finance-runtime-group',
            enable_auto_commit=False,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        self.tracer = trace.get_tracer(__name__)

    async def run(self):
        logger.info("Real Financial Worker started. Listening for events...")
        for message in self.consumer:
            event = message.value
            await self.process_event(event)
            self.consumer.commit()

    async def process_event(self, event):
        with self.tracer.start_as_current_span("process_financial_event") as span:
            header = event.get('header', {})
            payload = event.get('payload', {})
            tenant_id = header.get('tenant_id')
            trace_id = header.get('trace_id')

            logger.info(f"Processing real transaction for tenant: {tenant_id}")

            try:
                conn = psycopg2.connect(self.db_url)
                with conn.cursor() as cur:
                    # SECURE RLS Session Injection using set_config
                    cur.execute("SELECT set_config('app.current_tenant_id', %s, false)", (tenant_id,))

                    # Real persistence logic
                    cur.execute("""
                        INSERT INTO finance.sovereign_ledger_global
                        (tenant_id, trace_id, context_id, amount, entry_type, event_sourcing_id)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (tenant_id, trace_id, header.get('context_id'),
                          payload.get('amount'), 'CREDIT', str(header.get('trace_id'))))

                    conn.commit()
                conn.close()
            except Exception as e:
                logger.error(f"DB Error: {e}")

if __name__ == "__main__":
    worker = FinancialWorker()
    asyncio.run(worker.run())
