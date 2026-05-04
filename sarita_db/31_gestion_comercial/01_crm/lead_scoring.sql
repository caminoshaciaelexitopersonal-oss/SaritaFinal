CREATE TABLE core.lead_scoring (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    lead_id UUID NOT NULL, -- FK en 20_global
    score INT DEFAULT 0,
    criteria_met JSONB DEFAULT '[]',

    updated_at TIMESTAMP DEFAULT now()
);
