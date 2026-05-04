-- Búsquedas Realizadas por el Turista
CREATE TABLE core.tourist_searches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    search_text TEXT NOT NULL,
    filters_applied JSONB DEFAULT '{}',
    results_count INT,

    created_at TIMESTAMP DEFAULT now()
);
