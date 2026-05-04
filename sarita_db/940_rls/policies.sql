-- Row Level Security (RLS) Estandarizado - LANZAMIENTO GLOBAL

-- El Turista solo puede ver sus propios datos y datos públicos
DO $$
DECLARE
    t text;
    s text;
BEGIN
    FOR s, t IN
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema IN ('tourism', 'core') AND table_type = 'BASE TABLE'
    LOOP
        -- Si la tabla tiene user_id, restringir a su propio ID
        IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema = s AND table_name = t AND column_name = 'user_id') THEN
            EXECUTE format('DROP POLICY IF EXISTS tourist_self_policy ON %I.%I;', s, t);
            EXECUTE format('CREATE POLICY tourist_self_policy ON %I.%I USING (user_id = current_setting(''sarita.current_user_id'', true)::UUID);', s, t);
        END IF;

        -- Tablas de Marketplace (Directorio) son públicas para lectura
        IF t IN ('artisan_directory_index', 'tourist_feed') THEN
            EXECUTE format('DROP POLICY IF EXISTS public_read_policy ON %I.%I;', s, t);
            EXECUTE format('CREATE POLICY public_read_policy ON %I.%I FOR SELECT USING (true);', s, t);
        END IF;
    END LOOP;
END;
$$;
