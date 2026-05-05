-- 02_identity/tourist_notifications.sql
-- Historial de Notificaciones al Turista
CREATE TABLE IF NOT EXISTS identity.tourist_notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    title TEXT NOT NULL,
    message TEXT NOT NULL,
    type VARCHAR(50), -- BOOKING_CONFIRM, PAYMENT_SUCCESS, PROMOTION, ALERT
    channel VARCHAR(20), -- PUSH, EMAIL, SMS, WHATSAPP
    is_read BOOLEAN DEFAULT FALSE,
    action_url TEXT, -- Link profundo a la app
    metadata JSONB,
    tenant_id UUID NOT NULL,
    trace_id UUID,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_tourist_notif_tourist ON identity.tourist_notifications(tourist_id, is_read);
