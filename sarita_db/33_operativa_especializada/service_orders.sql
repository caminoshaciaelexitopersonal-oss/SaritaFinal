-- Operativa Especializada: Órdenes de Servicio
CREATE TABLE core.service_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL, -- FK en 20_global

    tipo_servicio TEXT NOT NULL,
    capacidad INT,
    estado TEXT DEFAULT 'en_preparacion',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
