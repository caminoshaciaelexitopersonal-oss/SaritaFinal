-- Gestión Comercial: Órdenes de Venta
CREATE TABLE core.sales_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL, -- FK en 20_global

    estado TEXT DEFAULT 'borrador',
    total DECIMAL(18,2) DEFAULT 0.00,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
