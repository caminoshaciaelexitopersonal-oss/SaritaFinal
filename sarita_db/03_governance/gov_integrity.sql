-- Test de Integridad Gubernamental
DO $$
DECLARE
    v_orphans INT;
BEGIN
    -- 1. Funcionarios sin Entidad o Cargo
    SELECT COUNT(*) INTO v_orphans FROM governance.public_officials
    WHERE entity_id IS NULL OR position_id IS NULL;
    IF v_orphans > 0 THEN RAISE EXCEPTION 'Integridad Fallida: Funcionarios huérfanos'; END IF;

    -- 2. Atractivos sin Municipio
    SELECT COUNT(*) INTO v_orphans FROM tourism.attractions
    WHERE municipality_id IS NULL;
    IF v_orphans > 0 THEN RAISE EXCEPTION 'Integridad Fallida: Atractivos sin municipio'; END IF;

    -- 3. Jerarquía Territorial (Todo municipio debe tener padre departamento)
    SELECT COUNT(*) INTO v_orphans FROM governance.territorial_entities
    WHERE type = 'municipio' AND parent_id IS NULL;
    IF v_orphans > 0 THEN RAISE EXCEPTION 'Integridad Fallida: Jerarquía territorial rota'; END IF;

    RAISE NOTICE 'Test Gobierno: PASSED';
END;
$$;
