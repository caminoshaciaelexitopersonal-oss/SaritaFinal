CREATE TABLE core.occupancy_tracking (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    capacity_unit_id UUID NOT NULL,
    current_occupancy INT DEFAULT 0,

    measured_at TIMESTAMP DEFAULT now()
);
