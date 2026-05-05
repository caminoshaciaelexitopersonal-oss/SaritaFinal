-- v10_stabilization_columns.sql
-- Normalización global de columnas de trazabilidad

DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema IN ('core', 'identity', 'governance', 'tourism', 'erp', 'finance', 'ai_core')
        AND table_type = 'BASE TABLE'
    LOOP
        -- tenant_id
        IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema = r.table_schema AND table_name = r.table_name AND column_name = 'tenant_id') THEN
            EXECUTE format('ALTER TABLE %I.%I ADD COLUMN tenant_id UUID', r.table_schema, r.table_name);
        END IF;

        -- trace_id
        IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema = r.table_schema AND table_name = r.table_name AND column_name = 'trace_id') THEN
            EXECUTE format('ALTER TABLE %I.%I ADD COLUMN trace_id UUID', r.table_schema, r.table_name);
        END IF;

        -- context_id
        IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema = r.table_schema AND table_name = r.table_name AND column_name = 'context_id') THEN
            EXECUTE format('ALTER TABLE %I.%I ADD COLUMN context_id UUID', r.table_schema, r.table_name);
        END IF;
    END LOOP;
END $$;
