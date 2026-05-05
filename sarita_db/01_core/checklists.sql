-- Checklist Operativo
CREATE TABLE core.checklists (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL,
    target_type TEXT NOT NULL, -- habitacion, cocina, vehiculo, personal

    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);
