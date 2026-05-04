-- Reseñas del Turista (Vía 3 Side)
CREATE TABLE core.tourist_reviews_extended (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    target_type TEXT NOT NULL, -- prestador, producto, evento
    target_id UUID NOT NULL,

    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment_text TEXT,
    is_verified BOOLEAN DEFAULT false,

    created_at TIMESTAMP DEFAULT now()
);
