CREATE TABLE delivery.delivery_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL REFERENCES identity.users(id),
    provider_id UUID NOT NULL REFERENCES erp.tourism_providers(id),
    status VARCHAR(20) DEFAULT 'PENDING',
    origin_address TEXT,
    destination_address TEXT,
    total_amount DECIMAL(18,2),
    tenant_id UUID REFERENCES core.tenants(id),
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
