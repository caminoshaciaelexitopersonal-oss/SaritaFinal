CREATE TABLE tourism.transport_trips (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    service_order_id UUID NOT NULL,
    vehicle_id UUID NOT NULL,
    driver_user_id UUID,

    route_id UUID, -- Ref a genérica

    departure_at TIMESTAMP,
    arrival_at TIMESTAMP,

    status TEXT DEFAULT 'programado',

    created_at TIMESTAMP DEFAULT now()
);
