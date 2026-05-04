-- Subsistema de Citas (Vía 3)
CREATE TABLE core.appointments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    appointment_type TEXT NOT NULL, -- guia, asesor_turismo, servicio_especial
    reference_id UUID, -- Ref al guia o servicio

    status TEXT DEFAULT 'pendiente', -- pendiente, confirmado, cancelado, completado
    reason TEXT,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
