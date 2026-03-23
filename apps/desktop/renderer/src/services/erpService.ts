import { api } from '../../services/api';

/**
 * SARITA Human Capital Service
 * Gestión de empleados y nómina para el ERP Desktop.
 */

export const erpService = {
  // Gestión de Empleados
  getEmployees: () => api.get('/payroll/employees/'),
  createEmployee: (data: any) => api.post('/payroll/employees/', data),
  updateEmployee: (id: string, data: any) => api.patch(`/payroll/employees/${id}/`, data),

  // Nómina
  getPayrollRuns: () => api.get('/payroll/runs/'),
  createPayrollRun: (data: any) => api.post('/payroll/runs/', data),
  getPayrollDetails: (runId: string) => api.get(`/payroll/runs/${runId}/details/`),

  // Contratos
  getContracts: () => api.get('/payroll/contracts/'),
  createContract: (data: any) => api.post('/payroll/contracts/', data),

  // Sincronización Local (Offline-first support)
  syncLocalChanges: (pendingItems: any[]) => api.post('/sync/erp-data/', { items: pendingItems }),
};
