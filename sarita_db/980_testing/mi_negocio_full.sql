-- Test ERP "Mi Negocio" Full
DO $$
DECLARE
    v_tenant_id UUID := '00000000-0000-0000-0000-000000000000';
    v_trace_id UUID := gen_random_uuid();
    v_customer_id UUID;
    v_product_id UUID;
    v_op_id UUID;
    v_provider_id UUID;
BEGIN
    -- Contexto
    PERFORM set_config('app.current_tenant', v_tenant_id::text, false);

    -- 1. Crear Cliente
    INSERT INTO core.customers (nombre, email, tenant_id, trace_id)
    VALUES ('Cliente ERP', 'erp@test.com', v_tenant_id, v_trace_id)
    RETURNING id INTO v_customer_id;

    -- 2. Crear Producto
    INSERT INTO core.products (nombre, tipo, precio, tenant_id, trace_id)
    VALUES ('Servicio Premium', 'servicio', 1000.00, v_tenant_id, v_trace_id)
    RETURNING id INTO v_product_id;

    -- 3. Obtener un Prestador (Vía 2 existente)
    SELECT id INTO v_provider_id FROM tourism.tourism_providers LIMIT 1;

    -- 4. Iniciar Operación
    INSERT INTO core.business_operations (tipo_operacion, cliente_id, provider_id, total_neto, tenant_id, trace_id)
    VALUES ('venta', v_customer_id, v_provider_id, 1000.00, v_tenant_id, v_trace_id)
    RETURNING id INTO v_op_id;

    -- 5. Crear Factura
    INSERT INTO core.invoices (operation_id, numero, total, tenant_id, trace_id)
    VALUES (v_op_id, 'FACT-001', 1000.00, v_tenant_id, v_trace_id);

    -- 6. Validar Trazabilidad (Audit log check)
    IF NOT EXISTS (SELECT 1 FROM auditoria.system_logs WHERE trace_id = v_trace_id) THEN
        RAISE EXCEPTION 'Falla: Trazabilidad ERP no registrada';
    END IF;

    RAISE NOTICE 'Test ERP (Mi Negocio): PASSED';
END;
$$;
