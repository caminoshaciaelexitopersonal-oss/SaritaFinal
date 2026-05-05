-- 940_rls/tourist_policies.sql
-- Políticas de Seguridad de Fila (RLS) para el dominio Turista

-- Habilitar RLS en las tablas
ALTER TABLE identity.tourist_profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE identity.tourist_realtime_location ENABLE ROW LEVEL SECURITY;
ALTER TABLE identity.tourist_location_history ENABLE ROW LEVEL SECURITY;
ALTER TABLE identity.tourist_searches ENABLE ROW LEVEL SECURITY;
ALTER TABLE identity.tourist_abandoned_carts ENABLE ROW LEVEL SECURITY;
ALTER TABLE identity.tourist_bookings ENABLE ROW LEVEL SECURITY;
ALTER TABLE identity.tourist_payments ENABLE ROW LEVEL SECURITY;
ALTER TABLE identity.tourist_reviews ENABLE ROW LEVEL SECURITY;
ALTER TABLE identity.tourist_reputation ENABLE ROW LEVEL SECURITY;

-- Políticas por tenant_id (Mandatorio)
CREATE POLICY tourist_profile_tenant_isolation ON identity.tourist_profiles
    USING (tenant_id = current_setting('app.current_tenant')::UUID);

CREATE POLICY tourist_location_tenant_isolation ON identity.tourist_realtime_location
    USING (tenant_id = current_setting('app.current_tenant')::UUID);

CREATE POLICY tourist_booking_tenant_isolation ON identity.tourist_bookings
    USING (tenant_id = current_setting('app.current_tenant')::UUID);

-- Políticas de Auto-Acceso (El turista solo ve sus propios datos)
CREATE POLICY tourist_self_access_profile ON identity.tourist_profiles
    FOR ALL
    TO authenticated
    USING (id = current_setting('app.current_user_id')::UUID);

CREATE POLICY tourist_self_access_bookings ON identity.tourist_bookings
    FOR ALL
    TO authenticated
    USING (tourist_id = current_setting('app.current_user_id')::UUID);
