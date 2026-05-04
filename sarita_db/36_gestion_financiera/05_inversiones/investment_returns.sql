CREATE TABLE core.investment_returns (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    investment_id UUID NOT NULL,
    amount_received DECIMAL(18,2) NOT NULL,
    period_label TEXT, -- Q1, Marzo, etc.

    received_at TIMESTAMP DEFAULT now()
);
