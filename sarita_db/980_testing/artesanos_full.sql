-- Test de Dominio Artesanos + Marketplace
DO $$
DECLARE
    v_tenant_id UUID := '00000000-0000-0000-0000-000000000000';
    v_trace_id UUID := gen_random_uuid();
    v_user_id UUID := '00000000-0000-0000-0000-000000000000'; -- Admin
    v_artisan_id UUID;
    v_product_id UUID;
BEGIN
    -- Contexto
    PERFORM set_config('app.current_tenant', v_tenant_id::text, false);

    -- 1. Crear Artesano (Extensión)
    INSERT INTO tourism.artisans (user_id, tipo_artesano, especialidad, tenant_id, trace_id)
    VALUES (v_user_id, 'independiente', 'Tejeduría de Sombreros', v_tenant_id, v_trace_id)
    RETURNING id INTO v_artisan_id;

    -- 2. Crear Ubicación y Taller
    INSERT INTO tourism.artisan_locations (artisan_id, geo_point, tenant_id, trace_id)
    VALUES (v_artisan_id, ST_SetSRID(ST_MakePoint(-73.36, 4.31), 4326), v_tenant_id, v_trace_id);

    -- 3. Crear Producto
    INSERT INTO tourism.artisan_products (artisan_id, nombre, precio_base, tenant_id, trace_id)
    VALUES (v_artisan_id, 'Sombrero Vueltiao Premium', 150000.00, v_tenant_id, v_trace_id)
    RETURNING id INTO v_product_id;

    -- 4. Inicializar Inventario
    INSERT INTO tourism.artisan_inventory (producto_id, stock_actual, tenant_id, trace_id)
    VALUES (v_product_id, 10, v_tenant_id, v_trace_id);

    -- 5. Validar Sincronización Directorio (Trigger check)
    IF NOT EXISTS (SELECT 1 FROM tourism.artisan_directory_index WHERE artisan_id = v_artisan_id) THEN
        RAISE EXCEPTION 'Falla: El artesano no se sincronizó con el índice del directorio';
    END IF;

    -- 6. Validar Notificación IA
    IF NOT EXISTS (SELECT 1 FROM ai_memory.agent_events WHERE trace_id = v_trace_id) THEN
        RAISE EXCEPTION 'Falla: El evento de artesano no se notificó a la capa de IA';
    END IF;

    RAISE NOTICE 'Test Artesanos y Marketplace: PASSED';
END;
$$;
