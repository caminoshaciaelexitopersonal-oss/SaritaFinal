-- Relaciones transversales y restricciones globales - ARTESANOS

-- [IDENTIDAD]
ALTER TABLE tourism.artisans ADD CONSTRAINT fk_artisan_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE tourism.artisan_profiles ADD CONSTRAINT fk_ap_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);
ALTER TABLE tourism.artisan_association_members ADD CONSTRAINT fk_aam_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);
ALTER TABLE tourism.artisan_association_members ADD CONSTRAINT fk_aam_assoc FOREIGN KEY (association_id) REFERENCES tourism.artisan_associations(id);

-- [UBICACIÓN]
ALTER TABLE tourism.artisan_locations ADD CONSTRAINT fk_al_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);
ALTER TABLE tourism.artisan_workshops ADD CONSTRAINT fk_aw_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);

-- [CATÁLOGO]
ALTER TABLE tourism.artisan_products ADD CONSTRAINT fk_aprod_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);
ALTER TABLE tourism.artisan_products ADD CONSTRAINT fk_aprod_cat FOREIGN KEY (categoria_id) REFERENCES tourism.artisan_categories(id);
ALTER TABLE tourism.artisan_product_variants ADD CONSTRAINT fk_apv_prod FOREIGN KEY (producto_id) REFERENCES tourism.artisan_products(id);
ALTER TABLE tourism.artisan_product_materials ADD CONSTRAINT fk_apm_prod FOREIGN KEY (producto_id) REFERENCES tourism.artisan_products(id);
ALTER TABLE tourism.artisan_product_images ADD CONSTRAINT fk_api_prod FOREIGN KEY (producto_id) REFERENCES tourism.artisan_products(id);

-- [INVENTARIO / PRODUCCIÓN]
ALTER TABLE tourism.artisan_inventory ADD CONSTRAINT fk_ainv_prod FOREIGN KEY (producto_id) REFERENCES tourism.artisan_products(id);
ALTER TABLE tourism.artisan_production_orders ADD CONSTRAINT fk_apo_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);
ALTER TABLE tourism.artisan_production_orders ADD CONSTRAINT fk_apo_prod FOREIGN KEY (producto_id) REFERENCES tourism.artisan_products(id);
ALTER TABLE tourism.artisan_production_stages ADD CONSTRAINT fk_aps_order FOREIGN KEY (orden_id) REFERENCES tourism.artisan_production_orders(id);

-- [CLASIFICACIÓN]
ALTER TABLE tourism.artisan_product_tags ADD CONSTRAINT fk_apt_prod FOREIGN KEY (producto_id) REFERENCES tourism.artisan_products(id);
ALTER TABLE tourism.artisan_certifications_extended ADD CONSTRAINT fk_ace_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);

-- [DIRECTORIO]
ALTER TABLE tourism.artisan_directory_index ADD CONSTRAINT fk_adi_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);
ALTER TABLE tourism.artisan_ratings ADD CONSTRAINT fk_arat_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);
ALTER TABLE tourism.artisan_ratings ADD CONSTRAINT fk_arat_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

-- [EVENTOS]
ALTER TABLE tourism.artisan_events_participation ADD CONSTRAINT fk_aep_artisan FOREIGN KEY (artisan_id) REFERENCES tourism.artisans(id);
ALTER TABLE tourism.artisan_events_participation ADD CONSTRAINT fk_aep_event FOREIGN KEY (evento_id) REFERENCES tourism.events(id);
