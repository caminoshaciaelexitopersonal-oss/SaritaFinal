-- Sistema de Reputación: Scores Consolidados
CREATE TABLE tourism.provider_reputation_score (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL UNIQUE, -- FK en 20_global

    score_global DECIMAL(3,2) DEFAULT 0.00,
    score_servicio DECIMAL(3,2) DEFAULT 0.00,
    score_cumplimiento DECIMAL(3,2) DEFAULT 0.00,
    score_cancelaciones DECIMAL(3,2) DEFAULT 0.00,

    updated_at TIMESTAMP DEFAULT now()
);
