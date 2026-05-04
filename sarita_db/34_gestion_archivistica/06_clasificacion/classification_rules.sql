-- Clasificación Inteligente
CREATE TABLE archival.classification_rules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL,
    patterns_json JSONB NOT NULL, -- Regex or keywords
    target_type_id UUID NOT NULL,

    is_ai_powered BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);
