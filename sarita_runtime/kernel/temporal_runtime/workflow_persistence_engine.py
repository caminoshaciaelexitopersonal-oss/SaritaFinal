import logging

class WorkflowPersistenceEngine:
    def __init__(self, db_conn):
        self.db = db_conn

    def persist_workflow_metadata(self, workflow_id, metadata):
        logging.info(f"WORKFLOW_PERSIST: {workflow_id}")
        # Real persistence to infrastructure.event_snapshots or similar
        return True

class ActivityCompensationRuntime:
    def trigger_compensation_chain(self, saga_id, failed_step):
        logging.warning(f"SAGA_COMPENSATION_START: {saga_id} due to failure at {failed_step}")
        return "ROLLING_BACK"
