-- Tesorería: Cuentas Financieras (Efectivo, Bancos, Wallets)
CREATE TYPE core.cash_account_type AS ENUM ('caja', 'banco', 'wallet');

CREATE TABLE core.cash_accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,
    version INT DEFAULT 1,

    name TEXT NOT NULL,
    account_type core.cash_account_type NOT NULL,
    financial_entity TEXT,
    account_number TEXT,
    currency VARCHAR(3) DEFAULT 'COP',
    status TEXT DEFAULT 'activo',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
