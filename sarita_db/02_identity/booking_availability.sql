-- 02_identity/booking_availability.sql
-- Gestión de Disponibilidad Escalable (Calendar Slots)
CREATE TABLE IF NOT EXISTS identity.booking_availability (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    provider_id UUID NOT NULL,
    service_id UUID,
    start_time TIMESTAMPTZ NOT NULL,
    end_time TIMESTAMPTZ NOT NULL,
    capacity INTEGER DEFAULT 1,
    current_bookings INTEGER DEFAULT 0,
    price_override DECIMAL(19,4), -- Precios dinámicos por slot (alta demanda)
    is_active BOOLEAN DEFAULT TRUE,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_booking_avail_provider_time ON identity.booking_availability(provider_id, start_time);
CREATE INDEX idx_booking_avail_service ON identity.booking_availability(service_id);
