CREATE TABLE tourism.attractions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    name TEXT NOT NULL,
    category TEXT, -- natural, cultural, patrimonial
    description TEXT,
    location GEOGRAPHY(POINT, 4326),
    municipality_id UUID NOT NULL, -- FK en 20_global
    responsible_entity_id UUID, -- FK en 20_global
    status TEXT,
    created_at TIMESTAMP DEFAULT now(),
    hash_integridad TEXT,
    trace_id UUID
);
