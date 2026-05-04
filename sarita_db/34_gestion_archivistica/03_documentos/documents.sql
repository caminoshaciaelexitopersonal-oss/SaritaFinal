-- Gestión de Documentos
CREATE TABLE archival.documents_main (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    file_id UUID NOT NULL, -- FK en 20_global
    type_id UUID NOT NULL, -- FK en 20_global

    current_version_id UUID, -- Ref circular manejada en 20_global
    title TEXT NOT NULL,

    status TEXT DEFAULT 'creado', -- creado, validado, firmado, archivado

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
