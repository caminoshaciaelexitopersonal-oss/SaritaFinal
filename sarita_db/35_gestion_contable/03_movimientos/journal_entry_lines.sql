-- Movimientos Contables: Líneas (Traducción Directa de LedgerEntry)
CREATE TABLE accounting.journal_entry_lines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    journal_entry_id UUID NOT NULL, -- FK en 20_global
    account_id UUID NOT NULL,       -- FK en 20_global

    debit_amount DECIMAL(18,2) DEFAULT 0.00,
    credit_amount DECIMAL(18,2) DEFAULT 0.00,

    -- Multidivisa soporte backend
    currency VARCHAR(3) DEFAULT 'COP',
    amount_transaction DECIMAL(18,2),
    amount_base DECIMAL(18,2),

    description TEXT,
    created_at TIMESTAMP DEFAULT now(),

    CONSTRAINT chk_journal_line CHECK ((debit_amount > 0 AND credit_amount = 0) OR (credit_amount > 0 AND debit_amount = 0))
);
