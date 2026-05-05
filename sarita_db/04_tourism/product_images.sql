-- Galería de Imágenes de Productos
CREATE TABLE tourism.artisan_product_images (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    producto_id UUID NOT NULL,
    image_url TEXT NOT NULL,
    orden_visualizacion INT DEFAULT 1,
    tipo_imagen TEXT DEFAULT 'galeria', -- principal, galeria, proceso

    created_at TIMESTAMP DEFAULT now()
);
