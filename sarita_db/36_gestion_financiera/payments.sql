-- Gestión Financiera: Pagos
CREATE TABLE core.payments_erp (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL, -- FK en 20_global

    monto DECIMAL(18,2) NOT NULL,
    metodo_pago TEXT NOT NULL,
    estado TEXT DEFAULT 'pendiente',

    fecha_pago TIMESTAMP,
    created_at TIMESTAMP DEFAULT now()
);
