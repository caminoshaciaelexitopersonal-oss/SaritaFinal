-- Relaciones transversales y restricciones globales - GESTIÓN OPERATIVA TOTAL

-- [CORE OPERATIVO]
ALTER TABLE core.operational_units ADD CONSTRAINT fk_unit_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);
ALTER TABLE core.service_catalog_extended ADD CONSTRAINT fk_cat_provider FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);

-- [ÓRDENES DE SERVICIO]
ALTER TABLE core.service_orders_erp ADD CONSTRAINT fk_so_operation FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);
ALTER TABLE core.service_order_items_erp ADD CONSTRAINT fk_soi_so FOREIGN KEY (service_order_id) REFERENCES core.service_orders_erp(id);
ALTER TABLE core.service_order_items_erp ADD CONSTRAINT fk_soi_prod FOREIGN KEY (product_id) REFERENCES core.products(id);
ALTER TABLE core.service_execution_logs ADD CONSTRAINT fk_sel_so FOREIGN KEY (service_order_id) REFERENCES core.service_orders_erp(id);
ALTER TABLE core.service_execution_logs ADD CONSTRAINT fk_sel_user FOREIGN KEY (actor_id) REFERENCES identity.users(id);

-- [TAREAS]
ALTER TABLE core.operational_tasks ADD CONSTRAINT fk_task_so FOREIGN KEY (service_order_id) REFERENCES core.service_orders_erp(id);
ALTER TABLE core.task_assignments ADD CONSTRAINT fk_ta_task FOREIGN KEY (task_id) REFERENCES core.operational_tasks(id);
ALTER TABLE core.task_assignments ADD CONSTRAINT fk_ta_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.task_status_history ADD CONSTRAINT fk_tsh_task FOREIGN KEY (task_id) REFERENCES core.operational_tasks(id);

-- [RECURSOS]
ALTER TABLE core.operational_resources ADD CONSTRAINT fk_res_type FOREIGN KEY (resource_type_id) REFERENCES core.resource_types(id);
ALTER TABLE core.resource_availability ADD CONSTRAINT fk_ra_res FOREIGN KEY (resource_id) REFERENCES core.operational_resources(id);

-- [AGENDA & RESERVAS]
ALTER TABLE core.schedules ADD CONSTRAINT fk_sch_res FOREIGN KEY (resource_id) REFERENCES core.operational_resources(id);
ALTER TABLE core.schedules ADD CONSTRAINT fk_sch_unit FOREIGN KEY (unit_id) REFERENCES core.operational_units(id);
ALTER TABLE core.bookings_erp ADD CONSTRAINT fk_book_op FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);
ALTER TABLE core.bookings_erp ADD CONSTRAINT fk_book_res FOREIGN KEY (resource_id) REFERENCES core.operational_resources(id);
ALTER TABLE core.time_slots ADD CONSTRAINT fk_ts_sch FOREIGN KEY (schedule_id) REFERENCES core.schedules(id);

-- [INCIDENTES]
ALTER TABLE core.incident_actions ADD CONSTRAINT fk_ia_inc FOREIGN KEY (incident_id) REFERENCES core.incidents(id);
ALTER TABLE core.incident_actions ADD CONSTRAINT fk_ia_user FOREIGN KEY (actor_id) REFERENCES identity.users(id);

-- [CHECKLIST]
ALTER TABLE core.checklist_items ADD CONSTRAINT fk_ci_check FOREIGN KEY (checklist_id) REFERENCES core.checklists(id);
ALTER TABLE core.checklist_execution ADD CONSTRAINT fk_ce_check FOREIGN KEY (checklist_id) REFERENCES core.checklists(id);
ALTER TABLE core.checklist_execution ADD CONSTRAINT fk_ce_so FOREIGN KEY (service_order_id) REFERENCES core.service_orders_erp(id);
ALTER TABLE core.checklist_execution ADD CONSTRAINT fk_ce_user FOREIGN KEY (actor_id) REFERENCES identity.users(id);

