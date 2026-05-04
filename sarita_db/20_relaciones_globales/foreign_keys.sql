-- Relaciones transversales y restricciones globales - GESTIÓN CONTABLE REAL (FINAL)

-- [CATALOGOS]
ALTER TABLE accounting.accounts ADD CONSTRAINT fk_acc_coa FOREIGN KEY (chart_of_accounts_id) REFERENCES accounting.charts_of_accounts(id);
ALTER TABLE accounting.account_structure ADD CONSTRAINT fk_struct_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE accounting.account_types ADD CONSTRAINT fk_type_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [CONFIGURACION]
ALTER TABLE accounting.accounting_rules ADD CONSTRAINT fk_rule_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [MOVIMIENTOS]
ALTER TABLE accounting.journal_entries ADD CONSTRAINT fk_je_period FOREIGN KEY (period_id) REFERENCES accounting.fiscal_periods(id);
ALTER TABLE accounting.journal_entries ADD CONSTRAINT fk_je_user FOREIGN KEY (created_by) REFERENCES identity.users(id);
ALTER TABLE accounting.journal_entry_lines ADD CONSTRAINT fk_jel_je FOREIGN KEY (journal_entry_id) REFERENCES accounting.journal_entries(id);
ALTER TABLE accounting.journal_entry_lines ADD CONSTRAINT fk_jel_acc FOREIGN KEY (account_id) REFERENCES accounting.accounts(id);
ALTER TABLE accounting.transaction_links ADD CONSTRAINT fk_tl_je FOREIGN KEY (journal_entry_id) REFERENCES accounting.journal_entries(id);

-- [PERIODOS]
ALTER TABLE accounting.period_closures ADD CONSTRAINT fk_pc_period FOREIGN KEY (period_id) REFERENCES accounting.fiscal_periods(id);
ALTER TABLE accounting.period_closures ADD CONSTRAINT fk_pc_user FOREIGN KEY (closed_by) REFERENCES identity.users(id);

-- [IMPUESTOS]
ALTER TABLE accounting.tax_rates_contable ADD CONSTRAINT fk_tr_tax FOREIGN KEY (tax_id) REFERENCES accounting.taxes(id);
ALTER TABLE accounting.tax_rules_contable ADD CONSTRAINT fk_tru_tax FOREIGN KEY (tax_id) REFERENCES accounting.taxes(id);
ALTER TABLE accounting.tax_transactions ADD CONSTRAINT fk_tt_tax FOREIGN KEY (tax_id) REFERENCES accounting.taxes(id);

-- [CONCILIACIÓN]
ALTER TABLE accounting.bank_movements_erp ADD CONSTRAINT fk_bm_acc FOREIGN KEY (bank_account_id) REFERENCES accounting.bank_accounts_erp(id);
ALTER TABLE accounting.reconciliation_process ADD CONSTRAINT fk_rp_acc FOREIGN KEY (bank_account_id) REFERENCES accounting.bank_accounts_erp(id);
ALTER TABLE accounting.reconciliation_process ADD CONSTRAINT fk_rp_period FOREIGN KEY (period_id) REFERENCES accounting.fiscal_periods(id);

-- [ANALÍTICA]
ALTER TABLE accounting.cost_allocations ADD CONSTRAINT fk_ca_jel FOREIGN KEY (journal_line_id) REFERENCES accounting.journal_entry_lines(id);
ALTER TABLE accounting.cost_allocations ADD CONSTRAINT fk_ca_cc FOREIGN KEY (cost_center_id) REFERENCES accounting.cost_centers(id);

-- [AUDITORIA]
ALTER TABLE accounting.accounting_logs ADD CONSTRAINT fk_aal_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE accounting.accounting_logs ADD CONSTRAINT fk_aal_je FOREIGN KEY (reference_entry_id) REFERENCES accounting.journal_entries(id);
