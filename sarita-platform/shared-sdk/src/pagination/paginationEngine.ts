/**
 * Motor de Paginación Unificado (Django REST Framework Style)
 * Garantiza que Web, Mobile y Desktop usen el mismo contrato de datos.
 */

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export class PaginationEngine {
  /**
   * Transforma una respuesta cruda del API en un objeto paginado tipado.
   */
  static transform<T>(data: any): PaginatedResponse<T> {
    return {
      count: data.count || 0,
      next: data.next || null,
      previous: data.previous || null,
      results: data.results || [],
    };
  }

  /**
   * Genera los parámetros de búsqueda para la siguiente página.
   */
  static getPageParams(page: number, pageSize: number = 20) {
    return {
      page,
      page_size: pageSize,
    };
  }
}
