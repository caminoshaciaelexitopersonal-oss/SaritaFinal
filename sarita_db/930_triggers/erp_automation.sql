-- ERP Automation: Event Sourcing & AI
DO $$
DECLARE
    t text;
    s text := 'core';
BEGIN
    FOR t IN
        VALUES ('business_operations', 'payments_erp', 'journal_entries', 'documents', 'invoices')
    LOOP
        -- Trigger para Event Sourcing
        EXECUTE format('DROP TRIGGER IF EXISTS trg_es_%I ON %I.%I;', t, s, t);
        EXECUTE format('CREATE TRIGGER trg_es_%I AFTER INSERT OR UPDATE ON %I.%I FOR EACH ROW EXECUTE FUNCTION events.fn_capture_event();', t, s, t);

        -- Trigger para Notificación IA
        EXECUTE format('DROP TRIGGER IF EXISTS trg_ai_%I ON %I.%I;', t, s, t);
        EXECUTE format('CREATE TRIGGER trg_ai_%I AFTER INSERT OR UPDATE ON %I.%I FOR EACH ROW EXECUTE FUNCTION ai_memory.fn_notify_ai_agent();', t, s, t);
    END LOOP;
END;
$$;

-- Validaciones Críticas de ERP
CREATE OR REPLACE FUNCTION core.fn_validate_erp_integrity()
RETURNS TRIGGER AS $$
BEGIN
    -- 1. Evitar asientos contables descuadrados (Trigger on journal_entry insert/update not possible easily on lines, but we check per transaction logic)
    -- Aquí pondríamos chequeos de negocio adicionales
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
