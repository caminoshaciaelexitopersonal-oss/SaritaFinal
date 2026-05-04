-- Relaciones transversales y restricciones globales - VÍA 3 TURISTAS

-- [PERFIL]
ALTER TABLE tourism.tourist_profiles ADD CONSTRAINT fk_tprof_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE tourism.tourist_preferences ADD CONSTRAINT fk_tpref_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

-- [GEOLOCALIZACION]
ALTER TABLE tourism.tourist_locations ADD CONSTRAINT fk_tloc_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE tourism.tourist_geo_history ADD CONSTRAINT fk_tgeoh_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

-- [COMPORTAMIENTO]
ALTER TABLE core.tourist_sessions ADD CONSTRAINT fk_tsess_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.tourist_events ADD CONSTRAINT fk_tev_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.tourist_searches ADD CONSTRAINT fk_tsea_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

-- [HISTORIAL]
ALTER TABLE core.tourist_orders ADD CONSTRAINT fk_tord_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.tourist_orders ADD CONSTRAINT fk_tord_order FOREIGN KEY (order_id) REFERENCES core.sales_orders(id);
ALTER TABLE core.tourist_reservations ADD CONSTRAINT fk_tres_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

-- [INTERACCIONES]
ALTER TABLE core.tourist_favorites ADD CONSTRAINT fk_tfav_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.tourist_reviews_extended ADD CONSTRAINT fk_treve_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.tourist_recommendation_logs ADD CONSTRAINT fk_trecl_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.tourist_feed ADD CONSTRAINT fk_tfeed_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

-- [CITAS]
ALTER TABLE core.appointments ADD CONSTRAINT fk_appo_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE core.appointment_bookings ADD CONSTRAINT fk_ab_appo FOREIGN KEY (appointment_id) REFERENCES core.appointments(id);
ALTER TABLE core.appointment_bookings ADD CONSTRAINT fk_ab_slot FOREIGN KEY (slot_id) REFERENCES core.appointment_slots(id);
ALTER TABLE core.appointment_attendance ADD CONSTRAINT fk_aa_book FOREIGN KEY (booking_id) REFERENCES core.appointment_bookings(id);
