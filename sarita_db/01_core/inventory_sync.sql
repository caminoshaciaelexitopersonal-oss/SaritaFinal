-- Triggers de Sincronización de Inventario

CREATE OR REPLACE FUNCTION tourism.fn_trg_update_stock_on_order()
RETURNS TRIGGER AS $$
BEGIN
    -- Al confirmar orden -> descontar stock real y liberar reserva
    IF NEW.status = 'confirmado' AND OLD.status = 'pendiente' THEN
        UPDATE tourism.artisan_inventory
        SET stock_actual = stock_actual - 1, -- Simplificado a 1 por item
            stock_reservado = stock_reservado - 1
        WHERE producto_id IN (SELECT producto_id FROM core.sales_order_items WHERE sales_order_id = NEW.id);

    -- Al cancelar -> devolver stock reservado
    ELSIF NEW.status = 'cancelado' AND OLD.status = 'pendiente' THEN
        UPDATE tourism.artisan_inventory
        SET stock_reservado = stock_reservado - 1
        WHERE producto_id IN (SELECT producto_id FROM core.sales_order_items WHERE sales_order_id = NEW.id);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_inventory_sync AFTER UPDATE ON core.sales_orders
FOR EACH ROW EXECUTE FUNCTION tourism.fn_trg_update_stock_on_order();
