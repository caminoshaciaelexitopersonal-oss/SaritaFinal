-- Etiquetas de Producto (Metadata Cultural)
CREATE TABLE tourism.artisan_product_tags (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    producto_id UUID NOT NULL,
    tag_name TEXT NOT NULL, -- ancestral, sostenible, organico, unico

    created_at TIMESTAMP DEFAULT now()
);
