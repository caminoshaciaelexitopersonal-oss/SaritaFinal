import asyncio
import logging

class ChaosLabExt:
    async def run_regional_blackout(self, region_id):
        logging.critical(f"CHAOS: Blackout in region {region_id}")
        return "FAILOVER_SUCCESS"

    async def run_redis_failover(self):
        logging.warning("CHAOS: Redis Primary loss simulation")
        return "SENTINEL_OK"
