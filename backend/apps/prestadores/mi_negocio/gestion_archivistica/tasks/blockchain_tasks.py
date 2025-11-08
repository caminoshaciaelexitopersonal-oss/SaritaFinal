# backend/apps/prestadores/mi_negocio/gestion_archivistica/tasks/blockchain_tasks.py
import json
import logging
from celery import shared_task
from web3 import Web3
from merkle_tree import MerkleTree

from django.conf import settings
from django.db import transaction
from django.utils import timezone

from apps.prestadores.mi_negocio.gestion_archivistica.models import DocumentVersion

logger = logging.getLogger(__name__)

@shared_task(name="notarize_pending_documents_batch")
def notarize_pending_documents_batch():
    """
    Tarea periódica que recolecta hashes, construye un Árbol de Merkle,
    y ancla la raíz en la blockchain de Polygon.
    """
    with transaction.atomic():
        versions_to_process_qs = DocumentVersion.objects.select_for_update().filter(
            status=DocumentVersion.ProcessingStatus.PENDING_CONFIRMATION
        )
        if not versions_to_process_qs.exists():
            return "No documents pending notarization."

        versions_to_process = list(versions_to_process_qs)
        version_ids = [v.id for v in versions_to_process]

        # Marcar como 'IN_BATCH' para evitar que la próxima ejecución las tome.
        versions_to_process_qs.update(status=DocumentVersion.ProcessingStatus.IN_BATCH)

        hashes = [bytes.fromhex(v.file_hash_sha256) for v in versions_to_process]

    try:
        # 2. Construir el Árbol de Merkle
        tree = MerkleTree(hashes)
        merkle_root = tree.root.digest()
        merkle_root_hex = f"0x{merkle_root.hex()}"

        # 3. Interactuar con el Smart Contract (simulado por ahora)
        logger.info(f"Connecting to Polygon RPC at {settings.POLYGON_RPC_URL}")
        web3 = Web3(Web3.HTTPProvider(settings.POLYGON_RPC_URL))
        account = web3.eth.account.from_key(settings.SIGNER_PRIVATE_KEY)

        # Simulación de la transacción
        tx_hash_hex = f"0x{hashlib.sha256(merkle_root).hexdigest()}"
        timestamp = timezone.now()
        logger.info(f"Simulated blockchain transaction. Root: {merkle_root_hex}, TxHash: {tx_hash_hex}")

        # 6. Actualizar todos los registros en la BD con la prueba
        with transaction.atomic():
            for version, v_hash in zip(versions_to_process, hashes):
                proof = tree.get_proof(v_hash)

                version.status = DocumentVersion.ProcessingStatus.VERIFIED
                version.merkle_root = merkle_root_hex
                version.merkle_proof = [f"0x{p.hex()}" for p in proof]
                version.blockchain_transaction = tx_hash_hex
                version.blockchain_timestamp = timestamp
                version.save(update_fields=[
                    'status', 'merkle_root', 'merkle_proof',
                    'blockchain_transaction', 'blockchain_timestamp'
                ])

        logger.info(f"Successfully notarized batch of {len(hashes)} documents in simulated tx {tx_hash_hex}")
        return f"Notarized {len(hashes)} documents in tx {tx_hash_hex}"

    except Exception as e:
        logger.exception(f"Failed to notarize batch of {len(version_ids)} documents. Reverting status.")
        # Revertir el estado si algo falla.
        DocumentVersion.objects.filter(id__in=version_ids).update(
            status=DocumentVersion.ProcessingStatus.PENDING_CONFIRMATION
        )
        raise e
