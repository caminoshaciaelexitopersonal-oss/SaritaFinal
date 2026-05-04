-- Preferencias del Turista (Alimento para IA)
CREATE TABLE tourism.tourist_preferences (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL UNIQUE,
    intereses JSONB DEFAULT '{}', -- {cultura: 5, gastronomia: 3, aventura: 0}
    presupuesto_promedio DECIMAL(18,2),
    tipo_viaje TEXT, -- solo, familia, pareja
    restricciones JSONB DEFAULT '{}', -- {alimentarias: [], movilidad: []}

    updated_at TIMESTAMP DEFAULT now()
);
