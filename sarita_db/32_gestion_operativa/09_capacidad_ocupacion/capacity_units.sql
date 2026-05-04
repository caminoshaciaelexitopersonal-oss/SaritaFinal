-- Capacidad y Ocupación (Universal)
CREATE TABLE core.capacity_units (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operational_unit_id UUID NOT NULL,
    resource_type_id UUID NOT NULL, -- Mesa, Habitación, Asiento

    total_capacity INT NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
