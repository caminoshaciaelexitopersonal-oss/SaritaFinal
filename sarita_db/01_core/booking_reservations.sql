-- Reservas de Recursos (Core Booking)
CREATE TABLE core.booking_reservations_core (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    slot_id UUID NOT NULL, -- FK en 20_global

    quantity INT DEFAULT 1,
    status TEXT DEFAULT 'confirmada', -- confirmada, cancelada, checkout

    created_at TIMESTAMP DEFAULT now()
);
