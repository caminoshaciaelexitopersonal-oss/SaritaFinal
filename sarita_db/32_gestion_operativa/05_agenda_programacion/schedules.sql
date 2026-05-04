-- Agenda y Programación (Universal)
CREATE TABLE core.schedules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    resource_id UUID, -- Opcional, agenda de un recurso o general
    unit_id UUID,     -- Opcional, agenda de una sede

    day_of_week INT NOT NULL, -- 0-6
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
