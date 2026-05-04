-- Test de Motor Operativo Universal
DO $$
DECLARE
    v_tenant_id UUID := '00000000-0000-0000-0000-000000000000';
    v_trace_id UUID := gen_random_uuid();
    v_op_id UUID;
    v_so_id UUID;
    v_unit_id UUID;
    v_resource_id UUID;
BEGIN
    -- Contexto
    PERFORM set_config('app.current_tenant', v_tenant_id::text, false);

    -- 1. Crear Unidad Operacional (Sede)
    INSERT INTO core.operational_units (provider_id, name, unit_type, tenant_id, trace_id)
    VALUES (gen_random_uuid(), 'Sede Norte', 'punto_venta', v_tenant_id, v_trace_id)
    RETURNING id INTO v_unit_id;

    -- 2. Crear Recurso (Personal)
    INSERT INTO core.operational_resources (resource_name, resource_type_id, tenant_id, trace_id)
    VALUES ('Juan Operario', gen_random_uuid(), v_tenant_id, v_trace_id)
    RETURNING id INTO v_resource_id;

    -- 3. Iniciar Operación Transaccional
    INSERT INTO core.business_operations (tipo_operacion, cliente_id, provider_id, tenant_id, trace_id)
    VALUES ('servicio', gen_random_uuid(), gen_random_uuid(), v_tenant_id, v_trace_id)
    RETURNING id INTO v_op_id;

    -- 4. Generar Orden de Servicio (CORE OPERATIVO)
    INSERT INTO core.service_orders_erp (operation_id, status, tenant_id, trace_id)
    VALUES (v_op_id, 'pendiente', v_tenant_id, v_trace_id)
    RETURNING id INTO v_so_id;

    -- 5. Simular Especialización (HOTEL - Extensión)
    INSERT INTO tourism.hotel_rooms (operational_unit_id, room_number, room_type_id, tenant_id, trace_id)
    VALUES (v_unit_id, '101', gen_random_uuid(), v_tenant_id, v_trace_id);

    -- 6. Crear Booking Universal
    INSERT INTO core.bookings_erp (operation_id, resource_id, start_at, end_at, tenant_id, trace_id)
    VALUES (v_op_id, v_resource_id, now(), now() + interval '2 hours', v_tenant_id, v_trace_id);

    -- 7. Validar que la IA vio el booking (Trigger check)
    IF NOT EXISTS (SELECT 1 FROM ai_memory.agent_events WHERE trace_id = v_trace_id) THEN
        RAISE EXCEPTION 'Falla: La IA no fue notificada de la nueva operación operativa';
    END IF;

    RAISE NOTICE 'Test Operativo Universal: PASSED';
END;
$$;
