-- Notarización
CREATE TABLE archival.notarization_providers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL, -- Blockchain, Notaría X, Servicio Digital Y
    config_json JSONB,

    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);
