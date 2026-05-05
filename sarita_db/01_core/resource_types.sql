CREATE TABLE core.resource_types (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    type_name TEXT NOT NULL, -- Personal, Vehiculo, Equipamiento, Insumo
    description TEXT,

    created_at TIMESTAMP DEFAULT now()
);
