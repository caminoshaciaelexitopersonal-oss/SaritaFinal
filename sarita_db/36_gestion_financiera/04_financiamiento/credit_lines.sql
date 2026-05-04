-- Financiamiento: Líneas de Crédito
CREATE TABLE core.credit_lines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    lender_entity TEXT NOT NULL,
    total_limit DECIMAL(18,2) NOT NULL,
    available_amount DECIMAL(18,2) NOT NULL,
    used_amount DECIMAL(18,2) DEFAULT 0.00,

    expiry_date DATE,
    created_at TIMESTAMP DEFAULT now()
);
