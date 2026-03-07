import { api } from '../services/api';

export const useTours = (params = {}) => {
  return api.get('/tours', { params });
};
