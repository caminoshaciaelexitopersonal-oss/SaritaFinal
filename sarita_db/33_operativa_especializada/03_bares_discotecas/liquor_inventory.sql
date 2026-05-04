CREATE TABLE tourism.liquor_inventory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operational_unit_id UUID NOT NULL,
    product_id UUID NOT NULL,

    current_stock_bottles INT DEFAULT 0,
    current_stock_shots INT DEFAULT 0,

    updated_at TIMESTAMP DEFAULT now()
);
