CREATE TABLE core.financial_snapshots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    snapshot_date DATE DEFAULT CURRENT_DATE,
    financial_data JSONB NOT NULL, -- {assets: X, liabilities: Y, equity: Z}

    created_at TIMESTAMP DEFAULT now()
);
