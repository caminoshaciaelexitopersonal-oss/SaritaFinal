-- Hard Enforcement de Contexto Multi-inquilino
CREATE OR REPLACE FUNCTION core.fn_enforce_tenant()
RETURNS TRIGGER AS $$
BEGIN
    IF current_setting('app.current_tenant', true) IS NULL OR current_setting('app.current_tenant', true) = '' THEN
        RAISE EXCEPTION 'SECURITY BREACH: Tenant context not defined for operation on %', TG_TABLE_NAME;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar como trigger BEFORE a todas las tablas de dominio críticas
DO $$
DECLARE
    t text;
    s text;
BEGIN
    FOR s, t IN
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema IN (
            'identity', 'governance', 'erp_operativo', 'ledger', 'payments', 'kyc', 'events'
        ) AND table_type = 'BASE TABLE'
    LOOP
        EXECUTE format('DROP TRIGGER IF EXISTS trg_tenant_guard ON %I.%I;', s, t);
        EXECUTE format('CREATE TRIGGER trg_tenant_guard BEFORE INSERT OR UPDATE OR DELETE ON %I.%I FOR EACH ROW EXECUTE FUNCTION core.fn_enforce_tenant();', s, t);
    END LOOP;
END;
$$;
