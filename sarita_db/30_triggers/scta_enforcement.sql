-- 30_triggers/scta_enforcement.sql
-- Control Cognitivo Transversal - ESTABILIZADO CON BYPASS DE SISTEMA

CREATE OR REPLACE FUNCTION infrastructure.fn_scta_validation()
RETURNS TRIGGER AS $$
BEGIN
    -- Misión 5: Permitir procesos internos, migraciones o testing
    -- Se usa el trace_id '00000000-0000-0000-0000-000000000000' como flag de sistema
    IF NEW.trace_id = '00000000-0000-0000-0000-000000000000'::UUID THEN
        RETURN NEW;
    END IF;

    -- Regla 4: Bloqueo si falta tenant_id o trace_id
    IF NEW.tenant_id IS NULL OR NEW.trace_id IS NULL THEN
        RAISE EXCEPTION 'SARITA SCTA ERROR: tenant_id y trace_id son obligatorios';
    END IF;

    -- Regla de context_id con excepción para sistema
    IF NEW.context_id IS NULL THEN
        IF TG_TABLE_NAME IN ('payment_intents', 'ledger_entries', 'tourist_bookings') THEN
             RAISE EXCEPTION 'SARITA SCTA ERROR: context_id es obligatorio para operaciones transaccionales críticas';
        ELSE
             -- Para otras tablas, advertir pero permitir durante estabilización
             RAISE NOTICE 'SARITA SCTA WARNING: context_id ausente en %, se permite por compatibilidad', TG_TABLE_NAME;
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
