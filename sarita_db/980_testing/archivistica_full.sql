-- Test de Gestión Archivística Institucional
DO $$
DECLARE
    v_tenant_id UUID := '00000000-0000-0000-0000-000000000000';
    v_trace_id UUID := gen_random_uuid();
    v_file_id UUID;
    v_type_id UUID;
    v_doc_id UUID;
    v_version_id UUID;
BEGIN
    -- Contexto
    PERFORM set_config('app.current_tenant', v_tenant_id::text, false);

    -- 1. Crear Expediente
    INSERT INTO archival.files (file_number, title, tenant_id, trace_id)
    VALUES ('EXP-2026-001', 'Expediente Maestro Test', v_tenant_id, v_trace_id)
    RETURNING id INTO v_file_id;

    -- 2. Crear Tipo y Categoría
    INSERT INTO archival.document_categories (name, tenant_id, trace_id)
    VALUES ('Legal', v_tenant_id, v_trace_id)
    RETURNING id INTO v_type_id; -- Reusando variable para simplicidad

    INSERT INTO archival.document_types_extended (name, category_id, tenant_id, trace_id)
    VALUES ('Contrato Marco', v_type_id, v_tenant_id, v_trace_id)
    RETURNING id INTO v_type_id;

    -- 3. Crear Documento (Core)
    INSERT INTO archival.documents_main (file_id, type_id, title, tenant_id, trace_id)
    VALUES (v_file_id, v_type_id, 'Contrato Proveedor X', v_tenant_id, v_trace_id)
    RETURNING id INTO v_doc_id;

    -- 4. Crear Versión (Inmutable)
    INSERT INTO archival.document_versions (document_id, version_number, file_url, binary_hash, author_id, tenant_id, trace_id)
    VALUES (v_doc_id, 1, 'https://storage.sarita.com/v1.pdf', 'hash-real-sha256', v_tenant_id, v_tenant_id, v_trace_id)
    RETURNING id INTO v_version_id;

    -- 5. Simular Firma
    INSERT INTO archival.signature_requests (document_version_id, tenant_id, trace_id)
    VALUES (v_version_id, v_tenant_id, v_trace_id);

    -- 6. Validar Trazabilidad (Trigger check)
    IF NOT EXISTS (SELECT 1 FROM events.event_store WHERE trace_id = v_trace_id) THEN
        RAISE EXCEPTION 'Falla: El evento archivístico no se registró en Event Store';
    END IF;

    RAISE NOTICE 'Test Archivística Institucional: PASSED';
END;
$$;
