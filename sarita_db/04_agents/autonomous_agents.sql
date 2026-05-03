CREATE TABLE agents.autonomous_agents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    persona_type VARCHAR(100),
    capabilities JSONB DEFAULT '[]',
    status VARCHAR(20) DEFAULT 'IDLE',
    user_id UUID REFERENCES identity.users(id),
    tenant_id UUID REFERENCES core.tenants(id),
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
