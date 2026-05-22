import json
import logging
from kafka import KafkaConsumer, TopicPartition

class EventReplayEngine:
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.servers = bootstrap_servers

    def replay_from_offset(self, topic, partition, offset, handler):
        logger = logging.getLogger("ReplayEngine")
        logger.info(f"Initiating Replay for {topic} partition {partition} from offset {offset}")

        consumer = KafkaConsumer(bootstrap_servers=self.servers)
        tp = TopicPartition(topic, partition)
        consumer.assign([tp])
        consumer.seek(tp, offset)

        for message in consumer:
            logger.info(f"Replaying message: {message.offset}")
            handler(message.value)
            # Break condition for replay end
            break
        consumer.close()

if __name__ == "__main__":
    replay = EventReplayEngine()
    # replay.replay_from_offset("sarita.finance.events", 0, 100, print)
