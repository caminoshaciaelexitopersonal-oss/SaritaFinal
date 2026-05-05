-- Test de Gestión Financiera Real
DO $$
DECLARE
    v_tenant_id UUID := '00000000-0000-0000-0000-000000000000';
    v_trace_id UUID := gen_random_uuid();
    v_account_id UUID;
    v_budget_id UUID;
    v_cash DECIMAL;
BEGIN
    -- Contexto
    PERFORM set_config('app.current_tenant', v_tenant_id::text, false);

    -- 1. Crear Cuenta de Tesorería
    INSERT INTO core.cash_accounts (name, account_type, financial_entity, tenant_id, trace_id)
    VALUES ('Caja Principal ERP', 'caja', 'SARITA Internal', v_tenant_id, v_trace_id)
    RETURNING id INTO v_account_id;

    -- 2. Registrar Movimiento (Ingreso)
    INSERT INTO core.cash_movements (cash_account_id, movement_type, source_type, amount, tenant_id, trace_id)
    VALUES (v_account_id, 'ingreso', 'venta', 5000.00, v_tenant_id, v_trace_id);

    -- 3. Probar Función de Flujo de Caja
    v_cash := core.fn_calcular_flujo_caja(v_tenant_id);
    IF v_cash != 5000.00 THEN
        RAISE EXCEPTION 'Falla: Cálculo de flujo de caja incorrecto (%)', v_cash;
    END IF;

    -- 4. Crear Presupuesto
    INSERT INTO core.budgets (name, period_start, period_end, tenant_id, trace_id)
    VALUES ('Presupuesto Q1 2026', '2026-01-01', '2026-03-31', v_tenant_id, v_trace_id)
    RETURNING id INTO v_budget_id;

    -- 5. Validar Notificación IA (Trigger check)
    IF NOT EXISTS (SELECT 1 FROM ai_memory.agent_events WHERE trace_id = v_trace_id) THEN
        RAISE EXCEPTION 'Falla: El evento financiero no se notificó a la capa de IA';
    END IF;

    RAISE NOTICE 'Test Gestión Financiera Real: PASSED';
END;
$$;
