-- Transacciones Fiscales (Traducción de TaxTransaction)
CREATE TABLE accounting.tax_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_id UUID NOT NULL,
    tax_id UUID NOT NULL,

    base_amount DECIMAL(18,2) NOT NULL,
    tax_amount DECIMAL(18,2) NOT NULL,
    rate_applied DECIMAL(10,6) NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
