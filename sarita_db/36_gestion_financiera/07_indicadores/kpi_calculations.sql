CREATE TABLE core.kpi_calculations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    kpi_id UUID NOT NULL,
    formula_expression TEXT NOT NULL,
    frequency_days INT DEFAULT 30,

    last_execution TIMESTAMP,
    created_at TIMESTAMP DEFAULT now()
);
