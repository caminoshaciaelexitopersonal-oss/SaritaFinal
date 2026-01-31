import { AxiosInstance, AxiosError, InternalAxiosRequestConfig } from 'axios';

export const setupInterceptors = (httpClient: AxiosInstance) => {
  httpClient.interceptors.request.use(
    (config: InternalAxiosRequestConfig) => {
      if (typeof window !== 'undefined') {
        const token = localStorage.getItem('token') || localStorage.getItem('authToken');
        if (token) {
          config.headers.Authorization = `Token ${token}`;
        }

        // Multi-tenant / Context headers
        const companyId = localStorage.getItem('activeCompanyId');
        if (companyId) {
          config.headers['X-Company-ID'] = companyId;
        }

        const periodId = localStorage.getItem('activePeriodId');
        if (periodId) {
          config.headers['X-Accounting-Period'] = periodId;
        }
      }
      return config;
    },
    (error) => Promise.reject(error)
  );

  httpClient.interceptors.response.use(
    (response) => response,
    (error: AxiosError) => {
      const status = error.response?.status;

      if (status === 401) {
        if (typeof window !== 'undefined') {
          localStorage.removeItem('token');
          localStorage.removeItem('authToken');
          // Optional: redirect to login
          // window.location.href = '/dashboard/login';
        }
      }

      // Normalized error handling
      const normalizedError = {
        code: status || 500,
        message: (error.response?.data as any)?.detail || (error.response?.data as any)?.message || 'Ocurrió un error inesperado.',
        technical: error.message,
        action: status === 401 ? 'REAUTH' : 'RETRY'
      };

      return Promise.reject(normalizedError);
    }
  );
};
