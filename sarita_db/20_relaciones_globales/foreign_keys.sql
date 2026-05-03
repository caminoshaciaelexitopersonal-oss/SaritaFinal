-- Relaciones transversales y restricciones globales - FASE VÍA 2 COMPLETA

-- [CORE & IDENTITY]
ALTER TABLE identity.users ADD CONSTRAINT fk_users_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [GUBERNAMENTAL V1]
-- [Mantener anteriores...]

-- [PRESTADORES V2]
-- Core Providers
ALTER TABLE tourism.tourism_providers ADD CONSTRAINT fk_providers_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

ALTER TABLE tourism.provider_structure ADD CONSTRAINT fk_struct_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.provider_structure ADD CONSTRAINT fk_struct_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);
ALTER TABLE tourism.provider_structure ADD CONSTRAINT fk_struct_parent FOREIGN KEY (parent_provider_id) REFERENCES tourism.tourism_providers(id);

ALTER TABLE tourism.provider_wallet ADD CONSTRAINT fk_pwallet_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.provider_wallet ADD CONSTRAINT fk_pwallet_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);
ALTER TABLE tourism.provider_wallet ADD CONSTRAINT fk_pwallet_wallet FOREIGN KEY (wallet_id) REFERENCES wallet.wallets(id);

-- Roles Empresariales
ALTER TABLE tourism.provider_roles ADD CONSTRAINT fk_proles_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.provider_roles ADD CONSTRAINT fk_proles_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);
ALTER TABLE tourism.provider_roles ADD CONSTRAINT fk_proles_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

-- Compliance
ALTER TABLE tourism.provider_licenses ADD CONSTRAINT fk_lic_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.provider_licenses ADD CONSTRAINT fk_lic_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);

ALTER TABLE tourism.provider_certifications ADD CONSTRAINT fk_cert_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.provider_certifications ADD CONSTRAINT fk_cert_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);

-- Directorio
ALTER TABLE tourism.provider_directory ADD CONSTRAINT fk_dir_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.provider_directory ADD CONSTRAINT fk_dir_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);

-- Reputación
ALTER TABLE tourism.provider_reviews ADD CONSTRAINT fk_rev_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.provider_reviews ADD CONSTRAINT fk_rev_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);
ALTER TABLE tourism.provider_reviews ADD CONSTRAINT fk_rev_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

ALTER TABLE tourism.provider_reputation_score ADD CONSTRAINT fk_score_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.provider_reputation_score ADD CONSTRAINT fk_score_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);

-- Eventos y Capacidad
ALTER TABLE tourism.provider_events ADD CONSTRAINT fk_pevent_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.provider_events ADD CONSTRAINT fk_pevent_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);

ALTER TABLE tourism.provider_capacity ADD CONSTRAINT fk_cap_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.provider_capacity ADD CONSTRAINT fk_cap_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);
