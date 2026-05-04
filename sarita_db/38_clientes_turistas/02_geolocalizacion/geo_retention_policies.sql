-- Políticas de Retención Geográfica
CREATE TABLE tourism.geo_retention_policies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    retention_days INT DEFAULT 30,
    anonymize_after_days INT DEFAULT 7,

    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);
