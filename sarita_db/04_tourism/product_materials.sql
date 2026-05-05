-- Materiales de Producto
CREATE TABLE tourism.artisan_product_materials (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    producto_id UUID NOT NULL,
    tipo_material TEXT NOT NULL, -- lana, arcilla, madera
    origen TEXT, -- local, regional, importado

    descripcion TEXT,
    created_at TIMESTAMP DEFAULT now()
);
