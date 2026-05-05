-- Estructura de Costos
CREATE TABLE core.cost_structures (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL, -- FK en 20_global

    tipo_costo TEXT NOT NULL, -- fijos, variables, nomina, insumos
    valor DECIMAL(18,2) NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
