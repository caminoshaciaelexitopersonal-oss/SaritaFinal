// frontend/src/app/dashboard/prestador/mi-negocio/hooks/useMiNegocioApi.ts
import { useAuth } from '@/contexts/AuthContext';
import api from '@/services/api';
import { useCallback, useState } from 'react';
import { toast } from 'sonner';

// --- Interfaces de Nómina ---
export interface Empleado {
  id: number;
  nombre: string;
  apellido: string;
  tipo_documento: 'CC' | 'CE' | 'PA';
  numero_documento: string;
  fecha_nacimiento: string;
  fecha_contratacion: string;
  salario_base: string;
  activo: boolean;
}
export type CreateEmpleadoDTO = Omit<Empleado, 'id'>;
export interface ConceptoNomina {
  id: number;
  codigo: string;
  descripcion: string;
  tipo: 'ingreso' | 'deduccion';
  es_fijo: boolean;
  valor: string;
}
export interface DetalleNomina {
  id: number;
  concepto: ConceptoNomina;
  valor_calculado: string;
}
export interface Nomina {
  id: number;
  fecha_inicio: string;
  fecha_fin: string;
  estado: 'borrador' | 'procesada' | 'pagada';
  total_ingresos: string;
  total_deducciones: string;
  neto_a_pagar: string;
  detalles: DetalleNomina[];
}

export function useMiNegocioApi() {
  const { user } = useAuth();
  const [loading, setLoading] = useState(false);

  const makeRequest = useCallback(async <T>(request: () => Promise<T>, successMessage?: string): Promise<T | null> => {
    if (!user) {
      toast.error("Error de autenticación", { description: "No se encontró un usuario válido." });
      return null;
    }
    setLoading(true);
    try {
      const data = await request();
      if (successMessage) {
        toast.success(successMessage);
      }
      return data;
    } catch (error: any) {
      const errorMessage = error.response?.data?.error || error.message || "Ocurrió un error desconocido.";
      toast.error("Error en la solicitud", { description: errorMessage });
      return null;
    } finally {
      setLoading(false);
    }
  }, [user]);

  // --- APIs de Nómina ---
  const getEmpleados = useCallback(async () => {
    return makeRequest(() => api.get<Empleado[]>('/api/v1/mi-negocio/nomina/empleados/').then(res => res.data));
  }, [makeRequest]);

  const createEmpleado = useCallback(async (data: CreateEmpleadoDTO) => {
    return makeRequest(() => api.post<Empleado>('/api/v1/mi-negocio/nomina/empleados/', data).then(res => res.data), "Empleado creado.");
  }, [makeRequest]);

  const procesarNomina = useCallback(async (fecha_inicio: string, fecha_fin: string) => {
    return makeRequest(() => api.post<Nomina>('/api/v1/mi-negocio/nomina/nominas/procesar/', { fecha_inicio, fecha_fin }).then(res => res.data), "Nómina procesada.");
  }, [makeRequest]);

  const getNominas = useCallback(async () => {
    return makeRequest(() => api.get<Nomina[]>('/api/v1/mi-negocio/nomina/nominas/').then(res => res.data));
  }, [makeRequest]);

  return {
    loading,
    getEmpleados,
    createEmpleado,
    procesarNomina,
    getNominas,
  };
}
