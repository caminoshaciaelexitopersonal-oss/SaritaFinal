-- Artesanos: Identidad Productiva (Extensión de identity.users)
CREATE TYPE tourism.artisan_type AS ENUM ('independiente', 'asociacion', 'colectivo');

CREATE TABLE tourism.artisans (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL UNIQUE, -- FK en 20_global
    tipo_artesano tourism.artisan_type NOT NULL,
    especialidad TEXT, -- tejedor, ceramista, orfebre
    experiencia_anios INT,

    descripcion TEXT,
    estado TEXT DEFAULT 'activo', -- activo, inactivo, suspendido

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
