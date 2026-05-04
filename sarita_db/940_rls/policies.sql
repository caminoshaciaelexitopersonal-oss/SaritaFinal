-- Row Level Security (RLS) Estandarizado - GESTIÓN OPERATIVA

-- Aplicar aislamiento por tenant_id a todos los nuevos módulos operativos
DO $$
DECLARE
    t text;
    s text;
BEGIN
    FOR s, t IN
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema IN ('core', 'tourism') AND table_type = 'BASE TABLE'
    LOOP
        -- Habilitar RLS
        EXECUTE format('ALTER TABLE %I.%I ENABLE ROW LEVEL SECURITY;', s, t);

        -- Política obligatoria usando app.current_tenant
        EXECUTE format('DROP POLICY IF EXISTS tenant_isolation_policy ON %I.%I;', s, t);
        EXECUTE format('CREATE POLICY tenant_isolation_policy ON %I.%I USING (tenant_id = current_setting(''app.current_tenant'', true)::UUID);', s, t);
    END LOOP;
END;
$$;
