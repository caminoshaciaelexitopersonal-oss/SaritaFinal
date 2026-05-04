-- Etapas de Producción
CREATE TABLE tourism.artisan_production_stages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    orden_id UUID NOT NULL,
    etapa_nombre TEXT NOT NULL, -- diseño, fabricacion, secado, terminado
    estado TEXT DEFAULT 'pendiente',

    order_index INT NOT NULL,
    started_at TIMESTAMP,
    finished_at TIMESTAMP
);
