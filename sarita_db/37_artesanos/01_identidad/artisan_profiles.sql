-- Perfil Público del Artesano
CREATE TABLE tourism.artisan_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    artisan_id UUID NOT NULL UNIQUE, -- FK en 20_global
    nombre_marca TEXT NOT NULL,
    historia TEXT,
    enfoque_cultural TEXT,
    certificaciones JSONB DEFAULT '[]',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
