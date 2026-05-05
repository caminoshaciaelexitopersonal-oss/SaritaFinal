-- Órdenes de Producción (Mi Taller)
CREATE TABLE tourism.artisan_production_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    artisan_id UUID NOT NULL,
    producto_id UUID NOT NULL,

    cantidad INT NOT NULL,
    estado TEXT DEFAULT 'pendiente', -- pendiente, en_proceso, terminada, cancelada

    fecha_entrega_prometida DATE,
    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
