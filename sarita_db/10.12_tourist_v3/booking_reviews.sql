-- 02_identity/tourist_reviews.sql
-- Reseñas y Calificaciones (Ecosistema de Confianza)
CREATE TABLE IF NOT EXISTS identity.tourist_reviews (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    provider_id UUID NOT NULL,
    booking_id UUID REFERENCES identity.tourist_bookings(id),
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    photos JSONB DEFAULT '[]', -- URLs de fotos de la experiencia
    is_verified_purchase BOOLEAN DEFAULT FALSE,
    response_from_provider TEXT,
    tenant_id UUID NOT NULL,
    trace_id UUID,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE INDEX idx_tourist_reviews_provider ON identity.tourist_reviews(provider_id);
CREATE INDEX idx_tourist_reviews_rating ON identity.tourist_reviews(rating);
