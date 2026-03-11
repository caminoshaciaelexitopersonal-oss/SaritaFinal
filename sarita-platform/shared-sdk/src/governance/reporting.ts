import { httpClient } from '../api/httpClient';

export interface ReportSummary {
  id: string;
  name: string;
  category: 'tourism' | 'economic' | 'provider' | 'operational';
  generatedAt: string;
  format: 'pdf' | 'excel' | 'csv';
}

export interface ChartDataSet {
  title: string;
  data: Array<{ label: string; value: number; color?: string }>;
}

export class ReportingService {
  /**
   * Obtiene el listado de reportes generados recientemente.
   */
  static async getRecentReports(): Promise<ReportSummary[]> {
    const response = await httpClient.get('/analytics/reports/recent/');
    return response.data;
  }

  /**
   * Obtiene datos para dashboards analíticos.
   */
  static async getAnalyticsSummary(): Promise<any> {
    const response = await httpClient.get('/dashboard/analytics/');
    return response.data;
  }

  /**
   * Solicita la generación de un nuevo reporte.
   */
  static async generateReport(config: { dataset: string; filters: any; format: string }): Promise<{ job_id: string }> {
    const response = await httpClient.post('/analytics/reports/generate/', config);
    return response.data;
  }
}
