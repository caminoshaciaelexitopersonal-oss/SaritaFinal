CREATE TABLE reconciliation.bank_movements (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    bank_account_id UUID NOT NULL,
    transaction_date DATE NOT NULL,
    amount DECIMAL(18,2) NOT NULL,
    reference VARCHAR(255),
    description TEXT,
    external_id VARCHAR(255) UNIQUE,
    match_status VARCHAR(20) DEFAULT 'UNMATCHED',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
