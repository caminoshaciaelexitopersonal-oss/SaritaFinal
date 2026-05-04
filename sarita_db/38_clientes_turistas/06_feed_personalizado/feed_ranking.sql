-- Feed Inteligente: Ranking y Priorización
CREATE TABLE core.feed_ranking_rules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,

    content_type TEXT NOT NULL,
    weight_score DECIMAL(3,2) DEFAULT 1.00,

    min_reputation_required DECIMAL(3,2) DEFAULT 3.00,
    is_commercial_boost BOOLEAN DEFAULT false,

    updated_at TIMESTAMP DEFAULT now()
);

-- Overhaul de Función de Recomendación (Cerebro de Vía 3)
CREATE OR REPLACE FUNCTION core.fn_generar_recomendaciones_v3(p_user_id UUID)
RETURNS TABLE(content_id UUID, final_score FLOAT) AS $$
DECLARE
    v_user_pref JSONB;
    v_user_geo GEOGRAPHY;
BEGIN
    -- 1. Obtener contexto del usuario
    SELECT intereses INTO v_user_pref FROM tourism.tourist_preferences WHERE user_id = p_user_id;
    SELECT geo_point INTO v_user_geo FROM tourism.tourist_locations WHERE user_id = p_user_id;

    -- 2. Calcular Score Ponderado: proximidad (40%) + popularidad (20%) + afinidad (30%) + conversion (10%)
    RETURN QUERY
    SELECT
        di.artisan_id,
        (
            (1.0 - (ST_Distance(di.geo_point, v_user_geo) / 50000.0)) * 0.4 + -- Proximidad (normalizado a 50km)
            (di.rating_promedio / 5.0) * 0.2 +                               -- Popularidad
            (CASE WHEN v_user_pref->>di.categoria_nombre IS NOT NULL THEN 1.0 ELSE 0.5 END) * 0.3 + -- Afinidad
            (di.popularidad_score / 1000.0) * 0.1                            -- Conversión/Tráfico
        )::FLOAT as total_score
    FROM tourism.artisan_directory_index di
    WHERE di.rating_promedio >= 3.0 -- Reputación mínima
    ORDER BY total_score DESC
    LIMIT 20;
END;
$$ LANGUAGE plpgsql;
