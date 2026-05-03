-- Definición de esquemas para la arquitectura Triple Vía de SARITA - HARDENING FASE 10

-- 01 Core & Multitenancy
CREATE SCHEMA IF NOT EXISTS core;

-- 02 Identity & Access Management
CREATE SCHEMA IF NOT EXISTS identity;

-- 03 Governance & Institutional (Vía 1)
CREATE SCHEMA IF NOT EXISTS governance;

-- 04 Autonomous Agents & AI
CREATE SCHEMA IF NOT EXISTS agents;

-- 05-09 ERP Domains (Vía 2)
CREATE SCHEMA IF NOT EXISTS erp_comercial;
CREATE SCHEMA IF NOT EXISTS erp_operativo;
CREATE SCHEMA IF NOT EXISTS erp_contable;
CREATE SCHEMA IF NOT EXISTS erp_financiero;
CREATE SCHEMA IF NOT EXISTS erp_archivistico;

-- 10 Financial & Wallets
CREATE SCHEMA IF NOT EXISTS wallet;

-- 11 Logistics & Delivery
CREATE SCHEMA IF NOT EXISTS delivery;

-- 12 Audit & Forensic
CREATE SCHEMA IF NOT EXISTS auditoria;

-- 13 AI Memory & Intelligence
CREATE SCHEMA IF NOT EXISTS ai_memory;

-- 14 External Integrations
CREATE SCHEMA IF NOT EXISTS integraciones;

-- 15 Event Sourcing (Reconstrucción Total)
CREATE SCHEMA IF NOT EXISTS events;

-- 16 Wallet Ledger (Contabilidad Financiera Real)
CREATE SCHEMA IF NOT EXISTS ledger;

-- 17 Payment Orchestrator
CREATE SCHEMA IF NOT EXISTS payments;

-- 18 AI Memory (Capa Extendida)
-- Reutiliza schema ai_memory definido arriba

-- 19 KYC & Identity Verification
CREATE SCHEMA IF NOT EXISTS kyc;

-- 21 Global Tax Engine
CREATE SCHEMA IF NOT EXISTS tax;

-- 22 Bank Reconciliation
CREATE SCHEMA IF NOT EXISTS reconciliation;

-- 23 Archival & Legal
CREATE SCHEMA IF NOT EXISTS archival;

-- Social & Tourist (Vía 3)
CREATE SCHEMA IF NOT EXISTS social;
CREATE SCHEMA IF NOT EXISTS turismo;
