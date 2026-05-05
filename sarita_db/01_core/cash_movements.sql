-- Tesorería: Movimientos de Efectivo
CREATE TABLE core.cash_movements (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,
    version INT DEFAULT 1,

    cash_account_id UUID NOT NULL, -- FK en 20_global
    movement_type TEXT NOT NULL, -- ingreso, egreso, transferencia
    source_type TEXT NOT NULL, -- venta, gasto, prestamo, inversion

    amount DECIMAL(18,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'COP',

    external_reference_id UUID, -- payment_id or transaction_id
    description TEXT,

    created_at TIMESTAMP DEFAULT now()
);
