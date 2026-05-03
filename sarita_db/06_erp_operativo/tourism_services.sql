CREATE TABLE erp_operativo.tourism_services (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    provider_id UUID NOT NULL REFERENCES erp_operativo.tourism_providers(id),
    service_type VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(18,2) NOT NULL,
    capacity INTEGER DEFAULT 0,
    is_available BOOLEAN DEFAULT true,
    tenant_id UUID REFERENCES core.tenants(id),
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
