-- Estructura Jerárquica del Plan de Cuentas (PUC)
CREATE TABLE accounting.account_structure (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    level_number INT NOT NULL, -- 1: Clase, 2: Grupo, 4: Cuenta, 6: Subcuenta
    name TEXT NOT NULL,
    digits_length INT NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
