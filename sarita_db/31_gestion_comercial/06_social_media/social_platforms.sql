CREATE TABLE core.social_platforms (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT UNIQUE NOT NULL, -- Facebook, Instagram, TikTok, WhatsApp
    api_base_url TEXT,
    is_active BOOLEAN DEFAULT true,

    created_at TIMESTAMP DEFAULT now()
);
