CREATE TABLE core.video_scenes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    project_id UUID NOT NULL, -- FK en 20_global
    order_index INT NOT NULL,

    asset_id UUID NOT NULL,   -- FK a media_assets
    duration_seconds DECIMAL(5,2),
    transition_effect TEXT,

    created_at TIMESTAMP DEFAULT now()
);
