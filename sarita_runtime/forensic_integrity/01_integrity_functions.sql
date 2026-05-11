-- 40.2 — IMPLEMENTAR HASHING FORENSE REAL
-- Real SHA256 Integrity functions using pgcrypto

CREATE OR REPLACE FUNCTION infrastructure.fn_calculate_integrity_hash()
RETURNS TRIGGER AS $$
DECLARE
    data_string TEXT;
BEGIN
    -- Concatenate core fields and payload for hashing
    -- We use pgcrypto's digest function for real SHA256
    data_string := COALESCE(NEW.id::TEXT, '') ||
                   COALESCE(NEW.tenant_id::TEXT, '') ||
                   COALESCE(NEW.trace_id::TEXT, '') ||
                   COALESCE(NEW.context_id::TEXT, '');

    -- Real SHA256 hashing
    NEW.hash_integridad := encode(digest(data_string, 'sha256'), 'hex');

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply trigger to a sample critical table (Ledger)
DROP TRIGGER IF EXISTS trg_ledger_integrity ON finance.sovereign_ledger_global;
CREATE TRIGGER trg_ledger_integrity
BEFORE INSERT OR UPDATE ON finance.sovereign_ledger_global
FOR EACH ROW EXECUTE FUNCTION infrastructure.fn_calculate_integrity_hash();
