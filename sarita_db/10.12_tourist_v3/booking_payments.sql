-- 02_identity/tourist_payments.sql
-- Pagos realizados por el Turista
CREATE TABLE IF NOT EXISTS identity.tourist_payments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    booking_id UUID REFERENCES identity.tourist_bookings(id),
    amount DECIMAL(19,4) NOT NULL,
    fee_platform DECIMAL(19,4) DEFAULT 0,
    payment_method_id UUID, -- Referencia a métodos guardados
    external_reference TEXT, -- ID de pasarela (Stripe, Kushki, etc)
    status VARCHAR(50) DEFAULT 'PENDING', -- PENDING, COMPLETED, FAILED, REFUNDED
    receipt_url TEXT,
    tenant_id UUID NOT NULL,
    trace_id UUID,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE INDEX idx_tourist_payments_tourist ON identity.tourist_payments(tourist_id);
CREATE INDEX idx_tourist_payments_status ON identity.tourist_payments(status);
CREATE INDEX idx_tourist_payments_booking ON identity.tourist_payments(booking_id);
