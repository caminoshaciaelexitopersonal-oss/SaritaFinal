-- Relaciones transversales y restricciones globales - SARITA ERP & TRIPLE VÍA

-- [CORE & IDENTITY]
ALTER TABLE identity.users ADD CONSTRAINT fk_user_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [CRM & VENTAS]
ALTER TABLE crm.customer_profiles ADD CONSTRAINT fk_cp_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE crm.leads ADD CONSTRAINT fk_leads_assigned FOREIGN KEY (assigned_to) REFERENCES identity.users(id);

-- [FINANZAS & CONTABILIDAD]
ALTER TABLE accounting.accounts ADD CONSTRAINT fk_acc_coa FOREIGN KEY (chart_of_accounts_id) REFERENCES accounting.charts_of_accounts(id);
ALTER TABLE accounting.journal_entries ADD CONSTRAINT fk_je_period FOREIGN KEY (period_id) REFERENCES accounting.periods(id);
ALTER TABLE accounting.journal_entries ADD CONSTRAINT fk_je_creator FOREIGN KEY (created_by) REFERENCES identity.users(id);
ALTER TABLE accounting.journal_entry_lines ADD CONSTRAINT fk_jel_entry FOREIGN KEY (journal_entry_id) REFERENCES accounting.journal_entries(id);
ALTER TABLE accounting.journal_entry_lines ADD CONSTRAINT fk_jel_account FOREIGN KEY (account_id) REFERENCES accounting.accounts(id);

-- [OPERATIVA & PRESTADORES]
ALTER TABLE turismo.tourism_providers ADD CONSTRAINT fk_provider_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE turismo.provider_structure ADD CONSTRAINT fk_ps_provider FOREIGN KEY (provider_id) REFERENCES turismo.tourism_providers(id);

-- [PRODUCTOS & SERVICIOS]
ALTER TABLE erp_operativo.tourism_services ADD CONSTRAINT fk_ts_provider FOREIGN KEY (provider_id) REFERENCES turismo.tourism_providers(id);

-- [LEDGER & WALLET]
ALTER TABLE ledger.ledger_entries ADD CONSTRAINT fk_le_trans FOREIGN KEY (transaction_id) REFERENCES ledger.transactions(id);
ALTER TABLE ledger.ledger_entries ADD CONSTRAINT fk_le_acc FOREIGN KEY (account_id) REFERENCES ledger.accounts(id);

-- [PAYMENTS]
ALTER TABLE payments.payment_intents ADD CONSTRAINT fk_pi_provider FOREIGN KEY (payment_provider_id) REFERENCES payments.payment_providers(id);

-- [HISTORIAL & TRANSACCIONES VÍA 3]
ALTER TABLE core.tourist_transaction_refs ADD CONSTRAINT fk_ttr_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.tourist_transaction_refs ADD CONSTRAINT fk_ttr_trans FOREIGN KEY (transaction_id) REFERENCES ledger.transactions(id);
-- Comentado si core.bookings_erp no existe aún o tiene otro nombre
-- ALTER TABLE core.tourist_transaction_refs ADD CONSTRAINT fk_ttr_book FOREIGN KEY (booking_id) REFERENCES core.bookings_erp(id);

-- [REPUTACION & FRAUDE VÍA 3]
ALTER TABLE core.fraud_detection_logs ADD CONSTRAINT fk_fdl_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

-- [PRIVACIDAD VÍA 3]
ALTER TABLE tourism.tourist_geo_consent ADD CONSTRAINT fk_tgc_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

-- [TIMELINE VÍA 3]
ALTER TABLE core.tourist_activity_timeline ADD CONSTRAINT fk_tat_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

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
