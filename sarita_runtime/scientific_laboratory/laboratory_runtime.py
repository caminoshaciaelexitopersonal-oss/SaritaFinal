class LaboratoryRuntime:
    """
    Physical master runner for executing scientific trials in isolated sandbox contexts.
    """
    def __init__(self):
        self.active_processes = 0

    def launch_trial(self, trial_callable, *args, **kwargs) -> dict:
        self.active_processes += 1
        try:
            res = trial_callable(*args, **kwargs)
            status = "COMPLETED"
            err = None
        except Exception as e:
            res = None
            status = "CRASHED"
            err = str(e)
        finally:
            self.active_processes -= 1

        return {
            "status": status,
            "result": res,
            "error": err
        }
