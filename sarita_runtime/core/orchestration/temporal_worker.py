import asyncio
from datetime import timedelta
from temporalio import workflow, activity
from temporalio.client import Client
from temporalio.worker import Worker

# 43.3 - Executable Activities
@activity.defn
async def reserve_inventory_activity(data: dict) -> str:
    # Real logic: DB Update in Tourism domain
    return f"Inventory reserved for {data.get('item_id')}"

@activity.defn
async def process_payment_activity(data: dict) -> str:
    # Real logic: Kafka Event emission to Finance
    return "Payment Processed"

@activity.defn
async def compensate_inventory_activity(data: dict) -> str:
    return "Inventory Released (Compensated)"

# 43.3 - Executable Workflow (Saga)
@workflow.defn
class BookingSagaWorkflow:
    @workflow.run
    async def run(self, data: dict) -> str:
        try:
            res1 = await workflow.execute_activity(
                reserve_inventory_activity, data, start_to_close_timeout=timedelta(seconds=10)
            )
            res2 = await workflow.execute_activity(
                process_payment_activity, data, start_to_close_timeout=timedelta(seconds=30)
            )
            return f"Saga Completed: {res1}, {res2}"
        except Exception:
            # Automatic Compensation
            await workflow.execute_activity(
                compensate_inventory_activity, data, start_to_close_timeout=timedelta(seconds=10)
            )
            raise

async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(client, task_queue="sarita-tasks", workflows=[BookingSagaWorkflow], activities=[reserve_inventory_activity, process_payment_activity, compensate_inventory_activity])
    print("Temporal Worker started. Waiting for workflows...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
