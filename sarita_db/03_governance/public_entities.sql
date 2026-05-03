CREATE TABLE governance.public_entities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    name TEXT NOT NULL,
    entity_type TEXT NOT NULL, -- alcaldia, gobernacion, ministerio
    territorial_id UUID NOT NULL, -- FK en 20_global
    parent_entity_id UUID, -- FK en 20_global
    created_at TIMESTAMP DEFAULT now(),
    hash_integridad TEXT,
    trace_id UUID
);
