-- 02_identity/booking_disputes.sql
-- Gestión de Disputas y Reembolsos
CREATE TABLE IF NOT EXISTS identity.booking_disputes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID NOT NULL REFERENCES identity.tourist_bookings(id),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    provider_id UUID NOT NULL,
    reason TEXT NOT NULL,
    evidence_urls JSONB DEFAULT '[]',
    status VARCHAR(50) DEFAULT 'OPEN', -- OPEN, UNDER_REVIEW, RESOLVED_REFUND, RESOLVED_NO_REFUND, CLOSED
    resolution_notes TEXT,
    resolution_amount DECIMAL(19,4),
    tenant_id UUID NOT NULL,
    trace_id UUID,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_booking_disputes_status ON identity.booking_disputes(status);
CREATE INDEX idx_booking_disputes_booking ON identity.booking_disputes(booking_id);
