-- Núcleo del Prestador (Base Universal del Sistema)
CREATE TYPE tourism.provider_status AS ENUM ('activo', 'suspendido', 'bloqueado');

CREATE TABLE tourism.tourism_providers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    nombre_comercial TEXT NOT NULL,
    razon_social TEXT,
    user_id UUID, -- FK a identity.users
    tipo_prestador TEXT NOT NULL, -- HOTEL, RESTAURANTE, GUIA, etc.
    subtipo TEXT,

    estado tourism.provider_status DEFAULT 'activo',

    pais TEXT DEFAULT 'Colombia',
    departamento TEXT,
    ciudad TEXT,
    direccion TEXT,
    geo_point GEOGRAPHY(Point, 4326),

    fecha_registro DATE DEFAULT CURRENT_DATE,
    verificado BOOLEAN DEFAULT false,
    nivel_verificacion INT DEFAULT 0,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
