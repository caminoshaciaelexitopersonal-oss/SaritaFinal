-- Estructura base para auditoría y trazabilidad en todas las tablas
-- Esta definición se usará como referencia para los scripts de dominio

/*
PATRÓN OBLIGATORIO PARA TABLAS SARITA:
- id UUID PRIMARY KEY DEFAULT gen_random_uuid()
- tenant_id UUID NOT NULL REFERENCES core.tenants(id)
- created_at TIMESTAMPTZ DEFAULT now()
- updated_at TIMESTAMPTZ DEFAULT now()
- created_by UUID (referencia a identity.users)
- hash_integridad TEXT (calculado por trigger)
*/

CREATE OR REPLACE FUNCTION core.update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ language 'plpgsql';
