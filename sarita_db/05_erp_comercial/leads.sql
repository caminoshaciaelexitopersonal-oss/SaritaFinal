CREATE TABLE erp_comercial.leads (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email CITEXT,
    phone VARCHAR(20),
    source VARCHAR(50),
    status VARCHAR(20) DEFAULT 'NEW',
    tenant_id UUID REFERENCES core.tenants(id),
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
