-- Workflow Funcional de KYC y Cumplimiento
CREATE TABLE kyc.kyc_workflows (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    kyc_profile_id UUID NOT NULL,
    current_step VARCHAR(50),
    status VARCHAR(20) DEFAULT 'pending', -- pending, in_review, approved, rejected
    assigned_to UUID,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

-- Trigger de bloqueo por KYC
CREATE OR REPLACE FUNCTION kyc.fn_enforce_kyc_compliance()
RETURNS TRIGGER AS $$
DECLARE
    v_status VARCHAR(20);
BEGIN
    SELECT status INTO v_status FROM kyc.kyc_profiles WHERE user_id = NEW.tenant_id OR user_id = (SELECT owner_id FROM core.tenants WHERE id = NEW.tenant_id);

    IF v_status IS NULL OR v_status != 'approved' THEN
        RAISE EXCEPTION 'CUMPLIMIENTO: Operación Financiera bloqueada por falta de KYC aprobado.';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar bloqueo a creación de wallets y transacciones grandes
-- CREATE TRIGGER trg_enforce_kyc_ledger BEFORE INSERT ON ledger.ledger_entries FOR EACH ROW EXECUTE FUNCTION kyc.fn_enforce_kyc_compliance();
