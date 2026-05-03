CREATE TABLE ledger.transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    description TEXT,
    reference VARCHAR(100) UNIQUE, -- Idempotencia (Anti-fraude)
    status VARCHAR(20) DEFAULT 'POSTED',
    version INTEGER DEFAULT 1, -- Optimistic Locking
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
