-- Clasificación Cultural y Turística: Categorías
CREATE TABLE tourism.artisan_categories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT UNIQUE NOT NULL, -- Tejeduría, Cestería, Ebanistería
    region_cultural TEXT,
    valor_patrimonial BOOLEAN DEFAULT false,

    created_at TIMESTAMP DEFAULT now()
);
