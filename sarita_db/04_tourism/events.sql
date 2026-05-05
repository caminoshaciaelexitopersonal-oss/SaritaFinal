-- Eventos de Prestadores
CREATE TABLE tourism.provider_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL, -- FK en 20_global

    nombre TEXT NOT NULL,
    tipo_evento TEXT,

    fecha_inicio TIMESTAMP NOT NULL,
    fecha_fin TIMESTAMP NOT NULL,

    capacidad INT,
    ubicacion GEOGRAPHY(Point, 4326),
    estado TEXT DEFAULT 'programado',

    created_at TIMESTAMP DEFAULT now()
);
