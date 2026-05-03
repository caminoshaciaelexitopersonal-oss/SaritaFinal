-- Row Level Security (RLS) Estandarizado - FASE CORRECTIVA FINAL

DO $$
DECLARE
    t text;
    s text;
BEGIN
    FOR s, t IN
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema IN (
            'identity', 'governance', 'agents', 'erp_comercial',
            'erp_operativo', 'erp_contable', 'erp_financiero',
            'erp_archivistico', 'wallet', 'delivery', 'ai_memory',
            'integraciones', 'auditoria', 'events', 'ledger',
            'payments', 'kyc', 'tax', 'reconciliation', 'archival'
        ) AND table_type = 'BASE TABLE'
    LOOP
        -- Habilitar RLS
        EXECUTE format('ALTER TABLE %I.%I ENABLE ROW LEVEL SECURITY;', s, t);

        -- Crear política obligatoria usando app.current_tenant
        EXECUTE format('DROP POLICY IF EXISTS tenant_isolation_policy ON %I.%I;', s, t);
        EXECUTE format('CREATE POLICY tenant_isolation_policy ON %I.%I USING (tenant_id = current_setting(''app.current_tenant'')::UUID);', s, t);

        -- Inmutabilidad para tablas clave
        IF t IN ('event_store', 'ledger_entries', 'system_logs', 'payment_state_transitions') THEN
            EXECUTE format('DROP POLICY IF EXISTS immutable_policy ON %I.%I;', s, t);
            EXECUTE format('CREATE POLICY immutable_policy ON %I.%I FOR UPDATE OR DELETE USING (false);', s, t);
        END IF;

    END LOOP;
END;
$$;

-- Función para validar contexto de sesión
CREATE OR REPLACE FUNCTION core.fn_check_tenant_context()
RETURNS TRIGGER AS $$
BEGIN
    IF current_setting('app.current_tenant', true) IS NULL OR current_setting('app.current_tenant', true) = '' THEN
        RAISE EXCEPTION 'Error de Seguridad: app.current_tenant no está definido en la sesión.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
