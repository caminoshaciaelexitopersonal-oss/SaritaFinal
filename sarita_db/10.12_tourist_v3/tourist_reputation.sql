-- 02_identity/tourist_reputation.sql
-- Sistema de Reputación del Turista (Antifraude y Confianza)
CREATE TABLE IF NOT EXISTS identity.tourist_reputation (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL UNIQUE REFERENCES identity.tourist_profiles(id),
    trust_score DECIMAL(5,2) DEFAULT 100.00, -- 0-100
    total_bookings INTEGER DEFAULT 0,
    completed_bookings INTEGER DEFAULT 0,
    cancelled_bookings_by_tourist INTEGER DEFAULT 0,
    no_show_count INTEGER DEFAULT 0,
    verified_reviews_count INTEGER DEFAULT 0,
    flags JSONB DEFAULT '[]', -- Reportes de prestadores (comportamiento, daños, etc)
    is_trusted BOOLEAN DEFAULT TRUE,
    is_banned BOOLEAN DEFAULT FALSE,
    ban_reason TEXT,
    tenant_id UUID NOT NULL,
    trace_id UUID,
    last_recalculation_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE INDEX idx_tourist_reputation_score ON identity.tourist_reputation(trust_score);
CREATE INDEX idx_tourist_reputation_trusted ON identity.tourist_reputation(is_trusted);
