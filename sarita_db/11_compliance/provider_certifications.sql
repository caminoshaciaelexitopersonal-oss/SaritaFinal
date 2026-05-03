-- Compliance Legal: Certificaciones
CREATE TABLE tourism.provider_certifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL, -- FK en 20_global

    nombre_certificacion TEXT NOT NULL,
    entidad_emisora TEXT,
    fecha_emision DATE,
    fecha_expiracion DATE,

    created_at TIMESTAMP DEFAULT now()
);
