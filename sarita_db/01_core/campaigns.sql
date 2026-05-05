CREATE TABLE core.marketing_campaigns (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL,
    objective TEXT,
    budget DECIMAL(18,2) DEFAULT 0.00,

    start_date DATE,
    end_date DATE,
    status TEXT DEFAULT 'planificada',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
