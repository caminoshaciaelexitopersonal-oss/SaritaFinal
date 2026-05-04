CREATE TABLE core.bookings_erp (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL,

    resource_id UUID, -- Mesa, Habitación, Guía, Asiento
    start_at TIMESTAMP NOT NULL,
    end_at TIMESTAMP NOT NULL,

    status TEXT DEFAULT 'confirmada',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
