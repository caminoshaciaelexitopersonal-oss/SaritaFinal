-- Test Omnicanal Comercial Full
DO $$
DECLARE
    v_tenant_id UUID := '00000000-0000-0000-0000-000000000000';
    v_trace_id UUID := gen_random_uuid();
    v_lead_id UUID;
    v_convo_id UUID;
    v_asset_id UUID;
    v_campaign_id UUID;
BEGIN
    -- Contexto
    PERFORM set_config('app.current_tenant', v_tenant_id::text, false);

    -- 1. Crear Lead
    INSERT INTO core.leads_erp (nombre, email, source, tenant_id, trace_id)
    VALUES ('Lead Omnicanal', 'lead@omni.com', 'whatsapp', v_tenant_id, v_trace_id)
    RETURNING id INTO v_lead_id;

    -- 2. Iniciar Conversación Social
    INSERT INTO core.social_conversations (account_id, external_convo_id, participant_handle, customer_id, tenant_id, trace_id)
    VALUES (gen_random_uuid(), 'WA-123', '+573000000', NULL, v_tenant_id, v_trace_id)
    RETURNING id INTO v_convo_id;

    -- 3. Recibir Mensaje (Trigger ES + AI)
    INSERT INTO core.social_messages (conversation_id, sender_handle, message_text, tenant_id, trace_id)
    VALUES (v_convo_id, '+573000000', 'Quiero informes del hotel', v_tenant_id, v_trace_id);

    -- 4. Crear Asset Multimedia (Video)
    INSERT INTO core.media_assets (name, file_type, tenant_id, trace_id)
    VALUES ('Video Promocional', 'video', v_tenant_id, v_trace_id)
    RETURNING id INTO v_asset_id;

    -- 5. Crear Campaña y Vincular Asset
    INSERT INTO core.marketing_campaigns (name, objective, tenant_id, trace_id)
    VALUES ('Campaña Verano', 'Conversión', v_tenant_id, v_trace_id)
    RETURNING id INTO v_campaign_id;

    INSERT INTO core.content_campaign_links (campaign_id, asset_id, tenant_id, trace_id)
    VALUES (v_campaign_id, v_asset_id, v_tenant_id, v_trace_id);

    -- 6. Validar que la IA fue notificada (Trigger check)
    IF NOT EXISTS (SELECT 1 FROM ai_core.agent_events WHERE trace_id = v_trace_id) THEN
        RAISE EXCEPTION 'Falla: La IA no fue notificada del mensaje entrante';
    END IF;

    RAISE NOTICE 'Test Comercial Omnicanal: PASSED';
END;
$$;
