# backend/apps/prestadores/mi_negocio/gestion_archivistica/tasks/processing_tasks.py
import base64
import logging
from celery import shared_task, chain
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from ..models import DocumentVersion
# Importación movida a local para evitar ciclo

logger = logging.getLogger(__name__)

@shared_task(name="start_file_processing_flow")
def start_file_processing_flow(version_id: int, file_content_b64: str):
    logger.info(f"Initiating file processing pipeline for DocumentVersion ID: {version_id}")
    processing_pipeline = chain(
        hash_and_upload_task.s(version_id, file_content_b64),
        prepare_for_notarization_task.s()
    )
    processing_pipeline.apply_async()

@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3, 'countdown': 60})
def hash_and_upload_task(self, version_id: int, file_content_b64: str) -> int:
    try:
        with transaction.atomic():
            version = DocumentVersion.objects.select_for_update().get(id=version_id)
            if version.status != DocumentVersion.ProcessingStatus.PENDING_UPLOAD:
                logger.warning(f"Skipping hash_and_upload for Version {version_id}, status is already '{version.status}'.")
                return version_id

        from ..services import FileCoordinator
        file_content = base64.b64decode(file_content_b64)
        file_coordinator = FileCoordinator()
        file_hash, external_id = file_coordinator.upload_and_process(file_content, version)
        version.external_file_id = external_id
        version.file_hash_sha256 = file_hash
        version.save(update_fields=['external_file_id', 'file_hash_sha256'])
        logger.info(f"Successfully uploaded and hashed Version ID: {version_id}. External ID: {external_id}")
        return version_id
    except ObjectDoesNotExist:
        logger.error(f"Version ID {version_id} not found in hash_and_upload_task. Aborting pipeline.")
    except Exception as exc:
        logger.exception(f"Error in hash_and_upload_task for Version {version_id}. Attempt {self.request.retries + 1}.")
        raise exc

@shared_task(bind=True)
def prepare_for_notarization_task(self, version_id: int) -> str:
    try:
        version = DocumentVersion.objects.get(id=version_id)
        if version.file_hash_sha256 and version.external_file_id:
            version.status = DocumentVersion.ProcessingStatus.PENDING_CONFIRMATION
            version.save(update_fields=['status'])
            logger.info(f"Version {version_id} is now ready for notarization.")
            return f"Success: Version {version_id} queued for notarization."
        else:
            logger.error(f"Cannot queue Version {version_id} for notarization, previous step failed.")
            return f"Failed: Version {version_id} could not be queued."
    except ObjectDoesNotExist:
        logger.error(f"Version ID {version_id} not found in prepare_for_notarization_task.")
        return f"Failed: Version {version_id} not found."
