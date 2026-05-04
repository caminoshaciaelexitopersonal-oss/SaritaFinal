CREATE OR REPLACE FUNCTION core.apply_schema_version(
    p_version TEXT,
    p_checksum TEXT
)
RETURNS VOID AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM core.schema_versions WHERE version = p_version
    ) THEN
        RAISE EXCEPTION 'Version already applied: %', p_version;
    END IF;

    INSERT INTO core.schema_versions (version, checksum, executed_by)
    VALUES (p_version, p_checksum, current_user);
END;
$$ LANGUAGE plpgsql;
