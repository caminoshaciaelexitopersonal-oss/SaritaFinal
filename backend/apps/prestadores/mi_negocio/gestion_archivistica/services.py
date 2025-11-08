from django.db import transaction
from .models import Document, DocumentVersion, Process, DocumentType
from api.models import CustomUser
from typing import Dict, Any, Optional
from apps.audit.services import AuditLogger

def get_ip_from_request(request) -> Optional[str]:
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class DocumentCoordinatorService:
    @staticmethod
    @transaction.atomic
    def _get_next_sequence(company, process, doc_type) -> int:
        last_doc = Document.objects.filter(
            company=company, process=process, document_type=doc_type
        ).order_by('-sequence').first()
        return (last_doc.sequence + 1) if last_doc else 1

    @staticmethod
    def _generate_code(process: Process, doc_type: DocumentType, sequence: int) -> str:
        # Assuming process_type is accessible from process
        return f"{process.process_type.code}-{process.code}-{doc_type.code}-{sequence:02d}"

    @classmethod
    def create_document_and_first_version(cls, *, data: Dict[str, Any], user: CustomUser, file_content: bytes, request: Any) -> DocumentVersion:
        process = Process.objects.get(id=data['process'].id)
        doc_type = DocumentType.objects.get(id=data['document_type'].id)
        company = user.perfil_prestador.company

        sequence = cls._get_next_sequence(company, process, doc_type)
        doc_code = cls._generate_code(process, doc_type, sequence)

        doc = Document.objects.create(
            company=company,
            process=process,
            document_type=doc_type,
            sequence=sequence,
            document_code=doc_code,
            created_by=user
        )

        initial_version = DocumentVersion.objects.create(
            document=doc,
            version_number=1,
            title=data['title'],
            validity_year=data['validity_year'],
            uploaded_by=user,
            original_filename=data['original_filename'],
            status=DocumentVersion.ProcessingStatus.PENDING_UPLOAD
        )

        import hashlib
        initial_version.file_hash_sha256 = hashlib.sha256(file_content).hexdigest()
        initial_version.external_file_id = f"uploads/{doc.id}/{initial_version.id}.enc"
        initial_version.status = DocumentVersion.ProcessingStatus.PENDING_CONFIRMATION
        initial_version.save()

        AuditLogger.log(
            user=user, action="DOCUMENT_CREATED", request=request,
            details={'document_id': str(doc.id), 'document_code': doc.document_code, 'version_id': initial_version.id}
        )
        return initial_version

    @classmethod
    def create_new_version_for_document(cls, *, document: Document, data: Dict[str, Any], user: CustomUser, file_content: bytes, request: Any) -> DocumentVersion:
        with transaction.atomic():
            latest_version = document.versions.order_by('-version_number').first()
            new_version_number = (latest_version.version_number + 1) if latest_version else 1

            new_version = DocumentVersion.objects.create(
                document=document,
                version_number=new_version_number,
                title=data['title'],
                validity_year=data['validity_year'],
                uploaded_by=user,
                original_filename=data['original_filename'],
                status=DocumentVersion.ProcessingStatus.PENDING_UPLOAD
            )

            import hashlib
            new_version.file_hash_sha256 = hashlib.sha256(file_content).hexdigest()
            new_version.external_file_id = f"uploads/{document.id}/{new_version.id}.enc"
            new_version.status = DocumentVersion.ProcessingStatus.PENDING_CONFIRMATION
            new_version.save()

            AuditLogger.log(
                user=user, action="VERSION_UPLOADED", request=request,
                details={'document_id': str(document.id), 'new_version_id': new_version.id}
            )
            return new_version
