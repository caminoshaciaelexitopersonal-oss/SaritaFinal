-- Financiamiento: Préstamos
CREATE TABLE core.loans (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,
    version INT DEFAULT 1,

    lender_entity TEXT NOT NULL,
    principal_amount DECIMAL(18,2) NOT NULL,
    interest_rate DECIMAL(5,4) NOT NULL, -- 0.1200 = 12%
    term_months INT NOT NULL,

    loan_type TEXT NOT NULL, -- bancario, privado, leasing
    status TEXT DEFAULT 'activo',

    disbursed_at DATE,
    created_at TIMESTAMP DEFAULT now()
);
