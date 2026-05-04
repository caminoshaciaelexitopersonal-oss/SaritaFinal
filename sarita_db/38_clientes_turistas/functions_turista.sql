-- Funciones Avanzadas del Turista

-- 3.1 Perfil Dinámico
CREATE OR REPLACE FUNCTION core.fn_perfil_dinamico_usuario(p_user_id UUID)
RETURNS JSONB AS $$
DECLARE
    v_profile JSONB;
    v_preferences JSONB;
    v_orders_count INT;
BEGIN
    SELECT to_jsonb(p) INTO v_profile FROM tourism.tourist_profiles p WHERE user_id = p_user_id;
    SELECT intereses INTO v_preferences FROM tourism.tourist_preferences WHERE user_id = p_user_id;
    SELECT COUNT(*) INTO v_orders_count FROM core.tourist_orders WHERE user_id = p_user_id;

    RETURN jsonb_build_object(
        'profile', v_profile,
        'preferences', v_preferences,
        'activity_level', v_orders_count
    );
END;
$$ LANGUAGE plpgsql;

-- 3.3 Búsqueda Geográfica de Usuario
CREATE OR REPLACE FUNCTION core.fn_busqueda_geo_usuario(p_user_id UUID, p_radio_metros INT)
RETURNS TABLE(atractivo_id UUID, nombre TEXT, distancia FLOAT) AS $$
DECLARE
    v_user_geo GEOGRAPHY;
BEGIN
    SELECT geo_point INTO v_user_geo FROM tourism.tourist_locations WHERE user_id = p_user_id;

    RETURN QUERY
    SELECT id, name, ST_Distance(location, v_user_geo) as dist
    FROM tourism.attractions
    WHERE ST_DWithin(location, v_user_geo, p_radio_metros)
    ORDER BY dist ASC;
END;
$$ LANGUAGE plpgsql;
