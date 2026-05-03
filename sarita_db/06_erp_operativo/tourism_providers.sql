CREATE TABLE erp_operativo.tourism_providers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    provider_type VARCHAR(50) NOT NULL,
    owner_id UUID NOT NULL, -- FK in 20_global
    rnt_number VARCHAR(50),
    rnt_validated BOOLEAN DEFAULT false,
    status VARCHAR(20) DEFAULT 'ACTIVE',
    puntuacion_total INTEGER DEFAULT 0,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
