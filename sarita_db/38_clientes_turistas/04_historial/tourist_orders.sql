-- Historial Transaccional del Turista (Referencias)
CREATE TABLE core.tourist_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    order_id UUID NOT NULL, -- Ref a core.sales_orders

    order_type TEXT, -- producto, servicio, reserva
    status TEXT,
    total_amount DECIMAL(18,2),

    created_at TIMESTAMP DEFAULT now()
);
