CREATE TABLE tourism.menu_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    menu_id UUID NOT NULL,
    product_id UUID NOT NULL, -- Ref a core.products

    category TEXT, -- entradas, fuertes, postres
    is_available BOOLEAN DEFAULT true,

    created_at TIMESTAMP DEFAULT now()
);
