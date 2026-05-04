-- Tasas de Impuesto (Traducción de TaxRate)
CREATE TABLE accounting.tax_rates_contable (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    tax_id UUID NOT NULL,
    rate DECIMAL(10,6) NOT NULL,

    effective_from DATE NOT NULL,
    effective_to DATE,

    created_at TIMESTAMP DEFAULT now()
);
