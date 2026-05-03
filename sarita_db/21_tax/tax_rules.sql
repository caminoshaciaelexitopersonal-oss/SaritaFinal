CREATE TABLE tax.tax_rules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jurisdiction_id UUID NOT NULL, -- FK in 20_global
    name VARCHAR(100) NOT NULL,
    tax_type VARCHAR(50) NOT NULL, -- VAT, ISR, etc
    rate DECIMAL(5,4) NOT NULL,
    conditions JSONB DEFAULT '{}',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
