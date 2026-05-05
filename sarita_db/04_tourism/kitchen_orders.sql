CREATE TABLE tourism.kitchen_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    service_order_id UUID NOT NULL, -- Ref a genérica
    table_id UUID,

    kitchen_status TEXT DEFAULT 'recibido', -- recibido, preparando, listo, servido

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
