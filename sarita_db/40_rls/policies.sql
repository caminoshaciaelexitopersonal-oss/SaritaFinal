-- Row Level Security (RLS) para aislamiento estricto de inquilinos (Multi-tenancy)

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
            'erp_archivistico', 'wallet', 'delivery', 'ai_memory', 'integraciones', 'auditoria'
        ) AND table_type = 'BASE TABLE'
    LOOP
        -- Habilitar RLS
        EXECUTE format('ALTER TABLE %I.%I ENABLE ROW LEVEL SECURITY;', s, t);

        -- Crear política por tenant_id
        -- Se asume que el backend setea 'sarita.current_tenant_id' en la sesión
        EXECUTE format('DROP POLICY IF EXISTS tenant_isolation_policy ON %I.%I;', s, t);
        EXECUTE format('CREATE POLICY tenant_isolation_policy ON %I.%I USING (tenant_id = current_setting(''sarita.current_tenant_id'', true)::UUID);', s, t);
    END LOOP;
END;
$$;
