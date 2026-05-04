-- Gestión Operativa: Incidentes
CREATE TABLE core.incidents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL, -- FK en 20_global

    tipo TEXT NOT NULL, -- accidente, reclamo, falla_tecnica
    descripcion TEXT,
    estado TEXT DEFAULT 'reportado',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
