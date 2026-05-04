CREATE TABLE tourism.trip_passenger_capacity (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    trip_id UUID NOT NULL,
    total_seats INT NOT NULL,
    available_seats INT NOT NULL,

    updated_at TIMESTAMP DEFAULT now()
);
