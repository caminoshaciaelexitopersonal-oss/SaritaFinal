-- Calificaciones de Artesanos (Vía 3)
CREATE TABLE tourism.artisan_ratings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    artisan_id UUID NOT NULL,
    user_id UUID NOT NULL,

    puntuacion INT CHECK (puntuacion BETWEEN 1 AND 5),
    comentario TEXT,

    created_at TIMESTAMP DEFAULT now()
);
