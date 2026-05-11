import asyncio
from sarita_runtime.runtime_integration.integration_bus import IntegrationBus
from sarita_runtime.distributed_transactions.real_saga_executor import RealSagaExecutor

async def run_full_runtime_validation():
    print("--- INITIATING REAL RUNTIME VALIDATION ---")

    # 1. Test Integration Bus
    bus = IntegrationBus()
    await bus.route_cross_domain("FINANCE", {"event": "test"})

    # 2. Test Saga Execution
    saga = RealSagaExecutor()
    await saga.run_saga(["StepA", "StepB"], "VAL-001")

    print("--- VALIDATION SUCCESSFUL ---")

if __name__ == "__main__":
    asyncio.run(run_full_runtime_validation())
