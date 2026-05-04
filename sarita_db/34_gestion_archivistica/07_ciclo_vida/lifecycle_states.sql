-- Ciclo de Vida Documental
CREATE TABLE archival.lifecycle_states (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    state_name TEXT UNIQUE NOT NULL, -- creado, validado, firmado, archivado, purgado
    description TEXT,

    created_at TIMESTAMP DEFAULT now()
);
