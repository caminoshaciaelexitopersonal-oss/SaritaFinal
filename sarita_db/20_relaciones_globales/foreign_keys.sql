-- Relaciones transversales y restricciones globales - SARITA ERP & TRIPLE VÍA

-- [CORE & IDENTITY]
ALTER TABLE identity.users ADD CONSTRAINT fk_user_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [CRM & VENTAS]
ALTER TABLE crm.customer_profiles ADD CONSTRAINT fk_cp_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.leads_erp ADD CONSTRAINT fk_leads_assigned FOREIGN KEY (assigned_agent_id) REFERENCES identity.users(id);

-- [FINANZAS & CONTABILIDAD]
ALTER TABLE accounting.accounts ADD CONSTRAINT fk_acc_coa FOREIGN KEY (chart_of_accounts_id) REFERENCES accounting.charts_of_accounts(id);
ALTER TABLE accounting.journal_entries ADD CONSTRAINT fk_je_period FOREIGN KEY (period_id) REFERENCES accounting.fiscal_periods(id);
ALTER TABLE accounting.journal_entries ADD CONSTRAINT fk_je_creator FOREIGN KEY (created_by) REFERENCES identity.users(id);
ALTER TABLE accounting.journal_entry_lines ADD CONSTRAINT fk_jel_entry FOREIGN KEY (journal_entry_id) REFERENCES accounting.journal_entries(id);
ALTER TABLE accounting.journal_entry_lines ADD CONSTRAINT fk_jel_account FOREIGN KEY (account_id) REFERENCES accounting.accounts(id);

-- [OPERATIVA & PRESTADORES]
ALTER TABLE tourism.tourism_providers ADD CONSTRAINT fk_provider_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
-- ALTER TABLE tourism.provider_structure ADD CONSTRAINT fk_ps_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);

-- [LEDGER & WALLET]
ALTER TABLE ledger.ledger_entries ADD CONSTRAINT fk_le_trans FOREIGN KEY (transaction_id) REFERENCES ledger.transactions(id);
ALTER TABLE ledger.ledger_entries ADD CONSTRAINT fk_le_acc FOREIGN KEY (account_id) REFERENCES ledger.accounts(id);

-- [PAYMENTS]
ALTER TABLE payments.payment_intents ADD CONSTRAINT fk_pi_provider FOREIGN KEY (payment_provider_id) REFERENCES payments.payment_providers(id);

-- [VÍA 3 TOURIST V3 - 10.12]
ALTER TABLE identity.tourist_profiles ADD CONSTRAINT fk_tp_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE identity.tourist_realtime_location ADD CONSTRAINT fk_trl_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_location_history ADD CONSTRAINT fk_tlh_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_bookings ADD CONSTRAINT fk_tb_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_payments ADD CONSTRAINT fk_tpay_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_payments ADD CONSTRAINT fk_tpay_booking FOREIGN KEY (booking_id) REFERENCES identity.tourist_bookings(id);
ALTER TABLE identity.tourist_reviews ADD CONSTRAINT fk_tr_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_reviews ADD CONSTRAINT fk_tr_booking FOREIGN KEY (booking_id) REFERENCES identity.tourist_bookings(id);
ALTER TABLE identity.tourist_reputation ADD CONSTRAINT fk_trep_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_favorites ADD CONSTRAINT fk_tf_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_rewards ADD CONSTRAINT fk_trew_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_reward_history ADD CONSTRAINT fk_trh_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_security_checks ADD CONSTRAINT fk_tsc_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_security_checks ADD CONSTRAINT fk_tsc_booking FOREIGN KEY (booking_id) REFERENCES identity.tourist_bookings(id);
ALTER TABLE identity.tourist_feed_recommendations ADD CONSTRAINT fk_tfr_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_abandoned_carts ADD CONSTRAINT fk_tac_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);
ALTER TABLE identity.tourist_searches ADD CONSTRAINT fk_ts_tourist FOREIGN KEY (tourist_id) REFERENCES identity.tourist_profiles(id);

-- [SCTA AI CORE RELATIONS]
ALTER TABLE ai.agent_hierarchy ADD CONSTRAINT fk_ah_parent FOREIGN KEY (parent_agent_id) REFERENCES ai.agents_master(id);
ALTER TABLE ai.agent_hierarchy ADD CONSTRAINT fk_ah_child FOREIGN KEY (child_agent_id) REFERENCES ai.agents_master(id);
ALTER TABLE ai.agent_executions ADD CONSTRAINT fk_ae_agent FOREIGN KEY (agent_id) REFERENCES ai.agents_master(id);
ALTER TABLE ai.agent_executions ADD CONSTRAINT fk_ae_context FOREIGN KEY (context_id) REFERENCES ai.agent_context_universal(id);
ALTER TABLE ai.agent_actions ADD CONSTRAINT fk_aa_execution FOREIGN KEY (execution_id) REFERENCES ai.agent_executions(id);
ALTER TABLE ai.agent_memory_global ADD CONSTRAINT fk_amg_context FOREIGN KEY (context_id) REFERENCES ai.agent_context_universal(id);
ALTER TABLE ai.agent_memory_global ADD CONSTRAINT fk_amg_agent FOREIGN KEY (agent_id) REFERENCES ai.agents_master(id);
ALTER TABLE ai.agent_learning ADD CONSTRAINT fk_al_agent FOREIGN KEY (agent_id) REFERENCES ai.agents_master(id);
ALTER TABLE ai.agent_learning ADD CONSTRAINT fk_al_context FOREIGN KEY (context_id) REFERENCES ai.agent_context_universal(id);
ALTER TABLE ai.agent_decisions ADD CONSTRAINT fk_ad_agent FOREIGN KEY (agent_id) REFERENCES ai.agents_master(id);
ALTER TABLE ai.agent_decisions ADD CONSTRAINT fk_ad_context FOREIGN KEY (context_id) REFERENCES ai.agent_context_universal(id);
