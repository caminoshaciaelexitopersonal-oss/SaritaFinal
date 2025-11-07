import logging
# from celery import shared_task, chain - Simulado
from ..services import db # Usamos nuestra BD en memoria
from ..models import DocumentVersion

logger = logging.getLogger(__name__)

# ==============================================================================
# Simulación del decorador de Celery para mantener el código sin dependencias
# ==============================================================================
def shared_task(func):
    """
    Decorador simulado que permite que el código sea estructuralmente idéntico
    al de Celery sin requerir la librería.
    """
    def wrapper(*args, **kwargs):
        logger.info(f"Ejecutando tarea simulada '{func.__name__}' con args: {args}")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error en tarea simulada '{func.__name__}': {e}")
            # En Celery real, aquí se manejarían los reintentos.
    return wrapper

# ==============================================================================
# Tareas Individuales del Pipeline (Simuladas)
# ==============================================================================

@shared_task
def hash_and_upload_task(version_id: int, file_content_b64: str) -> int:
    """
    Tarea #1 (Simulada): Calcula hash, cifra y "sube" el archivo.
    """
    import base64
    import hashlib

    version = db["document_versions"].get(version_id)
    if not version or version.status != 'PENDING_UPLOAD':
        logger.warning(f"Omitiendo hash_and_upload para Version {version_id}, estado: '{version.status if version else 'N/A'}'.")
        return version_id

    file_content = base64.b64decode(file_content_b64)

    # 1. Calcular hash
    file_hash = hashlib.sha256(file_content).hexdigest()

    # 2. Cifrar (simulado)
    # En la implementación real, aquí se llamaría al CryptoService
    encrypted_content = file_content # En esta simulación no ciframos

    # 3. Subir (simulado)
    # En la implementación real, se llamaría al StorageCoordinator
    import uuid
    external_id = f"s3-simulated/{uuid.uuid4()}.enc"

    # 4. Actualizar el registro en la "BD"
    version.external_file_id = external_id
    version.file_hash_sha256 = file_hash
    # El estado se actualiza en la siguiente tarea del pipeline.

    logger.info(f"Tarea 'hash_and_upload' completada para Version ID: {version_id}.")
    return version_id


@shared_task
def prepare_for_notarization_task(version_id: int) -> str:
    """
    Tarea final (Simulada): Marca la versión como lista para notarización.
    """
    version = db["document_versions"].get(version_id)
    if not version:
        logger.error(f"Version ID {version_id} no encontrada en 'prepare_for_notarization_task'.")
        return f"Fallo: Versión {version_id} no encontrada."

    if version.file_hash_sha256 and version.external_file_id:
        version.status = 'PENDING_CONFIRMATION'
        logger.info(f"Version {version_id} está ahora lista para notarización.")
        return f"Éxito: Versión {version_id} en cola para notarización."
    else:
        logger.error(f"No se puede poner en cola la Versión {version_id}, falta hash o id externo.")
        version.status = 'FAILED' # Marcar como fallida
        return f"Fallo: Versión {version_id} no pudo ser procesada."

# ==============================================================================
# Orquestador del Flujo (Simulado)
# ==============================================================================
def file_processing_chain(version_id: int, file_content_b64: str):
    """
    Función que simula la cadena de Celery (`chain`).
    En una implementación real, esto se definiría en el `DocumentCoordinatorService`
    y se llamaría con `.delay()`.
    """
    logger.info(f"Iniciando pipeline de procesamiento para DocumentVersion ID: {version_id}")

    # Ejecución secuencial para simular la cadena
    result_step1 = hash_and_upload_task(version_id, file_content_b64)
    if result_step1:
        prepare_for_notarization_task(result_step1)
