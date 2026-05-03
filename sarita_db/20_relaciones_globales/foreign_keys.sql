-- Relaciones transversales y restricciones globales - FASE V1-GOV FINAL

-- [CORE & IDENTITY]
ALTER TABLE identity.users ADD CONSTRAINT fk_users_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE identity.roles ADD CONSTRAINT fk_roles_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [GOVERNANCE EXPANSIÓN]
ALTER TABLE governance.territorial_entities ADD CONSTRAINT fk_territorial_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE governance.territorial_entities ADD CONSTRAINT fk_territorial_parent FOREIGN KEY (parent_id) REFERENCES governance.territorial_entities(id);

ALTER TABLE governance.public_entities ADD CONSTRAINT fk_public_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE governance.public_entities ADD CONSTRAINT fk_public_territorial FOREIGN KEY (territorial_id) REFERENCES governance.territorial_entities(id);
ALTER TABLE governance.public_entities ADD CONSTRAINT fk_public_parent FOREIGN KEY (parent_entity_id) REFERENCES governance.public_entities(id);

ALTER TABLE governance.departments ADD CONSTRAINT fk_dept_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE governance.departments ADD CONSTRAINT fk_dept_entity FOREIGN KEY (entity_id) REFERENCES governance.public_entities(id);
ALTER TABLE governance.departments ADD CONSTRAINT fk_dept_parent FOREIGN KEY (parent_id) REFERENCES governance.departments(id);

ALTER TABLE governance.positions ADD CONSTRAINT fk_pos_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE governance.positions ADD CONSTRAINT fk_pos_dept FOREIGN KEY (department_id) REFERENCES governance.departments(id);

ALTER TABLE governance.public_officials ADD CONSTRAINT fk_official_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE governance.public_officials ADD CONSTRAINT fk_official_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE governance.public_officials ADD CONSTRAINT fk_official_entity FOREIGN KEY (entity_id) REFERENCES governance.public_entities(id);
ALTER TABLE governance.public_officials ADD CONSTRAINT fk_official_pos FOREIGN KEY (position_id) REFERENCES governance.positions(id);

ALTER TABLE governance.administrative_acts ADD CONSTRAINT fk_act_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE governance.administrative_acts ADD CONSTRAINT fk_act_entity FOREIGN KEY (entity_id) REFERENCES governance.public_entities(id);
ALTER TABLE governance.administrative_acts ADD CONSTRAINT fk_act_issuer FOREIGN KEY (issued_by) REFERENCES governance.public_officials(id);

-- [TOURISM EXPANSIÓN]
ALTER TABLE tourism.attractions ADD CONSTRAINT fk_attr_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.attractions ADD CONSTRAINT fk_attr_mun FOREIGN KEY (municipality_id) REFERENCES governance.territorial_entities(id);
ALTER TABLE tourism.attractions ADD CONSTRAINT fk_attr_resp FOREIGN KEY (responsible_entity_id) REFERENCES governance.public_entities(id);

ALTER TABLE tourism.events ADD CONSTRAINT fk_event_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.events ADD CONSTRAINT fk_event_org FOREIGN KEY (organizer_entity_id) REFERENCES governance.public_entities(id);
ALTER TABLE tourism.events ADD CONSTRAINT fk_event_attr FOREIGN KEY (related_attraction_id) REFERENCES tourism.attractions(id);

ALTER TABLE tourism.tourism_directory ADD CONSTRAINT fk_dir_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.tourism_directory ADD CONSTRAINT fk_dir_attr FOREIGN KEY (attraction_id) REFERENCES tourism.attractions(id);
ALTER TABLE tourism.tourism_directory ADD CONSTRAINT fk_dir_event FOREIGN KEY (event_id) REFERENCES tourism.events(id);

-- [AGENTS, ERP, WALLET, LEDGER...]
-- Se asume el bloque anterior se mantiene o se concatena en el deploy final.
