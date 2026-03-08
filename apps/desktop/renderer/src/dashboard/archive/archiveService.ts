import { api } from '../../services/api';

/**
 * SARITA Archive & Document Service
 * Gestión de archivos, metadatos y auditoría documental.
 */

export const archiveService = {
  // Documentos
  getDocuments: (params = {}) => api.get('/documents/', { params }),
  uploadDocument: (formData: FormData) => api.post('/documents/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  }),
  getDocumentDetail: (id: string) => api.get(`/documents/${id}/`),
  updateDocument: (id: string, data: any) => api.put(`/documents/${id}/`, data),
  deleteDocument: (id: string) => api.delete(`/documents/${id}/`),

  // Versiones
  getDocumentVersions: (id: string) => api.get(`/documents/${id}/versions/`),

  // Categorías
  getCategories: () => api.get('/document-categories/'),

  // Auditoría
  getActivityLog: () => api.get('/documents/activity-log/'),

  // Métricas
  getStorageMetrics: () => api.get('/documents/storage-metrics/'),
};
