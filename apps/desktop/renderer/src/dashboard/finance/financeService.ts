import { api } from '../../services/api';

/**
 * SARITA Finance Service
 * Consumo de ratios financieros y análisis de flujo de caja.
 * No realiza cálculos locales, consume la verdad del Backend.
 */

export const financeService = {
  // Ratios Financieros (Liquidez, Rentabilidad, Márgenes)
  getRatios: (date?: string) => api.get('/finance/ratios/', {
    params: { date }
  }),

  // Análisis de Flujo de Caja
  getCashFlow: (start: string, end: string) => api.get('/finance/cashflow/', {
    params: { start, end }
  }),

  // Reportes Detallados de Ingresos y Gastos
  getIncomeReport: (params = {}) => api.get('/accounting/reports/p-and-l/', { params }),

  // Alertas Financieras (Basadas en los ratios y estados)
  getFinancialAlerts: () => api.get('/finance/alerts/'), // Endpoint proyectado o simulado por ahora
};
