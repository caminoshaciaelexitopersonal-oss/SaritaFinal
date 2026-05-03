CREATE TABLE governance.positions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    department_id UUID NOT NULL, -- FK en 20_global
    title TEXT NOT NULL,
    level TEXT NOT NULL, -- directivo, profesional, técnico, asistencial
    created_at TIMESTAMP DEFAULT now(),
    hash_integridad TEXT,
    trace_id UUID
);
