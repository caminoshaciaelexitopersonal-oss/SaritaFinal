-- Relaciones transversales y restricciones globales - GESTIÓN ARCHIVÍSTICA TOTAL

-- [ESTRUCTURA]
ALTER TABLE archival.document_types_extended ADD CONSTRAINT fk_dtype_cat FOREIGN KEY (category_id) REFERENCES archival.document_categories(id);
ALTER TABLE archival.file_entities ADD CONSTRAINT fk_fent_file FOREIGN KEY (file_id) REFERENCES archival.files(id);

-- [DOCUMENTOS]
ALTER TABLE archival.documents_main ADD CONSTRAINT fk_doc_file FOREIGN KEY (file_id) REFERENCES archival.files(id);
ALTER TABLE archival.documents_main ADD CONSTRAINT fk_doc_type FOREIGN KEY (type_id) REFERENCES archival.document_types_extended(id);
-- current_version_id es ref circular, se aplica después si es necesario o se deja para lógica app
ALTER TABLE archival.document_relations ADD CONSTRAINT fk_dr_parent FOREIGN KEY (parent_doc_id) REFERENCES archival.documents_main(id);
ALTER TABLE archival.document_relations ADD CONSTRAINT fk_dr_child FOREIGN KEY (child_doc_id) REFERENCES archival.documents_main(id);

-- [VERSIONADO]
ALTER TABLE archival.document_versions ADD CONSTRAINT fk_dv_doc FOREIGN KEY (document_id) REFERENCES archival.documents_main(id);
ALTER TABLE archival.document_versions ADD CONSTRAINT fk_dv_author FOREIGN KEY (author_id) REFERENCES identity.users(id);
ALTER TABLE archival.version_changes ADD CONSTRAINT fk_vc_ver FOREIGN KEY (version_id) REFERENCES archival.document_versions(id);

-- [METADATOS]
ALTER TABLE archival.metadata_fields ADD CONSTRAINT fk_mf_sch FOREIGN KEY (schema_id) REFERENCES archival.metadata_schemas(id);
ALTER TABLE archival.document_metadata_values ADD CONSTRAINT fk_dmv_doc FOREIGN KEY (document_id) REFERENCES archival.documents_main(id);
ALTER TABLE archival.document_metadata_values ADD CONSTRAINT fk_dmv_field FOREIGN KEY (field_id) REFERENCES archival.metadata_fields(id);

-- [INTELIGENCIA]
ALTER TABLE archival.classification_rules ADD CONSTRAINT fk_cr_type FOREIGN KEY (target_type_id) REFERENCES archival.document_types_extended(id);
ALTER TABLE archival.classification_results ADD CONSTRAINT fk_clres_doc FOREIGN KEY (document_id) REFERENCES archival.documents_main(id);
ALTER TABLE archival.ocr_jobs ADD CONSTRAINT fk_oj_ver FOREIGN KEY (version_id) REFERENCES archival.document_versions(id);
ALTER TABLE archival.ocr_results ADD CONSTRAINT fk_or_job FOREIGN KEY (job_id) REFERENCES archival.ocr_jobs(id);

-- [CICLO DE VIDA]
ALTER TABLE archival.lifecycle_transitions ADD CONSTRAINT fk_lt_from FOREIGN KEY (from_state_id) REFERENCES archival.lifecycle_states(id);
ALTER TABLE archival.lifecycle_transitions ADD CONSTRAINT fk_lt_to FOREIGN KEY (to_state_id) REFERENCES archival.lifecycle_states(id);
ALTER TABLE archival.lifecycle_logs ADD CONSTRAINT fk_ll_doc FOREIGN KEY (document_id) REFERENCES archival.documents_main(id);
ALTER TABLE archival.lifecycle_logs ADD CONSTRAINT fk_ll_actor FOREIGN KEY (actor_id) REFERENCES identity.users(id);

-- [SEGURIDAD]
ALTER TABLE archival.document_permissions ADD CONSTRAINT fk_dp_doc FOREIGN KEY (document_id) REFERENCES archival.documents_main(id);
ALTER TABLE archival.document_permissions ADD CONSTRAINT fk_dp_file FOREIGN KEY (file_id) REFERENCES archival.files(id);
ALTER TABLE archival.document_access_logs ADD CONSTRAINT fk_dal_doc FOREIGN KEY (document_id) REFERENCES archival.documents_main(id);
ALTER TABLE archival.document_access_logs ADD CONSTRAINT fk_dal_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

-- [FIRMA Y NOTARIZACIÓN]
ALTER TABLE archival.signature_requests ADD CONSTRAINT fk_sr_ver FOREIGN KEY (document_version_id) REFERENCES archival.document_versions(id);
ALTER TABLE archival.signature_participants ADD CONSTRAINT fk_sp_req FOREIGN KEY (request_id) REFERENCES archival.signature_requests(id);
ALTER TABLE archival.signature_participants ADD CONSTRAINT fk_sp_user FOREIGN KEY (user_id) REFERENCES identity.users(id);
ALTER TABLE archival.signatures ADD CONSTRAINT fk_sig_part FOREIGN KEY (participant_id) REFERENCES archival.signature_participants(id);
ALTER TABLE archival.notarizations ADD CONSTRAINT fk_not_ver FOREIGN KEY (document_version_id) REFERENCES archival.document_versions(id);
ALTER TABLE archival.notarizations ADD CONSTRAINT fk_not_prov FOREIGN KEY (provider_id) REFERENCES archival.notarization_providers(id);

-- [TRAZABILIDAD Y RETENCIÓN]
ALTER TABLE archival.document_audit_logs_extended ADD CONSTRAINT fk_dale_doc FOREIGN KEY (document_id) REFERENCES archival.documents_main(id);
ALTER TABLE archival.document_events ADD CONSTRAINT fk_de_doc FOREIGN KEY (document_id) REFERENCES archival.documents_main(id);
ALTER TABLE archival.retention_rules ADD CONSTRAINT fk_rr_pol FOREIGN KEY (policy_id) REFERENCES archival.retention_policies_extended(id);
ALTER TABLE archival.retention_rules ADD CONSTRAINT fk_rr_type FOREIGN KEY (document_type_id) REFERENCES archival.document_types_extended(id);
ALTER TABLE archival.disposal_logs ADD CONSTRAINT fk_dl_doc FOREIGN KEY (document_id) REFERENCES archival.documents_main(id);

-- [EXPORTACIÓN]
ALTER TABLE archival.export_jobs ADD CONSTRAINT fk_ej_user FOREIGN KEY (request_id) REFERENCES identity.users(id);
ALTER TABLE archival.export_files ADD CONSTRAINT fk_ef_job FOREIGN KEY (job_id) REFERENCES archival.export_jobs(id);
