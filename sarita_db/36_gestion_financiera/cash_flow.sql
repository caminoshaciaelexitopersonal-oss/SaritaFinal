-- Gestión Financiera: Flujo de Caja
CREATE TABLE core.cash_flow (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    tipo TEXT NOT NULL, -- ENTRADA, SALIDA
    monto DECIMAL(18,2) NOT NULL,
    fecha DATE DEFAULT CURRENT_DATE,

    referencia_id UUID, -- Ref opcional a operación/pago

    created_at TIMESTAMP DEFAULT now()
);
