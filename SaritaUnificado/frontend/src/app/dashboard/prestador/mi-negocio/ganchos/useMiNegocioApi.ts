import { useState, useCallback } from 'react';

// Define una URL base para la API de "Mi Negocio"
const API_BASE_URL = '/api/v1/prestadores/mi-negocio';

/**
 * Hook personalizado para interactuar con la API de "Mi Negocio".
 * Maneja el estado de carga, errores y la obtención de datos.
 */
const useMiNegocioApi = () => {
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  /**
   * Función genérica para realizar solicitudes a la API.
   * @param endpoint - El endpoint específico al que se llamará (ej. '/perfil/').
   * @param options - Opciones de la solicitud (método, cuerpo, etc.).
   */
  const request = useCallback(async (endpoint: string, options: RequestInit = {}) => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        ...options,
        headers: {
          'Content-Type': 'application/json',
          // Aquí se podrían agregar las cabeceras de autenticación (ej. JWT)
          ...options.headers,
        },
      });

      if (!response.ok) {
        throw new Error(`Error en la solicitud: ${response.statusText}`);
      }

      const data = await response.json();
      setLoading(false);
      return data;
    } catch (err: any) {
      setError(err.message || 'Ocurrió un error inesperado.');
      setLoading(false);
      throw err;
    }
  }, []);

  return { loading, error, request };
};

export default useMiNegocioApi;
