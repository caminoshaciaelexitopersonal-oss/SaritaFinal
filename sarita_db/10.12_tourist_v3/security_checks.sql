-- 02_identity/tourist_security_checks.sql
-- Verificaciones de Seguridad del Turista (Check-ins de seguridad)
CREATE TABLE IF NOT EXISTS identity.tourist_security_checks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    booking_id UUID NOT NULL REFERENCES identity.tourist_bookings(id),
    status VARCHAR(50) DEFAULT 'SAFE', -- SAFE, HELP_REQUESTED, NO_RESPONSE
    last_check_at TIMESTAMPTZ DEFAULT now(),
    emergency_contact_notified BOOLEAN DEFAULT FALSE,
    location_snapshot GEOGRAPHY(POINT, 4326),
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_tourist_sec_check_status ON identity.tourist_security_checks(status);
