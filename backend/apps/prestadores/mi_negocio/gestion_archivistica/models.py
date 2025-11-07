from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime
import uuid

# Se utilizan dataclasses para representar la estructura de los datos en memoria,
# sin depender de la base de datos, como se solicitó.

@dataclass
class Company:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    name: str = ""
    code: str = ""
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class CustomUser:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    username: str = ""
    email: str = ""
    company: Optional[Company] = None
    role: str = "VIEWER"  # ADMIN, EDITOR, VIEWER

@dataclass
class ProcessType:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    company: Company
    name: str
    code: str

@dataclass
class Process:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    company: Company
    process_type: ProcessType
    name: str
    code: str

@dataclass
class DocumentType:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    company: Company
    name: str
    code: str

@dataclass
class Document:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    company: Company
    process: Process
    document_type: DocumentType
    sequence: int
    document_code: str
    created_by: CustomUser
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class DocumentVersion:
    id: int
    document: Document
    version_number: int
    title: str
    validity_year: int
    uploaded_by: CustomUser
    original_filename: str
    status: str  # PENDING_UPLOAD, PENDING_CONFIRMATION, VERIFIED, COMPROMISED
    uploaded_at: datetime = field(default_factory=datetime.utcnow)
    file_hash_sha256: Optional[str] = None
    external_file_id: Optional[str] = None
    merkle_root: Optional[str] = None
    merkle_proof: Optional[List[str]] = None
    blockchain_transaction: Optional[str] = None
    blockchain_timestamp: Optional[datetime] = None

@dataclass
class AuditLog:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    user: Optional[CustomUser]
    username: str
    company: Optional[Company]
    action: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    ip_address: Optional[str] = None
    details: Dict[str, Any] = field(default_factory=dict)
