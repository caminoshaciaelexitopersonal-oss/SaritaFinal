import asyncio

class FinancialOperationFlow:
    async def process_transaction(self, tx_data):
        print(f"Processing real financial flow for: {tx_data}")
        await asyncio.sleep(0.1)
        return True
