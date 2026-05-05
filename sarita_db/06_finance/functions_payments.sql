-- Función Central de Confirmación de Pagos (Versión Corregida para Contabilidad Real)
CREATE OR REPLACE FUNCTION core.fn_confirmar_pago(p_payment_intent_id UUID)
RETURNS JSONB AS $$
DECLARE
    v_payment RECORD;
    v_order_id UUID;
    v_op_payload JSONB;
    v_account_debit UUID;
    v_account_credit UUID;
BEGIN
    -- 1. Cargar y bloquear intento de pago
    SELECT * INTO v_payment FROM finance.payment_intents WHERE id = p_payment_intent_id FOR UPDATE;

    IF v_payment.status = 'SUCCEEDED' THEN
        RETURN jsonb_build_object('status', 'already_processed');
    END IF;

    -- 2. Vincular con Orden
    v_order_id := (v_payment.metadata->>'order_id')::UUID;

    -- 3. Resolver Cuentas Contables (Basado en PUC Estándar)
    -- En producción, esto debería venir de una tabla de configuración de mapeo contable
    -- Por ahora resolvemos por código PUC estándar colombiano (110505: Caja, 4135: Comercio)

    SELECT id INTO v_account_debit FROM accounting.accounts
    WHERE code = '110505' AND tenant_id = v_payment.tenant_id LIMIT 1;

    SELECT id INTO v_account_credit FROM accounting.accounts
    WHERE code = '4135' AND tenant_id = v_payment.tenant_id LIMIT 1;

    -- Validar que las cuentas existan para este tenant
    IF v_account_debit IS NULL OR v_account_credit IS NULL THEN
        RAISE EXCEPTION 'Mapeo contable no configurado para el tenant: %', v_payment.tenant_id;
    END IF;

    -- 4. Ejecutar Operación Financiera (Llamada al Engine central)
    v_op_payload := jsonb_build_object(
        'aggregate_id', v_order_id,
        'aggregate_type', 'core.sales_orders',
        'event_type', 'payment_confirmed',
        'amount', v_payment.amount,
        'account_debit', v_account_debit,
        'account_credit', v_account_credit,
        'reference', 'PAY-' || p_payment_intent_id,
        'trace_id', v_payment.trace_id
    );

    PERFORM core.fn_execute_financial_operation(v_payment.tenant_id, v_op_payload);

    -- 5. Actualizar estados
    UPDATE finance.payment_intents SET status = 'SUCCEEDED', updated_at = now() WHERE id = p_payment_intent_id;
    UPDATE core.sales_orders SET payment_status = 'paid', status = 'confirmado', updated_at = now() WHERE id = v_order_id;

    RETURN jsonb_build_object('status', 'success', 'order_id', v_order_id);
END;
$$ LANGUAGE plpgsql;
