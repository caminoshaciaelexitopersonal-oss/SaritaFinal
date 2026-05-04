-- Tipos de Cuenta Contable
CREATE TABLE accounting.account_types (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL, -- ACTIVO, PASIVO, PATRIMONIO, INGRESOS, GASTOS, COSTOS
    normal_balance TEXT NOT NULL, -- DEBITO, CREDITO

    created_at TIMESTAMP DEFAULT now()
);
