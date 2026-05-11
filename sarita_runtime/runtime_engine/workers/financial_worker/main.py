import json
import time
from kafka import KafkaConsumer

class FinancialWorker:
    def __init__(self, topic="sarita.finance.events"):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=['localhost:9092'],
            group_id='financial-worker-group',
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

    def process_ledger(self, event):
        trace_id = event['header']['trace_id']
        print(f"[{trace_id}] Processing Ledger Entry: {event['payload']}")
        # Lógica real: Llamada a SQL para insertar en finance.ledger_entries
        # Simulación de éxito
        return True

    def run(self):
        print("Financial Worker Started...")
        for message in self.consumer:
            event = message.value
            try:
                success = self.process_ledger(event)
                if success:
                    self.consumer.commit()
            except Exception as e:
                print(f"Error processing event: {e}")
                # Retry logic or DLQ
                time.sleep(1)

if __name__ == "__main__":
    worker = FinancialWorker()
    worker.run()
