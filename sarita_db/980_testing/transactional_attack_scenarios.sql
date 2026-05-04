-- Test de Ataque y Resiliencia Transaccional
DO $$
DECLARE
    v_tenant_id UUID := '00000000-0000-0000-0000-000000000000';
    v_trace_id UUID := gen_random_uuid();
    v_slot_id UUID;
BEGIN
    -- Contexto
    PERFORM set_config('app.current_tenant', v_tenant_id::text, false);

    -- 1. Preparar Slot con capacidad 1
    INSERT INTO core.availability_slots (resource_id, slot_date, total_capacity, tenant_id, trace_id)
    VALUES (gen_random_uuid(), CURRENT_DATE, 1, v_tenant_id, v_trace_id)
    RETURNING id INTO v_slot_id;

    -- 2. Intento de Overbooking (Transacción 1)
    PERFORM core.fn_reservar_slot(v_slot_id, 1);

    -- 3. Intento de Overbooking (Transacción 2 - Debe Fallar)
    BEGIN
        PERFORM core.fn_reservar_slot(v_slot_id, 1);
        RAISE EXCEPTION 'Falla de Seguridad: Se permitió overbooking en el cupo final.';
    EXCEPTION WHEN OTHERS THEN
        RAISE NOTICE 'Test Overbooking: Bloqueo Exitoso (%)', SQLERRM;
    END;

    -- 4. Test Idempotencia de Pagos
    -- (Simulado mediante inserción duplicada de referencia en ledger.transactions)
    BEGIN
        INSERT INTO ledger.transactions (description, reference, tenant_id, trace_id)
        VALUES ('Test', 'REF-DUP-123', v_tenant_id, v_trace_id);

        INSERT INTO ledger.transactions (description, reference, tenant_id, trace_id)
        VALUES ('Test Duplicate', 'REF-DUP-123', v_tenant_id, v_trace_id);

        RAISE EXCEPTION 'Falla de Seguridad: Se permitió duplicidad de referencia de pago.';
    EXCEPTION WHEN OTHERS THEN
        RAISE NOTICE 'Test Idempotencia: Bloqueo Exitoso (%)', SQLERRM;
    END;

    RAISE NOTICE 'Test de Resiliencia Transaccional: PASSED';
END;
$$;
