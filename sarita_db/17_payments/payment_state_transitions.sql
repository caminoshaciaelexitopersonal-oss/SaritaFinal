-- Máquina de Estados de Pagos Profesional
CREATE TABLE payments.payment_state_transitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    payment_intent_id UUID NOT NULL,
    from_status VARCHAR(20),
    to_status VARCHAR(20) NOT NULL,
    actor_id UUID,
    notes TEXT,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

-- Trigger de Validación y Registro de Transiciones
CREATE OR REPLACE FUNCTION payments.fn_validate_payment_transition()
RETURNS TRIGGER AS $$
BEGIN
    -- Validar estados permitidos: pending, processing, authorized, failed, cancelled, refunded
    IF NOT (
        (OLD.status = 'pending' AND NEW.status IN ('processing', 'cancelled')) OR
        (OLD.status = 'processing' AND NEW.status IN ('authorized', 'failed')) OR
        (OLD.status = 'authorized' AND NEW.status IN ('refunded')) OR
        (OLD.status = 'cancelled' AND NEW.status IS NULL) -- Estado terminal
    ) THEN
        RAISE EXCEPTION 'Transición de Pago Prohibida: % -> %', OLD.status, NEW.status;
    END IF;

    -- Registrar en tabla de transiciones para auditoría legal
    INSERT INTO payments.payment_state_transitions (payment_intent_id, from_status, to_status, tenant_id)
    VALUES (NEW.id, OLD.status, NEW.status, NEW.tenant_id);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
