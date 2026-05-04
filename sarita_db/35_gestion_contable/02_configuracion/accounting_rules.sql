-- Reglas de Contabilización Automática
CREATE TABLE accounting.accounting_rules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    event_type TEXT NOT NULL, -- VENTA_HOSPEDAJE, PAGO_NOMINA
    rule_definition JSONB NOT NULL, -- Mapeo de cuentas y porcentajes

    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);
