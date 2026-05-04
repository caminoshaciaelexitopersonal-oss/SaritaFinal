-- Relaciones transversales y restricciones globales - GESTIÓN FINANCIERA

-- [TESORERIA]
ALTER TABLE core.cash_movements ADD CONSTRAINT fk_cmov_acc FOREIGN KEY (cash_account_id) REFERENCES core.cash_accounts(id);
ALTER TABLE core.cash_transfers ADD CONSTRAINT fk_ctra_source FOREIGN KEY (source_account_id) REFERENCES core.cash_accounts(id);
ALTER TABLE core.cash_transfers ADD CONSTRAINT fk_ctra_dest FOREIGN KEY (destination_account_id) REFERENCES core.cash_accounts(id);

-- [PRESUPUESTOS]
ALTER TABLE core.budget_lines ADD CONSTRAINT fk_bl_budget FOREIGN KEY (budget_id) REFERENCES core.budgets(id);
ALTER TABLE core.budget_versions ADD CONSTRAINT fk_bv_budget FOREIGN KEY (budget_id) REFERENCES core.budgets(id);
ALTER TABLE core.budget_versions ADD CONSTRAINT fk_bv_user FOREIGN KEY (approved_by) REFERENCES identity.users(id);

-- [FINANCIAMIENTO]
ALTER TABLE core.loan_payments ADD CONSTRAINT fk_lp_loan FOREIGN KEY (loan_id) REFERENCES core.loans(id);

-- [INVERSIONES]
ALTER TABLE core.investment_returns ADD CONSTRAINT fk_ir_inv FOREIGN KEY (investment_id) REFERENCES core.investments(id);
ALTER TABLE core.investment_movements ADD CONSTRAINT fk_imov_inv FOREIGN KEY (investment_id) REFERENCES core.investments(id);

-- [GASTOS]
ALTER TABLE core.expense_receipts ADD CONSTRAINT fk_er_expense FOREIGN KEY (expense_id) REFERENCES core.financial_expenses(id);

-- [INDICADORES]
ALTER TABLE core.kpi_calculations ADD CONSTRAINT fk_kcalc_kpi FOREIGN KEY (kpi_id) REFERENCES core.financial_kpis(id);

-- [CONSOLIDACION]
ALTER TABLE core.group_entities ADD CONSTRAINT fk_ge_group FOREIGN KEY (group_id) REFERENCES core.financial_groups(id);
ALTER TABLE core.consolidated_reports ADD CONSTRAINT fk_crep_group FOREIGN KEY (group_id) REFERENCES core.financial_groups(id);
