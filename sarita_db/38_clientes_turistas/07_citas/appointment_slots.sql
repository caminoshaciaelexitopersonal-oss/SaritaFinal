-- Slots de Citas
CREATE TABLE core.appointment_slots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    resource_id UUID NOT NULL, -- Guía o Funcionario
    slot_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,

    capacity INT DEFAULT 1,
    is_available BOOLEAN DEFAULT true,

    created_at TIMESTAMP DEFAULT now(),
    UNIQUE(resource_id, slot_date, start_time)
);
