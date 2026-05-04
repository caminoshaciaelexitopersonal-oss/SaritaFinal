-- Certificaciones de Artesanos
CREATE TABLE tourism.artisan_certifications_extended (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    artisan_id UUID NOT NULL,
    tipo_certificacion TEXT NOT NULL, -- Sello de Calidad, Denominacion de Origen
    entidad_emisora TEXT NOT NULL,

    fecha_certificacion DATE NOT NULL,
    expiry_date DATE,

    created_at TIMESTAMP DEFAULT now()
);
