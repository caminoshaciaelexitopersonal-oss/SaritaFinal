-- 02_identity/tourist_rewards.sql
-- Sistema de Recompensas y Gamificación
CREATE TABLE IF NOT EXISTS identity.tourist_rewards (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    points_total INTEGER DEFAULT 0,
    tier VARCHAR(20) DEFAULT 'BRONZE', -- BRONZE, SILVER, GOLD, PLATINUM
    unlocked_badges JSONB DEFAULT '[]', -- Lista de IDs de insignias
    last_points_earned_at TIMESTAMPTZ,
    tenant_id UUID NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS identity.tourist_reward_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    points INTEGER NOT NULL,
    reason VARCHAR(100), -- REVIEW_WRITTEN, BOOKING_COMPLETED, PROFILE_COMPLETED
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_tourist_rewards_tier ON identity.tourist_rewards(tier);
