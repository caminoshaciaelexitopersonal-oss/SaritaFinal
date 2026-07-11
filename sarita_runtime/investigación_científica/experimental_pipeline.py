class ExperimentalPipeline:
    """
    Builds and manages sequential experimental pipeline stages (Preprocessing, Run, Analysis, Postprocessing).
    """
    def __init__(self, name: str):
        self.name = name
        self.stages = []

    def add_stage(self, stage_name: str, stage_func):
        self.stages.append((stage_name, stage_func))

    def execute_pipeline(self, initial_context: dict) -> dict:
        context = initial_context.copy()
        execution_trace = []
        for name, func in self.stages:
            try:
                context = func(context)
                execution_trace.append({"stage": name, "status": "SUCCESS"})
            except Exception as e:
                execution_trace.append({"stage": name, "status": "FAILED", "error": str(e)})
                context["pipeline_error"] = str(e)
                break
        return {
            "pipeline": self.name,
            "trace": execution_trace,
            "final_context": context
        }
