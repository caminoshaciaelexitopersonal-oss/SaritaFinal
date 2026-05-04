-- 02_identity/tourist_session_events.sql
-- Eventos de sesión en tiempo real para análisis de fricción
CREATE TABLE IF NOT EXISTS identity.tourist_session_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID REFERENCES identity.tourist_profiles(id),
    session_id UUID NOT NULL,
    event_type VARCHAR(100) NOT NULL, -- PAGE_VIEW, BUTTON_CLICK, SEARCH_START, etc.
    metadata JSONB,
    path TEXT,
    duration_ms INTEGER,
    tenant_id UUID NOT NULL,
    trace_id UUID,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_tourist_session_sid ON identity.tourist_session_events(session_id);
CREATE INDEX idx_tourist_session_type ON identity.tourist_session_events(event_type);
