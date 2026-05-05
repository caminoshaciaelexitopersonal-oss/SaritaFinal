-- 02_identity/tourist_favorites.sql
-- Favoritos y Wishlists del Turista
CREATE TABLE IF NOT EXISTS identity.tourist_favorites (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    object_type VARCHAR(50) NOT NULL, -- PROVIDER, PRODUCT, ATTRACTION, EVENT
    object_id UUID NOT NULL,
    collection_name TEXT DEFAULT 'General', -- Para multiples listas de deseos
    notes TEXT,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_tourist_fav_tourist ON identity.tourist_favorites(tourist_id);
CREATE INDEX idx_tourist_fav_object ON identity.tourist_favorites(object_type, object_id);
