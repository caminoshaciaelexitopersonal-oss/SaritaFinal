CREATE TABLE auditoria.system_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES identity.users(id),
    action VARCHAR(100) NOT NULL,
    table_name VARCHAR(100),
    record_id UUID,
    old_value JSONB,
    new_value JSONB,
    ip_address INET,
    user_agent TEXT,
    tenant_id UUID REFERENCES core.tenants(id),
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
