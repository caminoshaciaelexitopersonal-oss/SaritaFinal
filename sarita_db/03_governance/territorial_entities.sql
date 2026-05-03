CREATE TABLE governance.territorial_entities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    name TEXT NOT NULL,
    type TEXT NOT NULL, -- pais, departamento, municipio
    dane_code TEXT UNIQUE,
    parent_id UUID, -- FK en 20_global
    location GEOGRAPHY(POLYGON, 4326),
    created_at TIMESTAMP DEFAULT now(),
    hash_integridad TEXT,
    trace_id UUID
);
