-- Asociaciones de Artesanos
CREATE TABLE tourism.artisan_associations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    nombre TEXT NOT NULL,
    tipo_asociacion TEXT, -- cooperativa, fundacion
    cobertura TEXT, -- local, regional, nacional

    created_at TIMESTAMP DEFAULT now()
);
