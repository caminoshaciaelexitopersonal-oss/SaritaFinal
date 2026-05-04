-- Función: Cálculo de Flujo de Caja Real
CREATE OR REPLACE FUNCTION core.fn_calcular_flujo_caja(p_tenant_id UUID)
RETURNS DECIMAL AS $$
DECLARE
    v_total_cash DECIMAL;
BEGIN
    -- Sumar todos los movimientos de cuentas de tesorería del inquilino
    SELECT SUM(CASE WHEN movement_type = 'ingreso' THEN amount ELSE -amount END)
    INTO v_total_cash
    FROM core.cash_movements
    WHERE tenant_id = p_tenant_id;

    RETURN COALESCE(v_total_cash, 0.00);
END;
$$ LANGUAGE plpgsql;
