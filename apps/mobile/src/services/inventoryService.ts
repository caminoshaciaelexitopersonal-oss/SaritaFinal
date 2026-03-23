import { api } from './api';

/**
 * SARITA Global Inventory Service (Fase 06)
 * Gestión centralizada de tours, eventos, transporte y restaurantes.
 */

export const inventoryService = {
  getInventory: (params = {}) => api.get('/inventory/', { params }),

  syncGlobalStock: (id: string, type: string) => api.post(`/inventory/${id}/sync/`, { type }),

  getMultiCurrencyPrice: (amount: number, from: string, to: string) =>
    api.get('/inventory/convert-currency/', { params: { amount, from, to } }),
};
