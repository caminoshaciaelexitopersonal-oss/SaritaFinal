import logging

class IoUringCompletionRouter:
    """
    Routes harvested completions from CQ to the appropriate causal vertices.
    """
    def __init__(self, nervous_system):
        self.nervous_system = nervous_system

    def route_completion(self, completion_event: dict):
        task_id = completion_event.get("user_data")
        logging.info(f"Completion Router: Routing CQE to vertex {task_id}")
        # Mark vertex as COMPLETED in nervous system
        vertex = self.nervous_system.get_vertex(task_id)
        if vertex:
            vertex.mark_completed(0) # Timestamp should come from clock
        return True
