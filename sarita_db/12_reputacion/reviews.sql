-- Sistema de Reputación: Reseñas
CREATE TABLE tourism.provider_reviews (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL, -- FK en 20_global
    user_id UUID NOT NULL,     -- FK en 20_global

    rating INT CHECK (rating BETWEEN 1 AND 5),
    comentario TEXT,
    verificado BOOLEAN DEFAULT false,

    created_at TIMESTAMP DEFAULT now()
);
