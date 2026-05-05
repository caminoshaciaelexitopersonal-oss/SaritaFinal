CREATE TABLE core.campaign_channels (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    campaign_id UUID NOT NULL, -- FK en 20_global
    channel_name TEXT NOT NULL, -- Facebook Ads, Google, Email
    allocated_budget DECIMAL(18,2) DEFAULT 0.00,

    created_at TIMESTAMP DEFAULT now()
);
