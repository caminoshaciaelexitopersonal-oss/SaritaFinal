-- Relaciones transversales y restricciones globales

-- IDENTITY -> CORE
ALTER TABLE identity.users
    ADD CONSTRAINT fk_users_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id) ON DELETE CASCADE;

ALTER TABLE identity.roles
    ADD CONSTRAINT fk_roles_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id) ON DELETE CASCADE;

-- GOVERNANCE -> IDENTITY & CORE
ALTER TABLE governance.entities
    ADD CONSTRAINT fk_entities_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id) ON DELETE CASCADE;

ALTER TABLE governance.government_profiles
    ADD CONSTRAINT fk_gov_profiles_user FOREIGN KEY (user_id) REFERENCES identity.users(id) ON DELETE CASCADE;
ALTER TABLE governance.government_profiles
    ADD CONSTRAINT fk_gov_profiles_entity FOREIGN KEY (entity_id) REFERENCES governance.entities(id) ON DELETE CASCADE;
ALTER TABLE governance.government_profiles
    ADD CONSTRAINT fk_gov_profiles_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id) ON DELETE CASCADE;

-- AGENTS
ALTER TABLE agents.autonomous_agents
    ADD CONSTRAINT fk_agents_user FOREIGN KEY (user_id) REFERENCES identity.users(id) ON DELETE SET NULL;
ALTER TABLE agents.autonomous_agents
    ADD CONSTRAINT fk_agents_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id) ON DELETE CASCADE;

-- ERP OPERATIVO
ALTER TABLE erp_operativo.tourism_providers
    ADD CONSTRAINT fk_providers_owner FOREIGN KEY (owner_id) REFERENCES identity.users(id) ON DELETE CASCADE;
ALTER TABLE erp_operativo.tourism_providers
    ADD CONSTRAINT fk_providers_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id) ON DELETE CASCADE;

ALTER TABLE erp_operativo.tourism_services
    ADD CONSTRAINT fk_services_provider FOREIGN KEY (provider_id) REFERENCES erp_operativo.tourism_providers(id) ON DELETE CASCADE;
ALTER TABLE erp_operativo.tourism_services
    ADD CONSTRAINT fk_services_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id) ON DELETE CASCADE;

-- ERP CONTABLE
ALTER TABLE erp_contable.puc_accounts
    ADD CONSTRAINT fk_puc_parent FOREIGN KEY (parent_id) REFERENCES erp_contable.puc_accounts(id) ON DELETE SET NULL;
ALTER TABLE erp_contable.puc_accounts
    ADD CONSTRAINT fk_puc_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id) ON DELETE CASCADE;

-- WALLET
ALTER TABLE wallet.wallets
    ADD CONSTRAINT fk_wallets_owner FOREIGN KEY (owner_id) REFERENCES identity.users(id) ON DELETE CASCADE;
ALTER TABLE wallet.wallets
    ADD CONSTRAINT fk_wallets_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id) ON DELETE CASCADE;

-- DELIVERY
ALTER TABLE delivery.delivery_orders
    ADD CONSTRAINT fk_delivery_customer FOREIGN KEY (customer_id) REFERENCES identity.users(id) ON DELETE CASCADE;
ALTER TABLE delivery.delivery_orders
    ADD CONSTRAINT fk_delivery_provider FOREIGN KEY (provider_id) REFERENCES erp_operativo.tourism_providers(id) ON DELETE CASCADE;
ALTER TABLE delivery.delivery_orders
    ADD CONSTRAINT fk_delivery_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id) ON DELETE CASCADE;

-- INTEGRACIONES
ALTER TABLE integraciones.document_types
    ADD CONSTRAINT fk_doc_types_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id) ON DELETE CASCADE;
