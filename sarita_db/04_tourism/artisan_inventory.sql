-- Inventario de Artesanos
CREATE TABLE tourism.artisan_inventory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    producto_id UUID NOT NULL UNIQUE, -- O variant_id
    stock_actual INT DEFAULT 0,
    stock_reservado INT DEFAULT 0,
    stock_minimo INT DEFAULT 1,

    updated_at TIMESTAMP DEFAULT now()
);

-- Trigger: Validación de Stock
CREATE OR REPLACE FUNCTION tourism.fn_validate_artisan_stock()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.stock_actual < 0 THEN
        RAISE EXCEPTION 'Inventario Insuficiente: No se permite stock negativo en productos artesanales.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_artisan_stock BEFORE UPDATE ON tourism.artisan_inventory
FOR EACH ROW EXECUTE FUNCTION tourism.fn_validate_artisan_stock();
