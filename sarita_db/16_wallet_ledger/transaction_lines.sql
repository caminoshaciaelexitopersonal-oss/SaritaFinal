CREATE TABLE ledger.transaction_lines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    transaction_id UUID NOT NULL, -- FK in 20_global
    account_id UUID NOT NULL, -- FK in 20_global
    amount DECIMAL(18,2) NOT NULL,
    description TEXT,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
