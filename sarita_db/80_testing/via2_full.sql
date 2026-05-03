-- Test de Operatividad Vía 2 (Prestadores)
DO $$
DECLARE
    v_provider_id UUID;
    v_user_id UUID := '00000000-0000-0000-0000-000000000000'; -- Admin
    v_tenant_id UUID := '00000000-0000-0000-0000-000000000000';
BEGIN
    -- Configurar contexto
    PERFORM set_config('app.current_tenant', v_tenant_id::text, false);

    -- 1. Crear Prestador
    INSERT INTO tourism.tourism_providers (nombre_comercial, razon_social, tipo_prestador, tenant_id, trace_id)
    VALUES ('Hotel Testing', 'Hotel Test S.A.S.', 'HOTEL', v_tenant_id, gen_random_uuid())
    RETURNING id INTO v_provider_id;

    -- 2. Asignar Rol
    INSERT INTO tourism.provider_roles (provider_id, user_id, rol, tenant_id, trace_id)
    VALUES (v_provider_id, v_user_id, 'admin', v_tenant_id, gen_random_uuid());

    -- 3. Crear Licencia
    INSERT INTO tourism.provider_licenses (provider_id, tipo_licencia, numero, fecha_emision, tenant_id, trace_id)
    VALUES (v_provider_id, 'RNT', '12345', CURRENT_DATE, v_tenant_id, gen_random_uuid());

    -- 4. Registrar en Directorio
    INSERT INTO tourism.provider_directory (provider_id, categoria, tenant_id, trace_id)
    VALUES (v_provider_id, 'Alojamiento', v_tenant_id, gen_random_uuid());

    -- 5. Validar Existencia en Event Store (Trigger Check)
    IF NOT EXISTS (SELECT 1 FROM events.event_store WHERE aggregate_id = v_provider_id) THEN
        RAISE EXCEPTION 'Falla: El prestador no generó evento en event_store';
    END IF;

    RAISE NOTICE 'Test Vía 2 (Negocios): PASSED';
END;
$$;
