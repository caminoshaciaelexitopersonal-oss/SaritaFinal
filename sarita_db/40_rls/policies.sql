-- Row Level Security (RLS) para aislamiento estricto de inquilinos - HARDENING FASE 10

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

        -- Crear políticas diferenciadas
        EXECUTE format('DROP POLICY IF EXISTS tenant_read_policy ON %I.%I;', s, t);
        EXECUTE format('CREATE POLICY tenant_read_policy ON %I.%I FOR SELECT USING (tenant_id = current_setting(''sarita.current_tenant_id'', true)::UUID);', s, t);

        EXECUTE format('DROP POLICY IF EXISTS tenant_write_policy ON %I.%I;', s, t);
        EXECUTE format('CREATE POLICY tenant_write_policy ON %I.%I FOR INSERT WITH CHECK (tenant_id = current_setting(''sarita.current_tenant_id'', true)::UUID);', s, t);

        EXECUTE format('DROP POLICY IF EXISTS tenant_update_policy ON %I.%I;', s, t);
        EXECUTE format('CREATE POLICY tenant_update_policy ON %I.%I FOR UPDATE USING (tenant_id = current_setting(''sarita.current_tenant_id'', true)::UUID);', s, t);

        -- Protección especial para tablas Inmutables (Event Sourcing / Ledger Entries)
        IF t IN ('event_store', 'ledger_entries', 'system_logs') THEN
            EXECUTE format('DROP POLICY IF EXISTS immutable_policy ON %I.%I;', s, t);
            EXECUTE format('CREATE POLICY immutable_policy ON %I.%I FOR UPDATE OR DELETE USING (false);', s, t);
        END IF;

    END LOOP;
END;
$$;
