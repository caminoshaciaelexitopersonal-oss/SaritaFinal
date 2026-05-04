-- Expedientes (Núcleo Archivístico)
CREATE TABLE archival.files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    file_number TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    description TEXT,

    status TEXT DEFAULT 'abierto', -- abierto, cerrado, transferido

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
