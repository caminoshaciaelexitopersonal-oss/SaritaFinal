-- Reservas de Citas
CREATE TABLE core.appointment_bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    appointment_id UUID NOT NULL, -- FK en 20_global
    slot_id UUID NOT NULL,        -- FK en 20_global

    status TEXT DEFAULT 'confirmado',

    created_at TIMESTAMP DEFAULT now()
);
