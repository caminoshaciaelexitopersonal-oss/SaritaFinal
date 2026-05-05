-- Membresía en Asociaciones (M:M)
CREATE TABLE tourism.artisan_association_members (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    artisan_id UUID NOT NULL,
    association_id UUID NOT NULL,
    rol_en_asociacion TEXT, -- lider, socio, aprendiz

    joined_at DATE DEFAULT CURRENT_DATE
);
