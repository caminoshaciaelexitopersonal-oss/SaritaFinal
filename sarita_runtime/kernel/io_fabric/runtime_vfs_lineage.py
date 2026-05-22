import logging

class RuntimeVFSLineage:
    """
    Tracks execution-backed file lineage and VFS operations.
    """
    def __init__(self):
        self.operation_history = []

    async def record_operation(self, pid: int, path: str, op_type: str, success: bool):
        logging.info(f"VFS Lineage: PID {pid} performed {op_type} on {path} (Success: {success})")
        self.operation_history.append({
            "pid": pid,
            "path": path,
            "op": op_type,
            "success": success
        })

    async def get_path_lineage(self, path: str):
        return [op for op in self.operation_history if op["path"] == path]
