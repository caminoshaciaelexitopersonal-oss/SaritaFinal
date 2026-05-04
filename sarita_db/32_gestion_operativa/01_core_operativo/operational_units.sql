-- Core Operativo: Unidades Operacionales
CREATE TABLE core.operational_units (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL, -- FK en 20_global
    name TEXT NOT NULL,
    unit_type TEXT NOT NULL, -- sede, sucursal, punto_venta

    address TEXT,
    location GEOGRAPHY(Point, 4326),

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
