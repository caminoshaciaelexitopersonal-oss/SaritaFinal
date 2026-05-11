import json
from kafka import KafkaConsumer

class AIWorker:
    def __init__(self, topic="sarita.ai.decisions"):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=['localhost:9092'],
            group_id='ai-worker-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

    def execute_agent_task(self, event):
        trace_id = event['header']['trace_id']
        print(f"[{trace_id}] AI Agent Executing Task: {event['payload']}")
        # Lógica real: Llamada a LLM y ejecución de herramientas
        return True

    def run(self):
        print("AI Worker Started...")
        for message in self.consumer:
            self.execute_agent_task(message.value)
            self.consumer.commit()

if __name__ == "__main__":
    worker = AIWorker()
    worker.run()
