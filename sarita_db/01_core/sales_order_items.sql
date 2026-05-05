CREATE TABLE core.sales_order_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    sales_order_id UUID NOT NULL, -- FK en 20_global
    product_id UUID NOT NULL,     -- FK en 20_global

    quantity INT NOT NULL,
    unit_price DECIMAL(18,2) NOT NULL,
    discount DECIMAL(18,2) DEFAULT 0.00,
    total DECIMAL(18,2) NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
