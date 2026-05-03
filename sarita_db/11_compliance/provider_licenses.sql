-- Compliance Legal: Licencias
CREATE TABLE tourism.provider_licenses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL, -- FK en 20_global

    tipo_licencia TEXT NOT NULL, -- RNT, Registro Mercantil, etc.
    numero TEXT NOT NULL,
    pais TEXT DEFAULT 'Colombia',

    fecha_emision DATE NOT NULL,
    fecha_expiracion DATE,

    estado TEXT DEFAULT 'activo',
    documento_url TEXT,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
