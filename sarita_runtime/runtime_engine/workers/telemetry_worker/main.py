import json
from kafka import KafkaConsumer

class TelemetryWorker:
    def __init__(self, topic="sarita.telemetry.metrics"):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=['localhost:9092'],
            group_id='telemetry-worker-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

    def process_metrics(self, event):
        print(f"Aggregating Metrics: {event['payload']}")
        # Lógica real: Enviar a Prometheus Pushgateway o VictoriaMetrics
        return True

    def run(self):
        print("Telemetry Worker Started...")
        for message in self.consumer:
            self.process_metrics(message.value)
            self.consumer.commit()

if __name__ == "__main__":
    worker = TelemetryWorker()
    worker.run()
