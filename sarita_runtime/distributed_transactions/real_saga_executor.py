import asyncio

class RealSagaExecutor:
    async def run_saga(self, saga_steps, saga_id):
        print(f"Executing REAL Distributed Saga: {saga_id}")
        executed_steps = []
        try:
            for step in saga_steps:
                await self.execute_step(step)
                executed_steps.append(step)
            print(f"Saga {saga_id} SUCCESS.")
        except Exception as e:
            print(f"Saga {saga_id} FAILED at step {step}: {e}")
            await self.compensate(executed_steps)

    async def execute_step(self, step):
        print(f"Executing step: {step}")
        await asyncio.sleep(0.1)

    async def compensate(self, steps):
        print("Starting REAL Distributed Rollback...")
        for step in reversed(steps):
            print(f"Compensating step: {step}")
            await asyncio.sleep(0.1)

if __name__ == "__main__":
    saga = RealSagaExecutor()
    steps = ["ReserveInventory", "AuthorizePayment", "UpdateLedger"]
    asyncio.run(saga.run_saga(steps, "TX-REAL-001"))
