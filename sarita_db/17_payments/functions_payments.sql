-- Función Central de Confirmación de Pagos
CREATE OR REPLACE FUNCTION core.fn_confirmar_pago(p_payment_intent_id UUID)
RETURNS JSONB AS $$
DECLARE
    v_payment RECORD;
    v_order_id UUID;
    v_op_payload JSONB;
BEGIN
    -- 1. Cargar y bloquear intento de pago
    SELECT * INTO v_payment FROM payments.payment_intents WHERE id = p_payment_intent_id FOR UPDATE;

    IF v_payment.status = 'SUCCEEDED' THEN
        RETURN jsonb_build_object('status', 'already_processed');
    END IF;

    -- 2. Vincular con Orden
    v_order_id := (v_payment.metadata->>'order_id')::UUID;

    -- 3. Ejecutar Operación Financiera (Llamada al Engine central)
    v_op_payload := jsonb_build_object(
        'aggregate_id', v_order_id,
        'aggregate_type', 'core.sales_orders',
        'event_type', 'payment_confirmed',
        'amount', v_payment.amount,
        'account_debit', gen_random_uuid(), -- Cuenta de Banco
        'account_credit', gen_random_uuid(), -- Cuenta de Ventas
        'reference', 'PAY-' || p_payment_intent_id,
        'trace_id', v_payment.trace_id
    );

    PERFORM core.fn_execute_financial_operation(v_payment.tenant_id, v_op_payload);

    -- 4. Actualizar estados
    UPDATE payments.payment_intents SET status = 'SUCCEEDED', updated_at = now() WHERE id = p_payment_intent_id;
    UPDATE core.sales_orders SET payment_status = 'paid', status = 'confirmado', updated_at = now() WHERE id = v_order_id;

    RETURN jsonb_build_object('status', 'success', 'order_id', v_order_id);
END;
$$ LANGUAGE plpgsql;
