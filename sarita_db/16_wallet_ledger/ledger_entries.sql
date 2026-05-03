CREATE TABLE ledger.ledger_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    transaction_id UUID NOT NULL, -- FK en 20_global
    account_id UUID NOT NULL, -- FK en 20_global
    debit DECIMAL(18,2) DEFAULT 0,
    credit DECIMAL(18,2) DEFAULT 0,
    entry_version INTEGER DEFAULT 1,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT,
    CONSTRAINT chk_double_entry CHECK ((debit > 0 AND credit = 0) OR (credit > 0 AND debit = 0))
) PARTITION BY RANGE (created_at);