-- [LOGÍSTICA]
ALTER TABLE core.logistics_orders ADD CONSTRAINT fk_lo_op FOREIGN KEY (operation_id) REFERENCES core.business_operations(id);
ALTER TABLE core.logistics_assignments ADD CONSTRAINT fk_la_ord FOREIGN KEY (logistics_order_id) REFERENCES core.logistics_orders(id);
ALTER TABLE core.logistics_assignments ADD CONSTRAINT fk_la_res FOREIGN KEY (resource_id) REFERENCES core.operational_resources(id);

-- [CAPACIDAD]
ALTER TABLE core.capacity_units ADD CONSTRAINT fk_cu_unit FOREIGN KEY (operational_unit_id) REFERENCES core.operational_units(id);
ALTER TABLE core.capacity_units ADD CONSTRAINT fk_cu_type FOREIGN KEY (resource_type_id) REFERENCES core.resource_types(id);
ALTER TABLE core.occupancy_tracking ADD CONSTRAINT fk_ot_unit FOREIGN KEY (capacity_unit_id) REFERENCES core.capacity_units(id);

-- [GEOLOCALIZACIÓN]
ALTER TABLE core.geo_points_history ADD CONSTRAINT fk_gp_res FOREIGN KEY (resource_id) REFERENCES core.operational_resources(id);
ALTER TABLE core.geo_routes_history ADD CONSTRAINT fk_gr_res FOREIGN KEY (resource_id) REFERENCES core.operational_resources(id);

-- [ESPECIALIZADA - HOTELES]
ALTER TABLE tourism.hotel_rooms ADD CONSTRAINT fk_hr_unit FOREIGN KEY (operational_unit_id) REFERENCES core.operational_units(id);
ALTER TABLE tourism.hotel_rooms ADD CONSTRAINT fk_hr_type FOREIGN KEY (room_type_id) REFERENCES tourism.room_types(id);
ALTER TABLE tourism.room_inventory ADD CONSTRAINT fk_ri_room FOREIGN KEY (room_id) REFERENCES tourism.hotel_rooms(id);

-- [ESPECIALIZADA - RESTAURANTES]
ALTER TABLE tourism.restaurant_tables ADD CONSTRAINT fk_rt_unit FOREIGN KEY (operational_unit_id) REFERENCES core.operational_units(id);
ALTER TABLE tourism.menus ADD CONSTRAINT fk_menu_prov FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);
ALTER TABLE tourism.menu_items ADD CONSTRAINT fk_mi_menu FOREIGN KEY (menu_id) REFERENCES tourism.menus(id);
ALTER TABLE tourism.menu_items ADD CONSTRAINT fk_mi_prod FOREIGN KEY (product_id) REFERENCES core.products(id);
ALTER TABLE tourism.kitchen_orders ADD CONSTRAINT fk_ko_so FOREIGN KEY (service_order_id) REFERENCES core.service_orders_erp(id);
ALTER TABLE tourism.kitchen_orders ADD CONSTRAINT fk_ko_table FOREIGN KEY (table_id) REFERENCES tourism.restaurant_tables(id);
ALTER TABLE tourism.kitchen_display_log ADD CONSTRAINT fk_kdl_ord FOREIGN KEY (kitchen_order_id) REFERENCES tourism.kitchen_orders(id);

-- [ESPECIALIZADA - BARES]
ALTER TABLE tourism.establishment_zones ADD CONSTRAINT fk_ez_unit FOREIGN KEY (operational_unit_id) REFERENCES core.operational_units(id);
ALTER TABLE tourism.liquor_inventory ADD CONSTRAINT fk_li_unit FOREIGN KEY (operational_unit_id) REFERENCES core.operational_units(id);
ALTER TABLE tourism.liquor_inventory ADD CONSTRAINT fk_li_prod FOREIGN KEY (product_id) REFERENCES core.products(id);
ALTER TABLE tourism.box_closing ADD CONSTRAINT fk_bc_unit FOREIGN KEY (operational_unit_id) REFERENCES core.operational_units(id);
ALTER TABLE tourism.box_closing ADD CONSTRAINT fk_bc_user FOREIGN KEY (actor_id) REFERENCES identity.users(id);

