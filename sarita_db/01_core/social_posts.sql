CREATE TABLE core.social_posts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    account_id UUID NOT NULL, -- FK en 20_global
    content_text TEXT,
    asset_id UUID,            -- FK a media_assets

    product_id UUID,          -- Vinculación comercial
    external_post_id TEXT,    -- ID retornado por la API (FB/IG)

    created_at TIMESTAMP DEFAULT now()
);
