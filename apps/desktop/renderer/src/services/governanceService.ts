import { api } from './api';

export const governanceService = {
  getOfficials: () => api.get('/government/'),
  createOfficial: (data: any) => api.post('/government/', data),
};
