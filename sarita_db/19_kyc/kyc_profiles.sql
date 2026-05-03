CREATE TABLE kyc.kyc_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    status VARCHAR(20) DEFAULT 'PENDING',
    risk_score INTEGER DEFAULT 0,
    verification_data JSONB DEFAULT '{}',
    expiry_date DATE, -- Hardening F10
    risk_recheck_required BOOLEAN DEFAULT false, -- Hardening F10
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

-- Auto-invalidación por expiración
CREATE OR REPLACE FUNCTION kyc.fn_auto_invalidate_kyc()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.expiry_date < CURRENT_DATE THEN
        NEW.status := 'EXPIRED';
        NEW.risk_recheck_required := true;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_kyc_expiry BEFORE INSERT OR UPDATE ON kyc.kyc_profiles FOR EACH ROW EXECUTE FUNCTION kyc.fn_auto_invalidate_kyc();
