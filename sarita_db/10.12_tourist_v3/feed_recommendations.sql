-- 02_identity/tourist_feed_recommendations.sql
-- Motor de Feed Dinámico (Recomendaciones IA)
CREATE TABLE IF NOT EXISTS identity.tourist_feed_recommendations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    object_type VARCHAR(50) NOT NULL, -- PROVIDER, PRODUCT, EVENT, ATTRACTION
    object_id UUID NOT NULL,
    relevance_score DECIMAL(7,4), -- Calculado por IA (0-100)
    recommendation_reason VARCHAR(100), -- SIMILAR_TO_FAVORITES, TRENDING_NEARBY, SEASONAL
    expires_at TIMESTAMPTZ,
    is_dismissed BOOLEAN DEFAULT FALSE,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_tourist_feed_relevance ON identity.tourist_feed_recommendations(tourist_id, relevance_score DESC);
CREATE INDEX idx_tourist_feed_active ON identity.tourist_feed_recommendations(is_dismissed) WHERE is_dismissed IS FALSE;
