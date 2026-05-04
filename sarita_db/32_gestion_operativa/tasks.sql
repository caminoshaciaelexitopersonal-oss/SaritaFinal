-- Gestión Operativa: Tareas
CREATE TABLE core.tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL, -- FK en 20_global

    tipo_tarea TEXT NOT NULL,
    estado TEXT DEFAULT 'pendiente',
    responsable_id UUID, -- FK a users en 20_global

    fecha_inicio TIMESTAMP,
    fecha_fin TIMESTAMP,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
