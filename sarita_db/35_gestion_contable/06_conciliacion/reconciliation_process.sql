CREATE TABLE accounting.reconciliation_process (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    bank_account_id UUID NOT NULL,
    period_id UUID NOT NULL,

    bank_balance DECIMAL(18,2),
    book_balance DECIMAL(18,2),
    difference DECIMAL(18,2),

    status TEXT DEFAULT 'en_proceso',

    created_at TIMESTAMP DEFAULT now()
);
