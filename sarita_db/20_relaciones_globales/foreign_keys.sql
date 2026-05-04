-- Relaciones transversales y restricciones globales - GESTIÓN COMERCIAL OMNICANAL

-- [CRM]
ALTER TABLE core.customer_profiles ADD CONSTRAINT fk_cp_customer FOREIGN KEY (customer_id) REFERENCES core.customers(id);
ALTER TABLE core.leads_erp ADD CONSTRAINT fk_lead_agent FOREIGN KEY (assigned_agent_id) REFERENCES identity.users(id);
ALTER TABLE core.lead_scoring ADD CONSTRAINT fk_ls_lead FOREIGN KEY (lead_id) REFERENCES core.leads_erp(id);
ALTER TABLE core.crm_interactions ADD CONSTRAINT fk_inter_customer FOREIGN KEY (customer_id) REFERENCES core.customers(id);
ALTER TABLE core.crm_interactions ADD CONSTRAINT fk_inter_lead FOREIGN KEY (lead_id) REFERENCES core.leads_erp(id);
ALTER TABLE core.customer_channels ADD CONSTRAINT fk_chan_customer FOREIGN KEY (customer_id) REFERENCES core.customers(id);

-- [VENTAS]
ALTER TABLE core.sales_order_items ADD CONSTRAINT fk_soi_order FOREIGN KEY (sales_order_id) REFERENCES core.business_operations(id);
ALTER TABLE core.sales_order_items ADD CONSTRAINT fk_soi_product FOREIGN KEY (product_id) REFERENCES core.products(id);
ALTER TABLE core.quotes ADD CONSTRAINT fk_quote_customer FOREIGN KEY (customer_id) REFERENCES core.customers(id);
ALTER TABLE core.funnel_steps ADD CONSTRAINT fk_fs_funnel FOREIGN KEY (funnel_id) REFERENCES core.sales_funnels(id);
ALTER TABLE core.funnel_tracking ADD CONSTRAINT fk_ft_lead FOREIGN KEY (lead_id) REFERENCES core.leads_erp(id);
ALTER TABLE core.funnel_tracking ADD CONSTRAINT fk_ft_step FOREIGN KEY (funnel_step_id) REFERENCES core.funnel_steps(id);
ALTER TABLE core.omnichannel_conversion ADD CONSTRAINT fk_oc_campaign FOREIGN KEY (campaign_id) REFERENCES core.marketing_campaigns(id);
ALTER TABLE core.omnichannel_conversion ADD CONSTRAINT fk_oc_product FOREIGN KEY (product_id) REFERENCES core.products(id);

-- [MARKETING]
ALTER TABLE core.campaign_channels ADD CONSTRAINT fk_cc_campaign FOREIGN KEY (campaign_id) REFERENCES core.marketing_campaigns(id);
ALTER TABLE core.campaign_metrics ADD CONSTRAINT fk_cm_campaign FOREIGN KEY (campaign_id) REFERENCES core.marketing_campaigns(id);
ALTER TABLE core.content_campaign_links ADD CONSTRAINT fk_ccl_campaign FOREIGN KEY (campaign_id) REFERENCES core.marketing_campaigns(id);
ALTER TABLE core.content_campaign_links ADD CONSTRAINT fk_ccl_asset FOREIGN KEY (asset_id) REFERENCES core.media_assets(id);

-- [MULTIMEDIA]
ALTER TABLE core.video_projects ADD CONSTRAINT fk_vp_product FOREIGN KEY (product_id) REFERENCES core.products(id);
ALTER TABLE core.video_scenes ADD CONSTRAINT fk_vs_project FOREIGN KEY (project_id) REFERENCES core.video_projects(id);
ALTER TABLE core.video_scenes ADD CONSTRAINT fk_vs_asset FOREIGN KEY (asset_id) REFERENCES core.media_assets(id);
ALTER TABLE core.video_edits ADD CONSTRAINT fk_ve_project FOREIGN KEY (project_id) REFERENCES core.video_projects(id);
ALTER TABLE core.video_edits ADD CONSTRAINT fk_ve_author FOREIGN KEY (author_id) REFERENCES identity.users(id);
ALTER TABLE core.video_renders ADD CONSTRAINT fk_vr_project FOREIGN KEY (project_id) REFERENCES core.video_projects(id);
ALTER TABLE core.media_storage_metadata ADD CONSTRAINT fk_msm_asset FOREIGN KEY (asset_id) REFERENCES core.media_assets(id);

