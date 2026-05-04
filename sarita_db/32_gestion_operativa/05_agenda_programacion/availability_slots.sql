-- Disponibilidad de Slots (Airbnb-style)
CREATE TABLE core.availability_slots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    resource_id UUID NOT NULL, -- Ref a productos/habitaciones/mesas
    slot_date DATE NOT NULL,

    total_capacity INT NOT NULL,
    reserved_capacity INT DEFAULT 0,

    is_blocked BOOLEAN DEFAULT false,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now(),
    UNIQUE(resource_id, slot_date)
);
