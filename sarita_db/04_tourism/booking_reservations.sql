-- 02_identity/tourist_bookings.sql
-- Reservas y Citas del Turista (Airbnb/Booking style)
CREATE TABLE IF NOT EXISTS identity.tourist_bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    provider_id UUID NOT NULL, -- FK a prestador (vía 2)
    service_id UUID, -- FK a servicio/producto
    start_date TIMESTAMPTZ NOT NULL,
    end_date TIMESTAMPTZ,
    status VARCHAR(50) DEFAULT 'PENDING', -- PENDING, CONFIRMED, CANCELLED, COMPLETED, NO_SHOW
    total_price DECIMAL(19,4) NOT NULL,
    currency VARCHAR(10) DEFAULT 'COP',
    notes TEXT,
    guest_count INTEGER DEFAULT 1,
    metadata JSONB, -- Opciones adicionales de la reserva
    tenant_id UUID NOT NULL,
    trace_id UUID,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE INDEX idx_tourist_bookings_dates ON identity.tourist_bookings(start_date, end_date);
CREATE INDEX idx_tourist_bookings_status ON identity.tourist_bookings(status);
CREATE INDEX idx_tourist_bookings_tourist ON identity.tourist_bookings(tourist_id);
CREATE INDEX idx_tourist_bookings_provider ON identity.tourist_bookings(provider_id);
