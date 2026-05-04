-- Variantes de Producto
CREATE TABLE tourism.artisan_product_variants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    producto_id UUID NOT NULL,
    color TEXT,
    tamano TEXT,
    material_principal TEXT,

    precio_adicional DECIMAL(18,2) DEFAULT 0.00,
    sku TEXT UNIQUE,

    created_at TIMESTAMP DEFAULT now()
);
