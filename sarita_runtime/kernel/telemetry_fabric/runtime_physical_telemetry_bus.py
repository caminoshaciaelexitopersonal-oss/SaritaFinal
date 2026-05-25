import logging

class RuntimePhysicalTelemetryBus:
    """
    Materializes physical telemetry.
    Toda métrica física pertenece a un execution graph.
    """
    def __init__(self):
        self.active_metrics = {}

    def push_metric(self, task_id: str, metric_type: str, value: float):
        logging.debug(f"Telemetry Bus: {task_id} -> {metric_type}: {value}")
        if task_id not in self.active_metrics:
            self.active_metrics[task_id] = []
        self.active_metrics[task_id].append({
            "type": metric_type,
            "value": value,
            "ts_ns": 0 # Should use RuntimeClockAuthority
        })

    def get_task_telemetry(self, task_id: str):
        return self.active_metrics.get(task_id, [])
