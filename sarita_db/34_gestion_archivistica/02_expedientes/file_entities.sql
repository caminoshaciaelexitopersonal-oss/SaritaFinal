CREATE TABLE archival.file_entities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    file_id UUID NOT NULL,
    entity_type TEXT NOT NULL, -- usuario, empresa, proceso_legal
    entity_id UUID NOT NULL,   -- Ref genérica

    relation_type TEXT,

    created_at TIMESTAMP DEFAULT now()
);
