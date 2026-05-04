-- Accesos y Seguridad
CREATE TABLE archival.document_permissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_id UUID, -- NULL si es permiso por carpeta/tipo
    file_id UUID,

    subject_type TEXT NOT NULL, -- user, role
    subject_id UUID NOT NULL,

    permission_level TEXT NOT NULL, -- view, download, sign, delete

    created_at TIMESTAMP DEFAULT now()
);
