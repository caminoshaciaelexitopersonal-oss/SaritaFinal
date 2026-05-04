CREATE TABLE tourism.room_types (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL, -- Sencilla, Doble, Suite
    base_capacity INT DEFAULT 1,
    amenities JSONB DEFAULT '[]',

    created_at TIMESTAMP DEFAULT now()
);
