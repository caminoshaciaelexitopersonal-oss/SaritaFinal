-- Catálogos: Cuentas Contables (Traducción Directa de Account)
CREATE TABLE accounting.accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    chart_of_accounts_id UUID NOT NULL, -- FK en 20_global
    code VARCHAR(50) NOT NULL,
    name TEXT NOT NULL,
    account_type TEXT NOT NULL, -- ASSET, LIABILITY, EQUITY, REVENUE, EXPENSE

    initial_balance DECIMAL(18,2) DEFAULT 0.00,
    is_active BOOLEAN DEFAULT true,

    ifrs_mapping TEXT,
    consolidation_code TEXT,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now(),

    UNIQUE(chart_of_accounts_id, code)
);
