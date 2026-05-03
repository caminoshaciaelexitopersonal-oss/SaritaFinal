-- Scripts de prueba de integridad
SELECT
    schemaname,
    tablename,
    policyname,
    permissive,
    roles,
    cmd,
    qual
FROM pg_policies
WHERE schemaname NOT IN ('pg_catalog', 'information_schema');

-- Verificar que todas las tablas tengan hash_integridad
SELECT table_schema, table_name
FROM information_schema.columns
WHERE column_name = 'hash_integridad'
AND table_schema NOT IN ('pg_catalog', 'information_schema');
