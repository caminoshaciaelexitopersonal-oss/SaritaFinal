-- Perfil del Turista (Identidad Extendida de identity.users)
CREATE TABLE tourism.tourist_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL UNIQUE, -- FK en 20_global
    tipo_cliente TEXT DEFAULT 'turista', -- turista, residente, corporativo
    nacionalidad TEXT,
    idioma_preferido TEXT DEFAULT 'es',
    moneda_preferida VARCHAR(3) DEFAULT 'COP',
    nivel_digital TEXT DEFAULT 'medio', -- bajo, medio, alto

    estado TEXT DEFAULT 'activo',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
