-- v10.18_add_context_id.sql
-- Adición masiva de context_id para cumplimiento SCTA
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema IN ('finance', 'tourism', 'governance', 'erp')
        AND table_type = 'BASE TABLE'
    LOOP
        BEGIN
            EXECUTE format('ALTER TABLE %I.%I ADD COLUMN IF NOT EXISTS context_id UUID', r.table_schema, r.table_name);
        EXCEPTION WHEN OTHERS THEN NULL;
        END;
    END LOOP;
END $$;
