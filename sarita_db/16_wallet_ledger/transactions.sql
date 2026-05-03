CREATE TABLE ledger.transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    description TEXT,
    reference VARCHAR(100), -- Idempotency / External Ref
    status VARCHAR(20) DEFAULT 'POSTED',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
