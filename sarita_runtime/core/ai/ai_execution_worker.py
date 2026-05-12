import asyncio
import json
import os
import psycopg2
from kafka import KafkaConsumer

class AIExecutionWorker:
    def __init__(self):
        self.db_url = os.getenv("DATABASE_URL")
        self.consumer = KafkaConsumer(
            'sarita.ai.decisions',
            bootstrap_servers=os.getenv("KAFKA_BROKERS", "localhost:9092"),
            group_id='ai-execution-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

    async def run(self):
        for message in self.consumer:
            event = message.value
            await self.execute_ai_action(event)

    async def execute_ai_action(self, event):
        header = event.get('header', {})
        tenant_id = header.get('tenant_id')
        trace_id = header.get('trace_id')

        conn = psycopg2.connect(self.db_url)
        with conn.cursor() as cur:
            # SECURE RLS Session Injection using set_config
            cur.execute("SELECT set_config('app.current_tenant_id', %s, false)", (tenant_id,))

            # Real AI Action persistence
            cur.execute("""
                INSERT INTO ai_core.autonomous_decisions_log
                (tenant_id, trace_id, context_id, dynamic_priority, decision_risk_score)
                VALUES (%s, %s, %s, %s, %s)
            """, (tenant_id, trace_id, header.get('context_id'), 1, 0.05))

            conn.commit()
        conn.close()
        print(f"AI Action Persisted for trace: {trace_id}")

if __name__ == "__main__":
    worker = AIExecutionWorker()
    asyncio.run(worker.run())
