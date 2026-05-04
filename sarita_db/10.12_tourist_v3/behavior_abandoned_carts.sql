-- 02_identity/tourist_abandoned_carts.sql
-- Control de carritos abandonados para recuperación (WPC)
CREATE TABLE IF NOT EXISTS identity.tourist_abandoned_carts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    cart_data JSONB NOT NULL, -- Productos, cantidades, precios
    total_amount DECIMAL(19,4) NOT NULL,
    status VARCHAR(50) DEFAULT 'ABANDONED', -- ABANDONED, RECOVERED, EXPIRED
    recovery_attempts INTEGER DEFAULT 0,
    last_recovery_at TIMESTAMPTZ,
    tenant_id UUID NOT NULL,
    trace_id UUID,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE INDEX idx_tourist_abandoned_status ON identity.tourist_abandoned_carts(status);
CREATE INDEX idx_tourist_abandoned_tourist ON identity.tourist_abandoned_carts(tourist_id);
