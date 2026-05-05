CREATE TABLE core.content_campaign_links (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    campaign_id UUID NOT NULL, -- FK en 20_global
    asset_id UUID NOT NULL,    -- FK a media_assets en 20_global

    created_at TIMESTAMP DEFAULT now()
);
