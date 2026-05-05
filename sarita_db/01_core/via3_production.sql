-- Test de Producción Vía 3: Escenarios de Lanzamiento
DO $$
DECLARE
    v_tenant_id UUID := '00000000-0000-0000-0000-000000000000';
    v_trace_id UUID := gen_random_uuid();
    v_user_id UUID := '00000000-0000-0000-0000-000000000002'; -- Turista Producción
    v_slot_id UUID;
    v_rec_count INT;
BEGIN
    -- Contexto
    PERFORM set_config('app.current_tenant', v_tenant_id::text, false);
    PERFORM set_config('sarita.current_user_id', v_user_id::text, false);

    -- 1. Crear Perfil y Cita con Capacidad
    INSERT INTO core.appointment_slots (resource_id, slot_date, start_time, end_time, capacity, tenant_id, trace_id)
    VALUES (gen_random_uuid(), CURRENT_DATE + 1, '10:00', '11:00', 1, v_tenant_id, v_trace_id)
    RETURNING id INTO v_slot_id;

    -- Reservar cita (Debe usar lock)
    PERFORM core.fn_reservar_cita(v_slot_id, v_user_id);

    -- 2. Simular Abandono de Sesión WPC
    INSERT INTO core.tourist_sessions (user_id, channel, session_status, tenant_id, trace_id)
    VALUES (v_user_id, 'web', 'activa', v_tenant_id, v_trace_id);

    UPDATE core.tourist_sessions SET session_status = 'abandonada' WHERE trace_id = v_trace_id;

    -- 3. Probar Recomendaciones Reales (Weighted)
    SELECT COUNT(*) INTO v_rec_count FROM core.fn_generar_recomendaciones_v3(v_user_id);

    -- 4. Inserción en Timeline
    IF NOT EXISTS (SELECT 1 FROM core.tourist_activity_timeline WHERE user_id = v_user_id) THEN
        RAISE EXCEPTION 'Falla: El timeline no registró la actividad del turista';
    END IF;

    RAISE NOTICE 'Test Vía 3 Producción: PASSED (Recs: %)', v_rec_count;
END;
$$;
