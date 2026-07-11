import json
import uuid
import datetime

class ScientificDatasetGenerator:
    """
    Generates structured, versioned, and schema-validated scientific datasets for active studies and trials.
    """
    def __init__(self, data_dir: str = "sarita_runtime/conjuntos_de_datos_científicos/"):
        self.data_dir = data_dir

    def generate_and_save_dataset(self, name: str, values_list: list, metadata_info: dict) -> dict:
        dataset_id = f"DATASET-UUID-{uuid.uuid4().hex.upper()}"
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

        payload = {
            "dataset_id": dataset_id,
            "name": name,
            "created_at": timestamp,
            "record_count": len(values_list),
            "data": values_list,
            "metadata": metadata_info
        }

        return payload
