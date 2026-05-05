-- Inversiones
CREATE TABLE core.investments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,
    version INT DEFAULT 1,

    investment_type TEXT NOT NULL, -- CDT, acciones, cripto, negocio_ajeno
    principal_amount DECIMAL(18,2) NOT NULL,
    estimated_return_rate DECIMAL(5,4),

    status TEXT DEFAULT 'activo',
    start_date DATE NOT NULL,
    end_date DATE,

    created_at TIMESTAMP DEFAULT now()
);
