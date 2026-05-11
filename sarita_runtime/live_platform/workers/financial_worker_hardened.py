import asyncio
import logging
from sarita_runtime.live_platform.workers.base_hardened_worker import BaseWorker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("HardenedFinancialWorker")

class HardenedFinancialWorker(BaseWorker):
    def __init__(self):
        super().__init__(topic='sarita.finance.events', group_id='sarita-finance-hardened-group')

    async def handle_event(self, event):
        # Implementation of real financial logic: ledger entry, tax calculation, etc.
        # This now benefits from tracing, error handling and manual commits from BaseWorker
        event_type = event.get('header', {}).get('event_type')
        logger.info(f"Hardened processing of: {event_type}")

        # Real logic would happen here (SQL execution within the trace span)
        await asyncio.sleep(0.1)
        return True

if __name__ == "__main__":
    worker = HardenedFinancialWorker()
    asyncio.run(worker.run())
