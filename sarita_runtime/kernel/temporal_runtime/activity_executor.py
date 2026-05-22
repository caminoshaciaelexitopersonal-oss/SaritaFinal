import logging

class ActivityExecutor:
    async def execute(self, activity_name, params):
        logging.info(f"Executing Temporal Activity: {activity_name}")
        return "DONE"
