CREATE OR REPLACE FUNCTION retry.classify_error(p_error TEXT)
RETURNS TEXT AS $$
BEGIN
    IF p_error LIKE '%timeout%' OR p_error LIKE '%connection%' OR p_error LIKE '%lock%' THEN
        RETURN 'transient';
    ELSE
        RETURN 'fatal';
    END IF;
END;
$$ LANGUAGE plpgsql;
