CREATE TABLE core.campaign_metrics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    campaign_id UUID NOT NULL, -- FK en 20_global
    reach INT DEFAULT 0,
    clicks INT DEFAULT 0,
    conversions INT DEFAULT 0,
    cost_per_conversion DECIMAL(18,2),

    measured_at TIMESTAMP DEFAULT now()
);
