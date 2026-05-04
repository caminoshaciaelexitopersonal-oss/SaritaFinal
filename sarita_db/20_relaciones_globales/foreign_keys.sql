-- Relaciones transversales y restricciones globales - CONECTORES TRANSACCIONALES

-- [WPC FUNNEL]
ALTER TABLE core.wpc_sessions ADD CONSTRAINT fk_wpc_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.wpc_intents ADD CONSTRAINT fk_wpc_sess FOREIGN KEY (session_id) REFERENCES core.wpc_sessions(id);

-- [COMERCIAL CONNECTORS]
ALTER TABLE core.sales_reservations ADD CONSTRAINT fk_sres_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.sales_reservations ADD CONSTRAINT fk_sres_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);
ALTER TABLE core.sales_orders ADD CONSTRAINT fk_sord_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.sales_orders ADD CONSTRAINT fk_sord_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);

-- [BOOKING CORE]
ALTER TABLE core.availability_slots ADD CONSTRAINT fk_aslot_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE core.booking_reservations_core ADD CONSTRAINT fk_bres_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.booking_reservations_core ADD CONSTRAINT fk_bres_slot FOREIGN KEY (slot_id) REFERENCES core.availability_slots(id);
