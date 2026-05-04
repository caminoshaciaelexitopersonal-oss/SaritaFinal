-- Consolidación Multi-empresa (Holding)
CREATE TABLE core.financial_groups (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL, -- El tenant que actúa como Holding
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    group_name TEXT NOT NULL,
    description TEXT,

    created_at TIMESTAMP DEFAULT now()
);
