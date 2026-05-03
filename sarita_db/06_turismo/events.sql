CREATE TABLE tourism.events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    name TEXT NOT NULL,
    type TEXT,
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    location GEOGRAPHY(POINT, 4326),
    organizer_entity_id UUID, -- FK en 20_global
    related_attraction_id UUID, -- FK en 20_global
    created_at TIMESTAMP DEFAULT now(),
    hash_integridad TEXT,
    trace_id UUID
);
