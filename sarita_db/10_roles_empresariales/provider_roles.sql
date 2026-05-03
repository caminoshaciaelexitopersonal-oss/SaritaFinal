-- Usuarios y Roles Empresariales
CREATE TYPE tourism.provider_role_type AS ENUM ('admin', 'gerente', 'operativo', 'financiero');

CREATE TABLE tourism.provider_roles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL, -- FK en 20_global
    user_id UUID NOT NULL,     -- FK en 20_global

    rol tourism.provider_role_type NOT NULL,
    nivel_autoridad INT DEFAULT 1,
    permisos JSONB DEFAULT '{}',

    activo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
