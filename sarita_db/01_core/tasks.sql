-- Tareas Operativas
CREATE TABLE core.operational_tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    service_order_id UUID, -- Opcional, puede ser tarea suelta
    title TEXT NOT NULL,
    description TEXT,

    status TEXT DEFAULT 'por_hacer',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
