CREATE TABLE core.consolidated_reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    group_id UUID NOT NULL,
    report_type TEXT NOT NULL, -- balance_general, p_y_g
    period_label TEXT NOT NULL,

    report_json JSONB NOT NULL,
    generated_at TIMESTAMP DEFAULT now()
);
