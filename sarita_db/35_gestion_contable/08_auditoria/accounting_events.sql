CREATE TABLE accounting.accounting_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    event_type TEXT NOT NULL, -- MANUAL, AUTOMATIC_FROM_SALES, AUTOMATIC_FROM_PAYMENTS
    payload JSONB,

    created_at TIMESTAMP DEFAULT now()
);
