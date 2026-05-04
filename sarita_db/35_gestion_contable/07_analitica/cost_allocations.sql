CREATE TABLE accounting.cost_allocations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    journal_line_id UUID NOT NULL,
    cost_center_id UUID NOT NULL,

    percentage DECIMAL(5,2) DEFAULT 100.00,
    amount DECIMAL(18,2),

    created_at TIMESTAMP DEFAULT now()
);
