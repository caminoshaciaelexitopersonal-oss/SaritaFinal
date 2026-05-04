CREATE TABLE core.service_order_items_erp (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    service_order_id UUID NOT NULL, -- FK en 20_global
    product_id UUID NOT NULL,       -- FK en 20_global (Catálogo)

    quantity INT NOT NULL,
    instructions TEXT,

    created_at TIMESTAMP DEFAULT now()
);
