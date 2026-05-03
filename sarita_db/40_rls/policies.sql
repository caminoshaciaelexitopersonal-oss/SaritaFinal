-- Row Level Security (RLS) Estandarizado - FASE V1-GOV

DO $$
DECLARE
    t text;
    s text;
BEGIN
    FOR s, t IN
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema IN (
            'identity', 'governance', 'erp_operativo', 'ledger', 'payments',
            'kyc', 'events', 'tourism', 'integrations'
        ) AND table_type = 'BASE TABLE'
    LOOP
        -- Habilitar RLS
        EXECUTE format('ALTER TABLE %I.%I ENABLE ROW LEVEL SECURITY;', s, t);

        -- Crear política obligatoria usando app.current_tenant
        EXECUTE format('DROP POLICY IF EXISTS tenant_isolation_policy ON %I.%I;', s, t);
        EXECUTE format('CREATE POLICY tenant_isolation_policy ON %I.%I USING (tenant_id = current_setting(''app.current_tenant'')::UUID);', s, t);
    END LOOP;
END;
$$;
