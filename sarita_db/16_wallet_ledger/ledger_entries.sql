CREATE TABLE ledger.ledger_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    transaction_id UUID NOT NULL REFERENCES ledger.transactions(id),
    account_id UUID NOT NULL REFERENCES ledger.accounts(id),
    debit DECIMAL(18,2) DEFAULT 0,
    credit DECIMAL(18,2) DEFAULT 0,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT,
    CONSTRAINT chk_double_entry CHECK ((debit > 0 AND credit = 0) OR (credit > 0 AND debit = 0))
) PARTITION BY RANGE (created_at);
