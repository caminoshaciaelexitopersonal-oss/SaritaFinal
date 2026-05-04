-- Definición de esquemas para la arquitectura Triple Vía de SARITA - HARDENING FASE 10 (BANCO CENTRAL)

-- 01-14 Core, Identity, Governance, ERP, etc
CREATE SCHEMA IF NOT EXISTS core;
CREATE SCHEMA IF NOT EXISTS identity;
CREATE SCHEMA IF NOT EXISTS governance;
CREATE SCHEMA IF NOT EXISTS agents;
CREATE SCHEMA IF NOT EXISTS erp_comercial;
CREATE SCHEMA IF NOT EXISTS erp_operativo;
CREATE SCHEMA IF NOT EXISTS erp_contable;
CREATE SCHEMA IF NOT EXISTS erp_financiero;
CREATE SCHEMA IF NOT EXISTS erp_archivistico;

-- ERP Mi Negocio (Soberanía de Datos 30-41)
CREATE SCHEMA IF NOT EXISTS crm;
CREATE SCHEMA IF NOT EXISTS accounting;
CREATE SCHEMA IF NOT EXISTS finance;
CREATE SCHEMA IF NOT EXISTS inventory;
CREATE SCHEMA IF NOT EXISTS logistics;
CREATE SCHEMA IF NOT EXISTS operational;
CREATE SCHEMA IF NOT EXISTS wallet;
CREATE SCHEMA IF NOT EXISTS delivery;
CREATE SCHEMA IF NOT EXISTS auditoria;
CREATE SCHEMA IF NOT EXISTS ai_memory;
CREATE SCHEMA IF NOT EXISTS integrations;

-- 15-26 Advanced Domains
CREATE SCHEMA IF NOT EXISTS events;
CREATE SCHEMA IF NOT EXISTS ledger;
CREATE SCHEMA IF NOT EXISTS payments;
CREATE SCHEMA IF NOT EXISTS kyc;
CREATE SCHEMA IF NOT EXISTS tax;
CREATE SCHEMA IF NOT EXISTS reconciliation;
CREATE SCHEMA IF NOT EXISTS archival;

-- 27-31 Hardening Schemas
-- Reutiliza core para retry y scheduler si no se especifican nuevos schemas,
-- pero la directriz menciona esquemas específicos en las funciones.
CREATE SCHEMA IF NOT EXISTS retry;
CREATE SCHEMA IF NOT EXISTS ai;
CREATE SCHEMA IF NOT EXISTS scheduler;
CREATE SCHEMA IF NOT EXISTS watchdog;

-- Social & Tourist (Vía 3)
CREATE SCHEMA IF NOT EXISTS social;
CREATE SCHEMA IF NOT EXISTS turismo;
