-- Asignación de triggers de auditoría, integridad y tiempo a todas las tablas del sistema

DO $$
DECLARE
    t text;
    s text;
BEGIN
    FOR s, t IN
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema IN (
            'core', 'identity', 'governance', 'agents', 'erp_comercial',
            'erp_operativo', 'erp_contable', 'erp_financiero',
            'erp_archivistico', 'wallet', 'delivery', 'ai_memory', 'integraciones'
        ) AND table_type = 'BASE TABLE'
    LOOP
        -- Trigger para updated_at
        EXECUTE format('DROP TRIGGER IF EXISTS trg_updated_at ON %I.%I;', s, t);
        EXECUTE format('CREATE TRIGGER trg_updated_at BEFORE UPDATE ON %I.%I FOR EACH ROW EXECUTE FUNCTION core.update_updated_at_column();', s, t);

        -- Trigger para hash_integridad
        EXECUTE format('DROP TRIGGER IF EXISTS trg_hash_integridad ON %I.%I;', s, t);
        EXECUTE format('CREATE TRIGGER trg_hash_integridad BEFORE INSERT OR UPDATE ON %I.%I FOR EACH ROW EXECUTE FUNCTION core.fn_generar_hash_integridad();', s, t);

        -- Trigger para auditoría (excepto en la propia tabla de logs para evitar recursión infinita)
        IF t != 'system_logs' AND s != 'auditoria' THEN
            EXECUTE format('DROP TRIGGER IF EXISTS trg_audit ON %I.%I;', s, t);
            EXECUTE format('CREATE TRIGGER trg_audit AFTER INSERT OR UPDATE OR DELETE ON %I.%I FOR EACH ROW EXECUTE FUNCTION auditoria.fn_audit_trigger();', s, t);
        END IF;
    END LOOP;
END;
$$;
