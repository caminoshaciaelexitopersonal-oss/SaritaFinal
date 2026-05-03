CREATE TABLE governance.government_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES identity.users(id),
    entity_id UUID NOT NULL REFERENCES governance.entities(id),
    cargo VARCHAR(255) NOT NULL,
    nivel VARCHAR(20) NOT NULL,
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT true,
    tenant_id UUID REFERENCES core.tenants(id),
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
