import psycopg2
import logging

class ReplayCheckpointEngine:
    def __init__(self, db_url):
        self.db_url = db_url

    def save_checkpoint(self, consumer_id, topic, partition, offset, tenant_id):
        logging.info(f"Saving checkpoint: {topic}:{partition} -> {offset}")
        try:
            conn = psycopg2.connect(self.db_url)
            with conn.cursor() as cur:
                cur.execute("SELECT set_config('app.current_tenant_id', %s, false)", (tenant_id,))
                cur.execute("""
                    INSERT INTO infrastructure.event_replay_checkpoints (consumer_id, topic_partition, last_offset, tenant_id, trace_id, context_id)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET last_offset = EXCLUDED.last_offset
                """, (consumer_id, f"{topic}-{partition}", offset, tenant_id, 'trace-50', 'context-50'))
                conn.commit()
            conn.close()
            return True
        except Exception as e:
            logging.error(f"Checkpoint Error: {e}")
            return False
