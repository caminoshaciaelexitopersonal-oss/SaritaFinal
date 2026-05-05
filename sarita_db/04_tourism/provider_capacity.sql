-- Capacidad Operativa de Prestadores
CREATE TABLE tourism.provider_capacity (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL, -- FK en 20_global

    tipo_recurso TEXT NOT NULL, -- mesas, habitaciones, vehículos, cupos
    cantidad_total INT NOT NULL,
    cantidad_disponible INT NOT NULL,

    updated_at TIMESTAMP DEFAULT now()
);
