import asyncio
import logging
from temporalio.client import Client

class TemporalClusterConnector:
    def __init__(self, namespace="sarita-production"):
        self.namespace = namespace
        self.client = None

    async def connect_with_retry(self, host):
        for i in range(5):
            try:
                self.client = await Client.connect(host, namespace=self.namespace)
                logging.info(f"Successfully connected to Temporal on attempt {i+1}")
                return self.client
            except Exception:
                await asyncio.sleep(1)
        raise Exception("Temporal Cluster Connection Failed after 5 retries.")
