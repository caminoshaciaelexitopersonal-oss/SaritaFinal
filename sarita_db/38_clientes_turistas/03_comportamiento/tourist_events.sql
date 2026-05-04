-- Eventos de Comportamiento del Turista
CREATE TABLE core.tourist_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    event_type TEXT NOT NULL, -- click, busqueda, favorito, compra, abandono
    payload JSONB NOT NULL,

    timestamp TIMESTAMP DEFAULT now()
);
