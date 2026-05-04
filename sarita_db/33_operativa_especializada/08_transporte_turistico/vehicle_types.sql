CREATE TABLE tourism.vehicle_types (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL, -- Bus, Van, 4x4, Lancha
    capacity_seats INT NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
