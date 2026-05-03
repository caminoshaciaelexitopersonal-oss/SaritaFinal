-- Row Level Security (RLS) Estandarizado - FASE VÍA 2

-- Todas las tablas de tourism heredan aislamiento por tenant_id
DO $$
DECLARE
    t text;
    s text;
BEGIN
    FOR s, t IN
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema = 'tourism' AND table_type = 'BASE TABLE'
    LOOP
        -- Habilitar RLS
        EXECUTE format('ALTER TABLE %I.%I ENABLE ROW LEVEL SECURITY;', s, t);

        -- Política por Tenant
        EXECUTE format('DROP POLICY IF EXISTS tenant_isolation_policy ON %I.%I;', s, t);
        EXECUTE format('CREATE POLICY tenant_isolation_policy ON %I.%I USING (tenant_id = current_setting(''app.current_tenant'')::UUID);', s, t);

        -- Política por Provider (Solo si aplica provider_id en la tabla)
        -- Permitir acceso si el usuario tiene un rol asignado a ese prestador
        IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema = s AND table_name = t AND column_name = 'provider_id') THEN
             EXECUTE format('DROP POLICY IF EXISTS provider_access_policy ON %I.%I;', s, t);
             EXECUTE format('CREATE POLICY provider_access_policy ON %I.%I USING (provider_id IN (SELECT provider_id FROM tourism.provider_roles WHERE user_id = current_setting(''sarita.current_user_id'', true)::UUID));', s, t);
        END IF;
    END LOOP;
END;
$$;