-- [ESPECIALIZADA - AGENCIAS]
ALTER TABLE tourism.travel_packages ADD CONSTRAINT fk_tp_prov FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);
ALTER TABLE tourism.package_itineraries ADD CONSTRAINT fk_pi_pack FOREIGN KEY (package_id) REFERENCES tourism.travel_packages(id);
ALTER TABLE tourism.package_pricing ADD CONSTRAINT fk_pp_pack FOREIGN KEY (package_id) REFERENCES tourism.travel_packages(id);
ALTER TABLE tourism.operator_assignments ADD CONSTRAINT fk_oa_so FOREIGN KEY (service_order_id) REFERENCES core.service_orders_erp(id);
ALTER TABLE tourism.operator_assignments ADD CONSTRAINT fk_oa_res FOREIGN KEY (operator_resource_id) REFERENCES core.operational_resources(id);
ALTER TABLE tourism.multi_provider_orders ADD CONSTRAINT fk_mpo_op FOREIGN KEY (main_operation_id) REFERENCES core.business_operations(id);
ALTER TABLE tourism.multi_provider_orders ADD CONSTRAINT fk_mpo_prov FOREIGN KEY (sub_provider_id) REFERENCES tourism.tourism_providers(id);

-- [ESPECIALIZADA - GUÍAS]
ALTER TABLE tourism.guide_profiles ADD CONSTRAINT fk_gp_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE tourism.guide_certifications ADD CONSTRAINT fk_gc_guide FOREIGN KEY (guide_id) REFERENCES tourism.guide_profiles(id);
ALTER TABLE tourism.guide_services ADD CONSTRAINT fk_gs_guide FOREIGN KEY (guide_id) REFERENCES tourism.guide_profiles(id);
ALTER TABLE tourism.association_members ADD CONSTRAINT fk_am_assoc FOREIGN KEY (association_id) REFERENCES tourism.tourism_providers(id);
ALTER TABLE tourism.association_members ADD CONSTRAINT fk_am_guide FOREIGN KEY (guide_user_id) REFERENCES identity.users(id);
ALTER TABLE tourism.association_shared_services ADD CONSTRAINT fk_ass_assoc FOREIGN KEY (association_id) REFERENCES tourism.tourism_providers(id);
ALTER TABLE tourism.association_shared_services ADD CONSTRAINT fk_ass_cat FOREIGN KEY (service_catalog_id) REFERENCES core.service_catalog_extended(id);

-- [ESPECIALIZADA - TRANSPORTE]
ALTER TABLE tourism.operational_vehicles ADD CONSTRAINT fk_ov_prov FOREIGN KEY (provider_id) REFERENCES tourism.tourism_providers(id);
ALTER TABLE tourism.operational_vehicles ADD CONSTRAINT fk_ov_type FOREIGN KEY (vehicle_type_id) REFERENCES tourism.vehicle_types(id);
ALTER TABLE tourism.transport_trips ADD CONSTRAINT fk_tt_so FOREIGN KEY (service_order_id) REFERENCES core.service_orders_erp(id);
ALTER TABLE tourism.transport_trips ADD CONSTRAINT fk_tt_veh FOREIGN KEY (vehicle_id) REFERENCES tourism.operational_vehicles(id);
ALTER TABLE tourism.transport_trips ADD CONSTRAINT fk_tt_user FOREIGN KEY (driver_user_id) REFERENCES identity.users(id);
ALTER TABLE tourism.transport_trips ADD CONSTRAINT fk_tt_route FOREIGN KEY (route_id) REFERENCES core.logistics_routes(id);
ALTER TABLE tourism.trip_passenger_capacity ADD CONSTRAINT fk_tpc_trip FOREIGN KEY (trip_id) REFERENCES tourism.transport_trips(id);
