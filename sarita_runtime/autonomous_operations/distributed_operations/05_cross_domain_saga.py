import asyncio

class CrossDomainSaga:
    async def execute_saga(self, saga_id):
        print(f"STARTING SAGA: {saga_id}")
        try:
            # Step 1: Finance
            await self.step_finance()
            # Step 2: Tourism
            await self.step_tourism()
            # Step 3: AI Audit
            await self.step_ai_audit()

            print(f"SAGA {saga_id} COMPLETED SUCCESSFULLY.")
        except Exception as e:
            print(f"SAGA {saga_id} FAILED: {e}. Starting Compensation...")
            await self.compensate()

    async def step_finance(self):
        print("Saga Step: Authorizing Payment...")
        await asyncio.sleep(0.1)

    async def step_tourism(self):
        print("Saga Step: Confirming Booking...")
        # Simulate failure
        # raise Exception("Inventory Lock Failed")
        await asyncio.sleep(0.1)

    async def step_ai_audit(self):
        print("Saga Step: AI Fraud Validation...")
        await asyncio.sleep(0.1)

    async def compensate(self):
        print("Compensation Logic: Reversing Ledger entries...")
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    saga = CrossDomainSaga()
    asyncio.run(saga.execute_saga("TX-999"))
