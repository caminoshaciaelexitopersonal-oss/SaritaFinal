-- Row Level Security (RLS) Estandarizado - GESTIÓN FINANCIERA

-- Aplicar aislamiento por tenant_id a todos los nuevos módulos financieros (esquema core)
DO $$
DECLARE
    t text;
    s text := 'core';
BEGIN
    FOR t IN
        VALUES ('cash_accounts', 'cash_movements', 'cash_transfers', 'budgets', 'budget_lines', 'budget_versions',
                'cash_flow_projections', 'cash_flow_actuals', 'cash_flow_gaps', 'loans', 'loan_payments', 'credit_lines',
                'investments', 'investment_returns', 'investment_movements', 'financial_expenses', 'expense_receipts',
                'expense_policies', 'financial_kpis', 'kpi_calculations', 'financial_snapshots', 'financial_groups',
                'group_entities', 'consolidated_reports')
    LOOP
        -- Habilitar RLS
        EXECUTE format('ALTER TABLE %I.%I ENABLE ROW LEVEL SECURITY;', s, t);

        -- Política obligatoria usando app.current_tenant
        EXECUTE format('DROP POLICY IF EXISTS tenant_isolation_policy ON %I.%I;', s, t);
        EXECUTE format('CREATE POLICY tenant_isolation_policy ON %I.%I USING (tenant_id = current_setting(''app.current_tenant'', true)::UUID);', s, t);
    END LOOP;
END;
$$;
