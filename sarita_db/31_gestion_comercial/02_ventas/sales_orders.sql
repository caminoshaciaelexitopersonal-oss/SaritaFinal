-- Refinamiento de Órdenes de Venta
CREATE TABLE core.sales_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    artisan_id UUID,

    status TEXT DEFAULT 'pendiente', -- pendiente, confirmado, cancelado
    total_amount DECIMAL(18,2) DEFAULT 0.00,

    payment_status TEXT DEFAULT 'unpaid', -- unpaid, partial, paid

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
