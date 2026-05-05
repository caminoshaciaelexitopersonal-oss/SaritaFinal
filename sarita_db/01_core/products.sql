-- Catálogo de Productos y Servicios
CREATE TABLE core.products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL, -- producto, servicio, tour, habitacion
    precio DECIMAL(18,2) NOT NULL,
    costo DECIMAL(18,2) DEFAULT 0.00,

    stock_minimo INT DEFAULT 0,
    activo BOOLEAN DEFAULT true,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
