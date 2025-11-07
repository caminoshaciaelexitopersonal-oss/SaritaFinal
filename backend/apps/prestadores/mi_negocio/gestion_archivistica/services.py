from .models import Document, DocumentVersion, Process, DocumentType, CustomUser, AuditLog, Company
from typing import Dict, Any, Optional, List
import uuid
from datetime import datetime

# ==========================================================
# Almacenamiento en Memoria (Simulación de Base de Datos)
# ==========================================================
# Usamos diccionarios para simular las tablas de la base de datos.
db = {
    "companies": {},
    "users": {},
    "process_types": {},
    "processes": {},
    "document_types": {},
    "documents": {},
    "document_versions": {},
    "audit_logs": [],
}

# Datos iniciales de ejemplo para permitir la funcionalidad sin una BD real
def init_mock_data():
    if not db["companies"]:
        company = Company(name="Empresa de Ejemplo", code="EJE")
        db["companies"][company.id] = company
        user = CustomUser(username="testuser", email="test@example.com", company=company, role="ADMIN")
        db["users"][user.id] = user
        pt = ProcessType(id=uuid.uuid4(), company=company, name="Procesos Generales", code="GEN")
        db["process_types"][pt.id] = pt
        p = Process(id=uuid.uuid4(), company=company, process_type=pt, name="Gestión de Calidad", code="CAL")
        db["processes"][p.id] = p
        dt = DocumentType(id=uuid.uuid4(), company=company, name="Manual", code="MAN")
        db["document_types"][dt.id] = dt
init_mock_data()


# ==========================================================
# Servicios de Lógica de Negocio
# ==========================================================

def get_ip_from_request(request) -> Optional[str]:
    # Implementación simulada para no depender de la request real de Django
    return "127.0.0.1"

class AuditLogger:
    @staticmethod
    def log(action: str, user: Optional[CustomUser] = None, request: Optional[Any] = None, details: Optional[Dict[str, Any]] = None):
        log_username = user.username if user else "System"
        log_company = user.company if user else None

        audit_entry = AuditLog(
            user=user, username=log_username, company=log_company,
            action=action, ip_address=get_ip_from_request(request), details=details or {}
        )
        db["audit_logs"].append(audit_entry)
        print(f"[AUDIT LOG] User: {log_username}, Action: {action}, Details: {details}")

class DocumentCoordinatorService:
    @staticmethod
    def _get_next_sequence(company_id: uuid.UUID, process_id: uuid.UUID, doc_type_id: uuid.UUID) -> int:
        sequences = [
            doc.sequence for doc in db["documents"].values()
            if doc.company.id == company_id and doc.process.id == process_id and doc.document_type.id == doc_type_id
        ]
        return max(sequences) + 1 if sequences else 1

    @staticmethod
    def _generate_code(process: Process, doc_type: DocumentType, sequence: int) -> str:
        return f"{process.process_type.code}-{process.code}-{doc_type.code}-{sequence:02d}"

    @classmethod
    def create_document_and_first_version(cls, *, data: Dict[str, Any], user: CustomUser, file_content: bytes, request: Any) -> DocumentVersion:
        process = db["processes"].get(uuid.UUID(data['process_id']))
        doc_type = db["document_types"].get(uuid.UUID(data['document_type_id']))
        if not process or not doc_type:
            raise ValueError("Proceso o Tipo de Documento no encontrado.")

        sequence = cls._get_next_sequence(user.company.id, process.id, doc_type.id)
        doc_code = cls._generate_code(process, doc_type, sequence)

        doc = Document(
            company=user.company, process=process, document_type=doc_type,
            sequence=sequence, document_code=doc_code, created_by=user
        )
        db["documents"][doc.id] = doc

        version_id = len(db["document_versions"]) + 1
        initial_version = DocumentVersion(
            id=version_id, document=doc, version_number=1, title=data['title'],
            validity_year=data['validity_year'], uploaded_by=user,
            original_filename=data['original_filename'], status='PENDING_UPLOAD'
        )
        db["document_versions"][initial_version.id] = initial_version

        # Simulación de procesamiento de archivo
        import hashlib
        file_hash = hashlib.sha256(file_content).hexdigest()
        initial_version.file_hash_sha256 = file_hash
        initial_version.external_file_id = f"simulated-path/{uuid.uuid4()}.enc"
        initial_version.status = "PENDING_CONFIRMATION"

        AuditLogger.log(
            user=user, action="DOCUMENT_CREATED", request=request,
            details={'document_id': str(doc.id), 'document_code': doc.document_code, 'version_id': initial_version.id}
        )
        return initial_version

    @classmethod
    def create_new_version_for_document(cls, *, document_id: str, data: Dict[str, Any], user: CustomUser, file_content: bytes, request: Any) -> DocumentVersion:
        document = db["documents"].get(uuid.UUID(document_id))
        if not document:
            raise ValueError("Documento no encontrado.")

        versions = [v.version_number for v in db["document_versions"].values() if v.document.id == document.id]
        new_version_number = max(versions) + 1 if versions else 1

        new_version_id = len(db["document_versions"]) + 1
        new_version = DocumentVersion(
            id=new_version_id, document=document, version_number=new_version_number,
            title=data['title'], validity_year=data['validity_year'], uploaded_by=user,
            original_filename=data['original_filename'], status='PENDING_UPLOAD'
        )
        db["document_versions"][new_version.id] = new_version

        # Simulación de procesamiento
        import hashlib
        file_hash = hashlib.sha256(file_content).hexdigest()
        new_version.file_hash_sha256 = file_hash
        new_version.external_file_id = f"simulated-path/{uuid.uuid4()}.enc"
        new_version.status = "PENDING_CONFIRMATION"

        AuditLogger.log(
            user=user, action="VERSION_UPLOADED", request=request,
            details={'document_id': str(document.id), 'new_version_id': new_version.id}
        )
        return new_version
