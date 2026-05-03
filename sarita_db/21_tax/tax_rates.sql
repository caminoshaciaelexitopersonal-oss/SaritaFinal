CREATE TABLE tax.tax_rates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    rule_id UUID NOT NULL, -- FK in 20_global
    valid_from DATE NOT NULL,
    valid_to DATE,
    rate DECIMAL(5,4) NOT NULL,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
