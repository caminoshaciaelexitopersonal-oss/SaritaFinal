-- Test de Mapeo Contable Real
DO $$
DECLARE
    v_tenant_id UUID := '00000000-0000-0000-0000-000000000000';
    v_trace_id UUID := gen_random_uuid();
    v_coa_id UUID;
    v_acc_id UUID;
    v_period_id UUID;
    v_entry_id UUID;
BEGIN
    -- Contexto
    PERFORM set_config('app.current_tenant', v_tenant_id::text, false);

    -- 1. Crear Plan de Cuentas
    INSERT INTO accounting.charts_of_accounts (name, tenant_id, trace_id)
    VALUES ('Plan Único de Cuentas - Prueba', v_tenant_id, v_trace_id)
    RETURNING id INTO v_coa_id;

    -- 2. Crear Cuenta
    INSERT INTO accounting.accounts (chart_of_accounts_id, code, name, account_type, tenant_id, trace_id)
    VALUES (v_coa_id, '110505', 'Caja General', 'ASSET', v_tenant_id, v_trace_id)
    RETURNING id INTO v_acc_id;

    -- 3. Crear Periodo Fiscal
    INSERT INTO accounting.fiscal_periods (name, start_date, end_date, tenant_id, trace_id)
    VALUES ('Marzo 2026', '2026-03-01', '2026-03-31', v_tenant_id, v_trace_id)
    RETURNING id INTO v_period_id;

    -- 4. Iniciar Asiento (Trigger ES + AI)
    INSERT INTO accounting.journal_entries (period_id, created_by, event_type, tenant_id, trace_id)
    VALUES (v_period_id, v_tenant_id, 'VENTA', v_tenant_id, v_trace_id)
    RETURNING id INTO v_entry_id;

    -- 5. Crear Líneas (Débito)
    INSERT INTO accounting.journal_entry_lines (journal_entry_id, account_id, debit_amount, tenant_id, trace_id)
    VALUES (v_entry_id, v_acc_id, 500.00, v_tenant_id, v_trace_id);

    -- 6. Validar que la IA fue notificada (Trigger check)
    IF NOT EXISTS (SELECT 1 FROM ai_memory.agent_events WHERE trace_id = v_trace_id) THEN
        RAISE EXCEPTION 'Falla: El evento contable no se notificó a la capa de IA';
    END IF;

    RAISE NOTICE 'Test Contable (Mapeo Real): PASSED';
END;
$$;
