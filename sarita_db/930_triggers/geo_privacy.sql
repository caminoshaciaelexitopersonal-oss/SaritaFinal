-- Anonimización y Privacidad Geográfica Automática
CREATE OR REPLACE FUNCTION tourism.fn_apply_geo_privacy()
RETURNS VOID AS $$
BEGIN
    -- 1. Eliminar historial más viejo que la política
    DELETE FROM tourism.tourist_geo_history
    WHERE created_at < now() - (SELECT (retention_days || ' days')::interval FROM tourism.geo_retention_policies WHERE is_active LIMIT 1);

    -- 2. Reducir precisión (Anonymize) historial intermedio
    UPDATE tourism.tourist_geo_history
    SET geo_point = ST_SnapToGrid(geo_point::geometry, 0.01)::geography -- Reduce precisión a ~1km
    WHERE created_at < now() - (SELECT (anonymize_after_days || ' days')::interval FROM tourism.geo_retention_policies WHERE is_active LIMIT 1);
END;
$$ LANGUAGE plpgsql;
