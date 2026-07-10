class RuntimeExecutor:
    """
    Safely executes arbitrary engine and service tasks within the master runtime.
    """
    def __init__(self):
        pass

    def execute_task(self, task_callable, *args, **kwargs):
        try:
            res = task_callable(*args, **kwargs)
            return {"status": "SUCCESS", "result": res}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}
