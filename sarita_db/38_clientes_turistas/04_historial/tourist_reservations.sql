CREATE TABLE core.tourist_reservations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    reservation_id UUID NOT NULL, -- Ref a core.sales_reservations o bookings_erp

    resource_type TEXT, -- evento, guia, habitacion
    scheduled_date TIMESTAMP,
    status TEXT,

    created_at TIMESTAMP DEFAULT now()
);
