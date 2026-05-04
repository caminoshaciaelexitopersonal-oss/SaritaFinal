-- Funciones Críticas de Reserva e Inventario

-- 1. Reservar Slot (Con lock preventivo de overbooking)
CREATE OR REPLACE FUNCTION core.fn_reservar_slot(
    p_slot_id UUID,
    p_quantity INT
) RETURNS BOOLEAN AS $$
DECLARE
    v_available INT;
BEGIN
    -- LOCK preventivo sobre la fila del slot
    SELECT (total_capacity - reserved_capacity) INTO v_available
    FROM core.availability_slots
    WHERE id = p_slot_id
    FOR UPDATE;

    IF v_available < p_quantity THEN
        RAISE EXCEPTION 'Capacidad Insuficiente: Solo quedan % cupos.', v_available;
    END IF;

    UPDATE core.availability_slots
    SET reserved_capacity = reserved_capacity + p_quantity,
        updated_at = now()
    WHERE id = p_slot_id;

    RETURN TRUE;
END;
$$ LANGUAGE plpgsql;

-- 2. Validar Stock Producto Físico
CREATE OR REPLACE FUNCTION tourism.fn_validar_stock_comercial(p_producto_id UUID)
RETURNS INT AS $$
DECLARE
    v_stock INT;
BEGIN
    SELECT (stock_actual - stock_reservado) INTO v_stock
    FROM tourism.artisan_inventory
    WHERE producto_id = p_producto_id;

    RETURN COALESCE(v_stock, 0);
END;
$$ LANGUAGE plpgsql;
