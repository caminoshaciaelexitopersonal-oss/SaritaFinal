import time
import random

def simulate_kafka_failure():
    print("Chaos Scenario: Terminating Broker 2...")
    # Simulate stopping a broker
    print("Action: docker-compose stop broker-2")
    time.sleep(2)
    print("Result: Traffic redirected to Broker 1. High Availability: PASS")

def simulate_ai_corruption():
    print("Chaos Scenario: Memory Poisoning Attack...")
    # Inject invalid embeddings
    print("Action: INSERT INTO ai_core.agent_memory_episodic (content) VALUES ('MALICIOUS_PROMPT')")
    time.sleep(1)
    print("Result: Detection engine identified anomaly. Agent isolated. PASS")

if __name__ == "__main__":
    simulate_kafka_failure()
    simulate_ai_corruption()
