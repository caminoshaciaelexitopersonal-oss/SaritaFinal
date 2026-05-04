-- Funciones Financieras Avanzadas

-- 4.2 Proyección Financiera
CREATE OR REPLACE FUNCTION core.fn_proyeccion_financiera(p_tenant_id UUID, p_meses INT)
RETURNS TABLE(mes DATE, ingresos_proyectados DECIMAL, gastos_proyectados DECIMAL) AS $$
BEGIN
    RETURN QUERY
    SELECT
        generate_series(CURRENT_DATE, CURRENT_DATE + (p_meses || ' months')::interval, '1 month')::date as mes,
        (SELECT COALESCE(SUM(estimated_amount), 0) FROM core.cash_flow_projections WHERE tenant_id = p_tenant_id AND flow_type = 'entrada') as ingresos,
        (SELECT COALESCE(SUM(estimated_amount), 0) FROM core.cash_flow_projections WHERE tenant_id = p_tenant_id AND flow_type = 'salida') as gastos;
END;
$$ LANGUAGE plpgsql;

-- 4.3 Análisis de Riesgo de Liquidez
CREATE OR REPLACE FUNCTION core.fn_riesgo_financiero(p_tenant_id UUID)
RETURNS TEXT AS $$
DECLARE
    v_cash DECIMAL;
    v_short_term_debt DECIMAL;
BEGIN
    v_cash := core.fn_calcular_flujo_caja(p_tenant_id);

    -- Simplificado: deuda que vence en los próximos 30 días
    SELECT COALESCE(SUM(principal_paid + interest_paid), 0) INTO v_short_term_debt
    FROM core.loan_payments
    WHERE tenant_id = p_tenant_id AND status = 'pendiente' AND paid_at < CURRENT_DATE + interval '30 days';

    IF v_cash < v_short_term_debt THEN RETURN 'ALTO - Insuficiencia para cubrir deuda próxima';
    ELSIF v_cash < v_short_term_debt * 1.5 THEN RETURN 'MEDIO - Liquidez ajustada';
    ELSE RETURN 'BAJO - Posición sólida';
    END IF;
END;
$$ LANGUAGE plpgsql;

-- 4.4 Ejecución Presupuestal
CREATE OR REPLACE FUNCTION core.fn_ejecucion_presupuesto(p_budget_id UUID)
RETURNS VOID AS $$
BEGIN
    UPDATE core.budget_lines bl
    SET amount_actual = (
        SELECT COALESCE(SUM(amount), 0)
        FROM core.cash_flow_actuals cfa
        WHERE cfa.tenant_id = bl.tenant_id
        -- Aquí iría lógica de mapeo de categoría a cuenta contable/origen
    ),
    variation = amount_planned - amount_actual
    WHERE budget_id = p_budget_id;
END;
$$ LANGUAGE plpgsql;
