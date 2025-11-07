import logging
# from celery import shared_task - Simulado
# from web3 import Web3 - Simulado
# from merkle_tree import MerkleTree - Simulado
from datetime import datetime, timezone

from ..services import db
from ..models import DocumentVersion

logger = logging.getLogger(__name__)

# Simulación del decorador de Celery
def shared_task(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Ejecutando tarea periódica simulada '{func.__name__}'")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error en tarea periódica simulada '{func.__name__}': {e}")
    return wrapper

@shared_task
def notarize_pending_documents_batch():
    """
    Tarea periódica (simulada) que recolecta hashes, construye un Árbol de Merkle
    y ancla la raíz en la blockchain.
    """

    # 1. Recolectar documentos listos para notarizar
    versions_to_process = [
        v for v in db["document_versions"].values()
        if v.status == 'PENDING_CONFIRMATION'
    ]

    if not versions_to_process:
        return "No hay documentos pendientes de notarización."

    logger.info(f"Iniciando lote de notarización con {len(versions_to_process)} documento(s).")

    # Marcar las versiones como 'en proceso' para evitar que se tomen en la siguiente ejecución
    for v in versions_to_process:
        v.status = 'IN_BATCH'

    hashes = [bytes.fromhex(v.file_hash_sha256) for v in versions_to_process]

    try:
        # 2. Construir el Árbol de Merkle (simulado)
        # En un entorno real: `tree = MerkleTree(hashes)`
        import hashlib
        merkle_root = hashlib.sha256(b"".join(hashes)).hexdigest()
        merkle_root_hex = f"0x{merkle_root}"

        # 3. Interactuar con el Smart Contract (simulado)
        # Aquí iría la lógica de Web3 para enviar la transacción
        import uuid
        tx_hash_hex = f"0x{uuid.uuid4().hex}"

        # 4. Simular espera de confirmación y obtener timestamp
        timestamp = datetime.now(timezone.utc)

        # 5. Actualizar todos los registros en la "BD" con la prueba
        for version, v_hash in zip(versions_to_process, hashes):
            # Simular la obtención de la prueba del árbol
            proof = [f"0x{hashlib.sha256(v_hash).hexdigest()}"]

            version.status = 'VERIFIED'
            version.merkle_root = merkle_root_hex
            version.merkle_proof = proof
            version.blockchain_transaction = tx_hash_hex
            version.blockchain_timestamp = timestamp

        logger.info(f"Lote de {len(hashes)} documentos notarizado con éxito en tx simulada: {tx_hash_hex}")
        return f"Notarizados {len(hashes)} documentos."

    except Exception as e:
        logger.exception("Fallo al notarizar el lote. Revirtiendo estados.")
        # Revertir el estado para que se reintenten en la próxima ejecución.
        for v in versions_to_process:
            v.status = 'PENDING_CONFIRMATION'
        raise e
