-- Datos Maestros Iniciales

-- Crear un Tenant Maestro para el sistema (Administración Global)
INSERT INTO core.tenants (id, name, legal_name, tax_id, domain, state)
VALUES ('00000000-0000-0000-0000-000000000000', 'SARITA GLOBAL', 'SARITA SISTEMA SOBERANO', '000000000-0', 'sarita.internal', 'ACTIVE')
ON CONFLICT DO NOTHING;

-- Roles Globales de Sistema (Asociados al Tenant Maestro)
INSERT INTO identity.roles (name, description, authority_level, is_system_role, tenant_id) VALUES
('SUPER_ADMIN', 'Control total soberano del sistema', 3, true, '00000000-0000-0000-0000-000000000000'),
('GOV_ADMIN', 'Administrador gubernamental (Vía 1)', 2, true, '00000000-0000-0000-0000-000000000000'),
('BUSINESS_OWNER', 'Propietario de Negocio (Vía 2)', 1, true, '00000000-0000-0000-0000-000000000000'),
('TOURIST', 'Turista / Ciudadano (Vía 3)', 1, true, '00000000-0000-0000-0000-000000000000')
ON CONFLICT DO NOTHING;

-- Tipos de Documentos de Verificación
INSERT INTO integraciones.document_types (name, description, is_required, tenant_id) VALUES
('RNT', 'Registro Nacional de Turismo', true, '00000000-0000-0000-0000-000000000000'),
('RUT', 'Registro Único Tributario', true, '00000000-0000-0000-0000-000000000000'),
('CAMARA_COMERCIO', 'Certificado de Existencia y Representación Legal', true, '00000000-0000-0000-0000-000000000000')
ON CONFLICT DO NOTHING;
