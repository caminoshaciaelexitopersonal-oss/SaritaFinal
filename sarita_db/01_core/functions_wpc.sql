-- Función de Entrada Global WPC
CREATE OR REPLACE FUNCTION core.fn_procesar_intencion_wpc(p_intent_id UUID)
RETURNS JSONB AS $$
DECLARE
    v_intent RECORD;
    v_result JSONB;
BEGIN
    -- 1. Cargar intención
    SELECT * INTO v_intent FROM core.wpc_intents WHERE id = p_intent_id;

    IF v_intent.status != 'pendiente' THEN
        RAISE EXCEPTION 'Intención ya procesada o inválida.';
    END IF;

    -- 2. Validar tipo y despachar
    IF v_intent.intent_type = 'compra' THEN
        -- Llamar a creación de orden (lógica delegada)
        NULL;
    ELSIF v_intent.intent_type = 'reserva' THEN
        -- Llamar a creación de reserva
        NULL;
    END IF;

    -- 3. Marcar como completada
    UPDATE core.wpc_intents SET status = 'completado' WHERE id = p_intent_id;

    RETURN jsonb_build_object('status', 'success', 'intent_id', p_intent_id);
END;
$$ LANGUAGE plpgsql;
