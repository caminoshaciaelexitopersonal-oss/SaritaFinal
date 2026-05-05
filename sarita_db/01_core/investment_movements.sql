CREATE TABLE core.investment_movements (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    investment_id UUID NOT NULL,
    movement_action TEXT NOT NULL, -- compra, venta, retiro_parcial
    amount DECIMAL(18,2) NOT NULL,

    executed_at TIMESTAMP DEFAULT now()
);
