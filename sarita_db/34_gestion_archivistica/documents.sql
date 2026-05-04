-- Gestión Archivística: Documentos
CREATE TABLE core.documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL, -- FK en 20_global

    tipo_documento TEXT NOT NULL,
    version INT DEFAULT 1,
    url TEXT NOT NULL,

    estado TEXT DEFAULT 'borrador',
    hash_documento TEXT NOT NULL, -- SHA256 del binario

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
