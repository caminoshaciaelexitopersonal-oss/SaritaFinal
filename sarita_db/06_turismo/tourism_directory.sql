CREATE TABLE tourism.tourism_directory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    attraction_id UUID, -- FK en 20_global
    event_id UUID, -- FK en 20_global
    category TEXT,
    searchable_vector tsvector,
    created_at TIMESTAMP DEFAULT now(),
    hash_integridad TEXT,
    trace_id UUID
);
