CREATE TABLE reconciliation.matches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    movement_id UUID NOT NULL, -- FK in 20_global
    ledger_transaction_id UUID NOT NULL, -- Ref to ledger.transactions
    match_type VARCHAR(20), -- AUTOMATIC, MANUAL
    confidence_score FLOAT,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
