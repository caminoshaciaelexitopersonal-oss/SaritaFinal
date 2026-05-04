-- Catálogo de Productos de Artesanos (Core)
CREATE TABLE tourism.artisan_products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    artisan_id UUID NOT NULL, -- FK en 20_global
    nombre TEXT NOT NULL,
    descripcion TEXT,

    categoria_id UUID, -- FK en 20_global
    subcategoria TEXT,

    precio_base DECIMAL(18,2) NOT NULL,
    moneda VARCHAR(3) DEFAULT 'COP',

    es_personalizable BOOLEAN DEFAULT false,
    estado TEXT DEFAULT 'activo', -- activo, agotado, discontinuado

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
