CREATE TABLE tax.tax_jurisdictions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    country_code VARCHAR(3) NOT NULL,
    region_code VARCHAR(10),
    name VARCHAR(255) NOT NULL,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
