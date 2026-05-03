CREATE TABLE governance.public_officials (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    user_id UUID NOT NULL, -- FK en 20_global
    entity_id UUID NOT NULL, -- FK en 20_global
    position_id UUID NOT NULL, -- FK en 20_global
    employment_type TEXT, -- carrera, libre nombramiento, contratista
    start_date DATE,
    end_date DATE,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT now(),
    hash_integridad TEXT,
    trace_id UUID
);
