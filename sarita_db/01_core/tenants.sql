-- Definición de la entidad fundamental de aislamiento
CREATE TABLE core.tenants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID, -- Referencia al tenant maestro para cumplimiento jerárquico
    name VARCHAR(255) NOT NULL,
    legal_name VARCHAR(255),
    tax_id VARCHAR(50) UNIQUE NOT NULL,
    domain VARCHAR(255) UNIQUE,
    currency VARCHAR(3) DEFAULT 'COP',
    state VARCHAR(20) DEFAULT 'ACTIVE',
    settings JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

COMMENT ON TABLE core.tenants IS 'Entidades (Empresas, Alcaldías, Prestadores) que operan en la plataforma.';
