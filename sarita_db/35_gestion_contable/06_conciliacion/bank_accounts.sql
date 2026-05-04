-- Conciliación: Cuentas Bancarias
CREATE TABLE accounting.bank_accounts_erp (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    account_name TEXT NOT NULL,
    account_number TEXT NOT NULL,
    bank_name TEXT NOT NULL,

    currency VARCHAR(3) DEFAULT 'COP',

    created_at TIMESTAMP DEFAULT now(),
    UNIQUE(tenant_id, account_number)
);
