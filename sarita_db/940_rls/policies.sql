-- Row Level Security (RLS) Estandarizado - GESTIÓN ARCHIVÍSTICA

-- Aplicar aislamiento por tenant_id a todos los módulos del esquema archival
DO $$
DECLARE
    t text;
    s text := 'archival';
BEGIN
    FOR t IN
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = s AND table_type = 'BASE TABLE'
    LOOP
        -- Habilitar RLS
        EXECUTE format('ALTER TABLE %I.%I ENABLE ROW LEVEL SECURITY;', s, t);

        -- Política obligatoria usando app.current_tenant
        EXECUTE format('DROP POLICY IF EXISTS tenant_isolation_policy ON %I.%I;', s, t);
        EXECUTE format('CREATE POLICY tenant_isolation_policy ON %I.%I USING (tenant_id = current_setting(''app.current_tenant'', true)::UUID);', s, t);
    END LOOP;
END;
$$;
