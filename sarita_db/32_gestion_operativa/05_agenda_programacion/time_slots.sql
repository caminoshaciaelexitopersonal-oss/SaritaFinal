CREATE TABLE core.time_slots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    schedule_id UUID NOT NULL,
    slot_start TIME NOT NULL,
    duration_minutes INT NOT NULL,

    capacity_limit INT DEFAULT 1,

    created_at TIMESTAMP DEFAULT now()
);
