-- Favoritos del Turista
CREATE TABLE core.tourist_favorites (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    favoritable_type TEXT NOT NULL, -- producto, artesano, evento, atractivo
    favoritable_id UUID NOT NULL,

    created_at TIMESTAMP DEFAULT now(),
    UNIQUE(user_id, favoritable_type, favoritable_id)
);
