CREATE TABLE core.budget_lines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,
    version INT DEFAULT 1,

    budget_id UUID NOT NULL, -- FK en 20_global
    category TEXT NOT NULL, -- ventas, costos, gastos_admin, marketing

    amount_planned DECIMAL(18,2) NOT NULL,
    amount_actual DECIMAL(18,2) DEFAULT 0.00,
    variation DECIMAL(18,2) DEFAULT 0.00,

    created_at TIMESTAMP DEFAULT now()
);
