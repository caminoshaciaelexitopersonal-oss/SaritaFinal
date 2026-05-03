-- Relaciones transversales y restricciones globales - FASE 10 FINAL (COMPLETO)

-- [CORE & IDENTITY]
ALTER TABLE identity.users ADD CONSTRAINT fk_users_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE identity.roles ADD CONSTRAINT fk_roles_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [GOVERNANCE]
ALTER TABLE governance.entities ADD CONSTRAINT fk_entities_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE governance.government_profiles ADD CONSTRAINT fk_gov_profiles_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE governance.government_profiles ADD CONSTRAINT fk_gov_profiles_entity FOREIGN KEY (entity_id) REFERENCES governance.entities(id);
ALTER TABLE governance.government_profiles ADD CONSTRAINT fk_gov_profiles_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [AGENTS]
ALTER TABLE agents.autonomous_agents ADD CONSTRAINT fk_agents_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE agents.autonomous_agents ADD CONSTRAINT fk_agents_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [ERP OPERATIVO]
ALTER TABLE erp_operativo.tourism_providers ADD CONSTRAINT fk_providers_owner FOREIGN KEY (owner_id) REFERENCES identity.users(id);
ALTER TABLE erp_operativo.tourism_providers ADD CONSTRAINT fk_providers_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE erp_operativo.tourism_services ADD CONSTRAINT fk_services_provider FOREIGN KEY (provider_id) REFERENCES erp_operativo.tourism_providers(id);
ALTER TABLE erp_operativo.tourism_services ADD CONSTRAINT fk_services_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [ERP CONTABLE]
ALTER TABLE erp_contable.puc_accounts ADD CONSTRAINT fk_puc_parent FOREIGN KEY (parent_id) REFERENCES erp_contable.puc_accounts(id);
ALTER TABLE erp_contable.puc_accounts ADD CONSTRAINT fk_puc_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [WALLET & LEDGER]
ALTER TABLE wallet.wallets ADD CONSTRAINT fk_wallets_owner FOREIGN KEY (owner_id) REFERENCES identity.users(id);
ALTER TABLE wallet.wallets ADD CONSTRAINT fk_wallets_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE ledger.accounts ADD CONSTRAINT fk_ledger_accounts_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE ledger.transactions ADD CONSTRAINT fk_ledger_trans_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE ledger.ledger_entries ADD CONSTRAINT fk_ledger_entries_trans FOREIGN KEY (transaction_id) REFERENCES ledger.transactions(id);
ALTER TABLE ledger.ledger_entries ADD CONSTRAINT fk_ledger_entries_acc FOREIGN KEY (account_id) REFERENCES ledger.accounts(id);
ALTER TABLE ledger.ledger_entries ADD CONSTRAINT fk_ledger_entries_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE ledger.transaction_lines ADD CONSTRAINT fk_ledger_lines_trans FOREIGN KEY (transaction_id) REFERENCES ledger.transactions(id);
ALTER TABLE ledger.transaction_lines ADD CONSTRAINT fk_ledger_lines_acc FOREIGN KEY (account_id) REFERENCES ledger.accounts(id);
ALTER TABLE ledger.transaction_lines ADD CONSTRAINT fk_ledger_lines_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [DELIVERY]
ALTER TABLE delivery.delivery_orders ADD CONSTRAINT fk_delivery_customer FOREIGN KEY (customer_id) REFERENCES identity.users(id);
ALTER TABLE delivery.delivery_orders ADD CONSTRAINT fk_delivery_provider FOREIGN KEY (provider_id) REFERENCES erp_operativo.tourism_providers(id);
ALTER TABLE delivery.delivery_orders ADD CONSTRAINT fk_delivery_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [PAYMENTS]
ALTER TABLE payments.payment_providers ADD CONSTRAINT fk_pay_prov_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE payments.payment_intents ADD CONSTRAINT fk_pay_int_prov FOREIGN KEY (provider_id) REFERENCES payments.payment_providers(id);
ALTER TABLE payments.payment_intents ADD CONSTRAINT fk_pay_int_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE payments.payment_attempts ADD CONSTRAINT fk_pay_att_int FOREIGN KEY (payment_intent_id) REFERENCES payments.payment_intents(id);
ALTER TABLE payments.payment_attempts ADD CONSTRAINT fk_pay_att_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE payments.payment_webhooks ADD CONSTRAINT fk_pay_web_prov FOREIGN KEY (provider_id) REFERENCES payments.payment_providers(id);
ALTER TABLE payments.payment_webhooks ADD CONSTRAINT fk_pay_web_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE payments.payment_settlements ADD CONSTRAINT fk_pay_set_int FOREIGN KEY (payment_intent_id) REFERENCES payments.payment_intents(id);
ALTER TABLE payments.payment_settlements ADD CONSTRAINT fk_pay_set_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [KYC]
ALTER TABLE kyc.kyc_profiles ADD CONSTRAINT fk_kyc_prof_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE kyc.kyc_profiles ADD CONSTRAINT fk_kyc_prof_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE kyc.kyc_documents ADD CONSTRAINT fk_kyc_doc_prof FOREIGN KEY (kyc_profile_id) REFERENCES kyc.kyc_profiles(id);
ALTER TABLE kyc.kyc_documents ADD CONSTRAINT fk_kyc_doc_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE kyc.kyc_verifications ADD CONSTRAINT fk_kyc_ver_prof FOREIGN KEY (kyc_profile_id) REFERENCES kyc.kyc_profiles(id);
ALTER TABLE kyc.kyc_verifications ADD CONSTRAINT fk_kyc_ver_user FOREIGN KEY (verifier_id) REFERENCES identity.users(id);
ALTER TABLE kyc.kyc_verifications ADD CONSTRAINT fk_kyc_ver_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE kyc.kyc_risk_scores ADD CONSTRAINT fk_kyc_risk_prof FOREIGN KEY (kyc_profile_id) REFERENCES kyc.kyc_profiles(id);
ALTER TABLE kyc.kyc_risk_scores ADD CONSTRAINT fk_kyc_risk_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [TAX]
ALTER TABLE tax.tax_jurisdictions ADD CONSTRAINT fk_tax_jur_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tax.tax_rules ADD CONSTRAINT fk_tax_rules_jur FOREIGN KEY (jurisdiction_id) REFERENCES tax.tax_jurisdictions(id);
ALTER TABLE tax.tax_rules ADD CONSTRAINT fk_tax_rules_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tax.tax_rates ADD CONSTRAINT fk_tax_rates_rule FOREIGN KEY (rule_id) REFERENCES tax.tax_rules(id);
ALTER TABLE tax.tax_rates ADD CONSTRAINT fk_tax_rates_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tax.tax_applications ADD CONSTRAINT fk_tax_app_rule FOREIGN KEY (tax_rule_id) REFERENCES tax.tax_rules(id);
ALTER TABLE tax.tax_applications ADD CONSTRAINT fk_tax_app_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [RECONCILIATION]
ALTER TABLE reconciliation.bank_accounts ADD CONSTRAINT fk_bank_acc_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE reconciliation.bank_movements ADD CONSTRAINT fk_bank_mov_acc FOREIGN KEY (bank_account_id) REFERENCES reconciliation.bank_accounts(id);
ALTER TABLE reconciliation.bank_movements ADD CONSTRAINT fk_bank_mov_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE reconciliation.reconciliation_jobs ADD CONSTRAINT fk_recon_job_acc FOREIGN KEY (bank_account_id) REFERENCES reconciliation.bank_accounts(id);
ALTER TABLE reconciliation.reconciliation_jobs ADD CONSTRAINT fk_recon_job_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE reconciliation.matches ADD CONSTRAINT fk_match_mov FOREIGN KEY (movement_id) REFERENCES reconciliation.bank_movements(id);
ALTER TABLE reconciliation.matches ADD CONSTRAINT fk_match_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [ARCHIVAL]
ALTER TABLE archival.document_signatures ADD CONSTRAINT fk_doc_sig_signer FOREIGN KEY (signer_id) REFERENCES identity.users(id);
ALTER TABLE archival.document_signatures ADD CONSTRAINT fk_doc_sig_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE archival.retention_policies ADD CONSTRAINT fk_ret_pol_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE archival.document_notarizations ADD CONSTRAINT fk_doc_not_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE archival.document_chain ADD CONSTRAINT fk_doc_chain_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [INTEGRACIONES]
ALTER TABLE integraciones.document_types ADD CONSTRAINT fk_doc_types_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [EVENTS]
ALTER TABLE events.event_store ADD CONSTRAINT fk_events_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE events.event_streams ADD CONSTRAINT fk_streams_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE events.event_snapshots ADD CONSTRAINT fk_snapshots_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
