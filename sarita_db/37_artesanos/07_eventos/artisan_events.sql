-- Relación con Eventos Institucionales
CREATE TABLE tourism.artisan_events_participation (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    artisan_id UUID NOT NULL,
    evento_id UUID NOT NULL, -- Ref a tourism.events (Vía 1)

    tipo_participacion TEXT, -- expositor, tallerista, asistente
    stand_numero TEXT,

    created_at TIMESTAMP DEFAULT now()
);
