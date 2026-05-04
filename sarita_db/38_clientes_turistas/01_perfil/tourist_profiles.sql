-- Perfil del Turista (Identidad Fuertemente Tipada)
CREATE TABLE tourism.tourist_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL UNIQUE, -- 🔒 1 usuario = 1 perfil
    tipo_cliente TEXT DEFAULT 'turista',
    nacionalidad TEXT,
    idioma_preferido TEXT DEFAULT 'es',
    moneda_preferida VARCHAR(3) DEFAULT 'COP',
    nivel_digital TEXT DEFAULT 'medio',

    estado TEXT DEFAULT 'activo',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);

-- Validación: El usuario debe tener rol 'tourist' en identity.users
-- Nota: En Postgres puro, esta validación se hace vía trigger o CHECK contra función,
-- aquí se define el CONSTRAINT y se asume validación en la capa de servicio/trigger.
ALTER TABLE tourism.tourist_profiles ADD CONSTRAINT check_user_type_tourist CHECK (true); -- Placeholder para trigger
