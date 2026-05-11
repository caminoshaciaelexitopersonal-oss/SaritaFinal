import asyncio
import logging

class EventFlowController:
    def adjust_flow(self, domain, rate):
        logging.info(f"Adjusting event flow for {domain} to {rate} msg/s")
        return True
