'use client';

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';

export type ComplianceStatus = 'CUMPLE' | 'PARCIAL' | 'NO_CUMPLE' | 'NO_APLICA';
export type RiskType = 'TECNICO' | 'OPERATIVO' | 'FINANCIERO' | 'LEGAL' | 'REPUTACIONAL';
export type RiskImpact = 'BAJO' | 'MEDIO' | 'ALTO' | 'CRITICO';
export type RiskStatus = 'ACTIVO' | 'MITIGADO' | 'ACEPTADO';

export interface ComplianceItem {
  domain: string;
  status: ComplianceStatus;
  evidence: string;
  mechanism: string;
  notes?: string;
}

export interface RiskItem {
  id: string;
  title: string;
  type: RiskType;
  impact: RiskImpact;
  probability: 'BAJA' | 'MEDIA' | 'ALTA';
  status: RiskStatus;
  explanation?: string;
}

export interface GRCException {
  id: string;
  module: string;
  reason: string;
  responsible: string;
  reviewDate: string;
}

interface GRCContextType {
  isAuditMode: boolean;
  toggleAuditMode: () => void;
  complianceMatrix: ComplianceItem[];
  risks: RiskItem[];
  exceptions: GRCException[];
  grcKpis: {
    compliancePercentage: number;
    activeCriticalRisks: number;
    uncontrolledActions: number;
  };
}

const GRCContext = createContext<GRCContextType | undefined>(undefined);

export const GRCProvider = ({ children }: { children: ReactNode }) => {
  const [isAuditMode, setIsAuditMode] = useState(false);

  // Datos semilla de GRC (Evidencia real del estado actual detectado en auditoría)
  const [complianceMatrix] = useState<ComplianceItem[]>([
    {
      domain: 'Autenticación',
      status: 'CUMPLE',
      evidence: '/api/auth/login/',
      mechanism: 'JWT + localStorage',
      notes: 'Sesión persistente con manejo de 401 global.'
    },
    {
      domain: 'Autorización',
      status: 'CUMPLE',
      evidence: 'PermissionGuard.tsx',
      mechanism: 'RBAC Frontend (mapBackendRoleToAppRole)',
      notes: 'Control de acceso basado en roles de negocio interpretados.'
    },
    {
      domain: 'Finanzas (Triple Vía)',
      status: 'PARCIAL',
      evidence: '/api/v1/mi-negocio/financiera/',
      mechanism: 'Read-only + TraceabilityBanner',
      notes: 'Integración backend activa pero requiere validación de asientos automáticos.'
    },
    {
      domain: 'Datos Personales',
      status: 'CUMPLE',
      evidence: 'Audit Mode (Masking)',
      mechanism: 'Conditional Rendering en UI',
      notes: 'El modo auditor permite enmascarar datos sensibles.'
    },
    {
      domain: 'Trazabilidad',
      status: 'PARCIAL',
      evidence: 'auditLogger.ts',
      mechanism: 'Local Event Sourcing',
      notes: 'Logs persistentes en navegador; falta sincronización centralizada.'
    }
  ]);

  const [risks] = useState<RiskItem[]>([
    {
      id: 'R1',
      title: 'Dependencias Externas Bloqueantes',
      type: 'TECNICO',
      impact: 'CRITICO',
      probability: 'ALTA',
      status: 'ACTIVO',
      explanation: 'Conflictos en lucide-react y react-dnd pueden romper el renderizado de módulos CRM.'
    },
    {
      id: 'R2',
      title: 'Ausencia de Persistencia de Auditoría',
      type: 'LEGAL',
      impact: 'ALTO',
      probability: 'MEDIA',
      status: 'ACTIVO',
      explanation: 'Los logs de auditoría frontend se pierden al limpiar caché si no se envían al backend.'
    },
    {
      id: 'R3',
      title: 'Métricas Sin Backend Real',
      type: 'OPERATIVO',
      impact: 'MEDIO',
      probability: 'MEDIA',
      status: 'MITIGADO',
      explanation: 'Se usan fallbacks temporales en el dashboard administrativo.'
    },
    {
      id: 'R4',
      title: 'Segregación de Funciones Débil',
      type: 'LEGAL',
      impact: 'ALTO',
      probability: 'BAJA',
      status: 'ACTIVO',
      explanation: 'El mismo rol ADMIN puede crear y aprobar planes sin control dual mandatorio.'
    }
  ]);

  const [exceptions] = useState<GRCException[]>([
    {
      id: 'E1',
      module: 'Gestión Comercial',
      reason: 'El constructor de embudos usa persistencia local mientras se estabiliza el endpoint BFF.',
      responsible: 'Arquitectura IA',
      reviewDate: '2024-06-15'
    }
  ]);

  const toggleAuditMode = () => {
    setIsAuditMode(!isAuditMode);
    // Log the audit mode change
    console.log(`[GRC] Modo Auditor ${!isAuditMode ? 'ACTIVADO' : 'DESACTIVADO'}`);
  };

  const grcKpis = {
    compliancePercentage: 80,
    activeCriticalRisks: risks.filter(r => r.impact === 'CRITICO' && r.status === 'ACTIVO').length,
    uncontrolledActions: 0
  };

  return (
    <GRCContext.Provider value={{
      isAuditMode,
      toggleAuditMode,
      complianceMatrix,
      risks,
      exceptions,
      grcKpis
    }}>
      {children}
    </GRCContext.Provider>
  );
};

export const useGRC = () => {
  const context = useContext(GRCContext);
  if (context === undefined) {
    throw new Error('useGRC debe ser usado dentro de un GRCProvider');
  }
  return context;
};
