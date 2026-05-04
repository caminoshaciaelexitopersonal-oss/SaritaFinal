-- Relaciones transversales y restricciones globales - ERP COMPLETO

-- [CORE & IDENTITY]
ALTER TABLE identity.users ADD CONSTRAINT fk_users_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [ERP MI NEGOCIO 30-41]
-- Business Operations
ALTER TABLE core.business_operations ADD CONSTRAINT fk_op_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE core.business_operations ADD CONSTRAINT fk_op_customer FOREIGN KEY (cliente_id) REFERENCES core.customers(id);
ALTER TABLE core.business_operations ADD CONSTRAINT fk_op_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);

-- Commercial
ALTER TABLE core.opportunities ADD CONSTRAINT fk_opp_customer FOREIGN KEY (cliente_id) REFERENCES core.customers(id);
ALTER TABLE core.contracts ADD CONSTRAINT fk_con_customer FOREIGN KEY (cliente_id) REFERENCES core.customers(id);
ALTER TABLE core.contracts ADD CONSTRAINT fk_con_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);
ALTER TABLE core.sales_orders ADD CONSTRAINT fk_so_op FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);

-- Operational
ALTER TABLE core.tasks ADD CONSTRAINT fk_task_op FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);
ALTER TABLE core.tasks ADD CONSTRAINT fk_task_user FOREIGN KEY (responsable_id) REFERENCES identity.users(id);
ALTER TABLE core.incidents ADD CONSTRAINT fk_inc_op FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);
ALTER TABLE core.service_orders ADD CONSTRAINT fk_se_op FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);
ALTER TABLE core.resource_allocation ADD CONSTRAINT fk_res_se FOREIGN KEY (service_order_id) REFERENCES core.service_orders(id);

-- Archival
ALTER TABLE core.documents ADD CONSTRAINT fk_doc_op FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);
ALTER TABLE core.document_traces ADD CONSTRAINT fk_trace_doc FOREIGN KEY (document_id) REFERENCES core.documents(id);
ALTER TABLE core.document_traces ADD CONSTRAINT fk_trace_user FOREIGN KEY (usuario_id) REFERENCES identity.users(id);

-- Accounting
ALTER TABLE core.journal_entries ADD CONSTRAINT fk_je_op FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);
ALTER TABLE core.journal_lines ADD CONSTRAINT fk_jl_je FOREIGN KEY (journal_entry_id) REFERENCES core.journal_entries(id);
ALTER TABLE core.journal_lines ADD CONSTRAINT fk_jl_acc FOREIGN KEY (cuenta_id) REFERENCES erp_contable.puc_accounts(id);

-- Financial
ALTER TABLE core.payments_erp ADD CONSTRAINT fk_pay_op FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);

-- Billing
ALTER TABLE core.invoices ADD CONSTRAINT fk_inv_op FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);
ALTER TABLE core.invoice_lines ADD CONSTRAINT fk_il_inv FOREIGN KEY (invoice_id) REFERENCES core.invoices(id);
ALTER TABLE core.invoice_lines ADD CONSTRAINT fk_il_prod FOREIGN KEY (producto_id) REFERENCES core.products(id);

-- Costs
ALTER TABLE core.cost_structures ADD CONSTRAINT fk_cost_op FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);
