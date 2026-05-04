-- Sistema de Reputación (Vía 3)
CREATE TABLE core.reputation_scores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    entity_type TEXT NOT NULL, -- 'tourist', 'artisan', 'provider'
    entity_id UUID NOT NULL,

    score DECIMAL(3,2) DEFAULT 5.00, -- 1.00 a 5.00
    total_reviews INT DEFAULT 0,

    updated_at TIMESTAMP DEFAULT now()
);

CREATE TABLE core.reputation_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,

    score_id UUID NOT NULL,
    impact_value DECIMAL(3,2), -- +0.1, -0.5
    reason TEXT,

    created_at TIMESTAMP DEFAULT now()
);
