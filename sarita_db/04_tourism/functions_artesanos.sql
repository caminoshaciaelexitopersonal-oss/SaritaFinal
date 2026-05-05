-- Funciones Críticas: Artesanos

-- 3.1 Búsqueda Geográfica
CREATE OR REPLACE FUNCTION tourism.fn_buscar_artesanos_por_ubicacion(
    p_lat DOUBLE PRECISION,
    p_lon DOUBLE PRECISION,
    p_radio_metros INT
) RETURNS TABLE(artisan_id UUID, nombre TEXT, distancia_metros FLOAT) AS $$
BEGIN
    RETURN QUERY
    SELECT
        id,
        nombre_busqueda,
        ST_Distance(geo_point, ST_SetSRID(ST_MakePoint(p_lon, p_lat), 4326)::geography) as dist
    FROM tourism.artisan_directory_index
    WHERE ST_DWithin(geo_point, ST_SetSRID(ST_MakePoint(p_lon, p_lat), 4326)::geography, p_radio_metros)
    ORDER BY dist ASC;
END;
$$ LANGUAGE plpgsql;

-- 3.3 Disponibilidad de Producto
CREATE OR REPLACE FUNCTION tourism.fn_stock_disponible(p_producto_id UUID)
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
