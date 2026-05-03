CREATE TABLE erp_contable.puc_accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code VARCHAR(20) NOT NULL,
    name VARCHAR(255) NOT NULL,
    level INTEGER NOT NULL,
    parent_id UUID REFERENCES erp_contable.puc_accounts(id),
    account_type VARCHAR(20), -- DEBITO, CREDITO
    tenant_id UUID REFERENCES core.tenants(id),
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT,
    UNIQUE(tenant_id, code)
);