-- [SOCIAL MEDIA]
ALTER TABLE core.social_accounts ADD CONSTRAINT fk_sa_platform FOREIGN KEY (platform_id) REFERENCES core.social_platforms(id);
ALTER TABLE core.social_posts ADD CONSTRAINT fk_sp_account FOREIGN KEY (account_id) REFERENCES core.social_accounts(id);
ALTER TABLE core.social_posts ADD CONSTRAINT fk_sp_asset FOREIGN KEY (asset_id) REFERENCES core.media_assets(id);
ALTER TABLE core.social_posts ADD CONSTRAINT fk_sp_product FOREIGN KEY (product_id) REFERENCES core.products(id);
ALTER TABLE core.social_post_queue ADD CONSTRAINT fk_spq_account FOREIGN KEY (account_id) REFERENCES core.social_accounts(id);
ALTER TABLE core.social_post_queue ADD CONSTRAINT fk_spq_post FOREIGN KEY (post_id) REFERENCES core.social_posts(id);
ALTER TABLE core.social_post_metrics ADD CONSTRAINT fk_spm_post FOREIGN KEY (post_id) REFERENCES core.social_posts(id);
ALTER TABLE core.social_conversations ADD CONSTRAINT fk_scon_account FOREIGN KEY (account_id) REFERENCES core.social_accounts(id);
ALTER TABLE core.social_conversations ADD CONSTRAINT fk_scon_customer FOREIGN KEY (customer_id) REFERENCES core.customers(id);
ALTER TABLE core.social_messages ADD CONSTRAINT fk_sm_convo FOREIGN KEY (conversation_id) REFERENCES core.social_conversations(id);

-- [AUTOMATIZACIÓN]
ALTER TABLE core.automation_triggers ADD CONSTRAINT fk_at_rule FOREIGN KEY (rule_id) REFERENCES core.automation_rules(id);
ALTER TABLE core.automation_actions ADD CONSTRAINT fk_aa_rule FOREIGN KEY (rule_id) REFERENCES core.automation_rules(id);
ALTER TABLE core.automation_execution_logs ADD CONSTRAINT fk_ael_rule FOREIGN KEY (rule_id) REFERENCES core.automation_rules(id);
ALTER TABLE core.automation_failures ADD CONSTRAINT fk_af_exec FOREIGN KEY (execution_id) REFERENCES core.automation_execution_logs(id);

-- [IA CONVERSACIONAL]
ALTER TABLE core.ai_chat_sessions ADD CONSTRAINT fk_ais_customer FOREIGN KEY (customer_id) REFERENCES core.customers(id);
ALTER TABLE core.ai_chat_sessions ADD CONSTRAINT fk_ais_lead FOREIGN KEY (lead_id) REFERENCES core.leads_erp(id);
ALTER TABLE core.ai_chat_messages ADD CONSTRAINT fk_aim_session FOREIGN KEY (session_id) REFERENCES core.ai_chat_sessions(id);
ALTER TABLE core.ai_response_templates ADD CONSTRAINT fk_air_intent FOREIGN KEY (intent_id) REFERENCES core.ai_intents_registry(id);
ALTER TABLE core.ai_sales_actions ADD CONSTRAINT fk_aisa_session FOREIGN KEY (session_id) REFERENCES core.ai_chat_sessions(id);
ALTER TABLE core.ai_sales_actions ADD CONSTRAINT fk_aisa_product FOREIGN KEY (product_id) REFERENCES core.products(id);
ALTER TABLE core.ai_sales_actions ADD CONSTRAINT fk_aisa_order FOREIGN KEY (order_id) REFERENCES core.business_operations(id);
ALTER TABLE core.ai_lead_generation ADD CONSTRAINT fk_ailg_session FOREIGN KEY (session_id) REFERENCES core.ai_chat_sessions(id);
ALTER TABLE core.ai_lead_generation ADD CONSTRAINT fk_ailg_lead FOREIGN KEY (lead_id) REFERENCES core.leads_erp(id);
ALTER TABLE core.ai_conversion_events ADD CONSTRAINT fk_aice_session FOREIGN KEY (session_id) REFERENCES core.ai_chat_sessions(id);
ALTER TABLE core.ai_conversion_events ADD CONSTRAINT fk_aice_order FOREIGN KEY (order_id) REFERENCES core.business_operations(id);
