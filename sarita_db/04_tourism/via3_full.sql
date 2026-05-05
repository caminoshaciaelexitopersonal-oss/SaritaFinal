-- Test de Motor de Experiencia Turista (Vía 3)
DO $$
DECLARE
    v_tenant_id UUID := '00000000-0000-0000-0000-000000000000';
    v_trace_id UUID := gen_random_uuid();
    v_user_id UUID := '00000000-0000-0000-0000-000000000001'; -- Turista Test
    v_slot_id UUID;
    v_profile JSONB;
BEGIN
    -- Contexto
    PERFORM set_config('app.current_tenant', v_tenant_id::text, false);

    -- 1. Crear Perfil Turista
    INSERT INTO tourism.tourist_profiles (user_id, nacionalidad, tenant_id, trace_id)
    VALUES (v_user_id, 'Colombiana', v_tenant_id, v_trace_id);

    -- 2. Registrar Ubicación (Trigger Behavior Check)
    INSERT INTO tourism.tourist_locations (user_id, geo_point, tenant_id, trace_id)
    VALUES (v_user_id, ST_SetSRID(ST_MakePoint(-73.36, 4.31), 4326), v_tenant_id, v_trace_id);

    -- 3. Crear Preferencias
    INSERT INTO tourism.tourist_preferences (user_id, intereses, tenant_id, trace_id)
    VALUES (v_user_id, '{"cultura": 10, "naturaleza": 5}', v_tenant_id, v_trace_id);

    -- 4. Simular Búsqueda
    INSERT INTO core.tourist_searches (user_id, search_text, tenant_id, trace_id)
    VALUES (v_user_id, 'sombreros artesanales', v_tenant_id, v_trace_id);

    -- 5. Probar Perfil Dinámico
    v_profile := core.fn_perfil_dinamico_usuario(v_user_id);
    IF v_profile->'preferences' IS NULL THEN
        RAISE EXCEPTION 'Falla: El perfil dinámico no recuperó preferencias.';
    END IF;

    -- 6. Validar que la IA vio los eventos (Trigger check)
    IF (SELECT COUNT(*) FROM core.tourist_events WHERE user_id = v_user_id) = 0 THEN
        RAISE EXCEPTION 'Falla: No se registraron eventos de comportamiento del turista';
    END IF;

    RAISE NOTICE 'Test Experiencia Turista (V3): PASSED';
END;
$$;
