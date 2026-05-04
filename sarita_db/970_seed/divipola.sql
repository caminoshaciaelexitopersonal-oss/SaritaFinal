-- Seed de Estructura Territorial Real (DIVIPOLA Colombia - Ejemplo Base)
-- Nota: En un entorno real este archivo se poblaría desde el CSV oficial del DANE.

-- País
INSERT INTO governance.territorial_entities (id, tenant_id, name, type, dane_code)
VALUES ('00000000-0000-0000-0001-000000000000', '00000000-0000-0000-0000-000000000000', 'COLOMBIA', 'pais', '170')
ON CONFLICT DO NOTHING;

-- Departamentos (Ejemplos)
INSERT INTO governance.territorial_entities (id, tenant_id, name, type, dane_code, parent_id) VALUES
('00000000-0000-0000-0002-000000000050', '00000000-0000-0000-0000-000000000000', 'META', 'departamento', '50', '00000000-0000-0000-0001-000000000000'),
('00000000-0000-0000-0002-000000000025', '00000000-0000-0000-0000-000000000000', 'CUNDINAMARCA', 'departamento', '25', '00000000-0000-0000-0001-000000000000')
ON CONFLICT DO NOTHING;

-- Municipios (Ejemplos)
INSERT INTO governance.territorial_entities (id, tenant_id, name, type, dane_code, parent_id) VALUES
('00000000-0000-0000-0003-000000005001', '00000000-0000-0000-0000-000000000000', 'VILLAVICENCIO', 'municipio', '50001', '00000000-0000-0000-0002-000000000050'),
('00000000-0000-0000-0003-000000005005', '00000000-0000-0000-0000-000000000000', 'PUERTO GAITÁN', 'municipio', '50313', '00000000-0000-0000-0002-000000000050')
ON CONFLICT DO NOTHING;
