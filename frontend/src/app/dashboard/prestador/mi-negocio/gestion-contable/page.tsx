'use client';
import { useState, useEffect } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import api from '@/services/api';

interface CuentaContable {
  id: number;
  codigo: string;
  nombre: string;
  naturaleza: string;
}

export default function GestionContablePage() {
  const { user } = useAuth();
  const [cuentas, setCuentas] = useState<CuentaContable[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (user) {
      const fetchCuentas = async () => {
        try {
          const response = await api.get('/v1/mi-negocio/contable/plan-de-cuentas/');
          setCuentas(response.data.results);
        } catch (err) {
          setError('No se pudo cargar el plan de cuentas.');
        } finally {
          setIsLoading(false);
        }
      };
      fetchCuentas();
    }
  }, [user]);

  if (!user) {
    return <div>Debe iniciar sesión para ver este módulo.</div>;
  }

  if (isLoading) {
    return <div>Cargando Plan de Cuentas...</div>;
  }

  if (error) {
    return <div className="text-red-500">{error}</div>;
  }

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Gestión Contable - Plan de Cuentas</h1>
      <div className="bg-white p-4 rounded-lg shadow">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Código</th>
              <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
              <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Naturaleza</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {cuentas.length > 0 ? (
              cuentas.map((cuenta) => (
                <tr key={cuenta.id}>
                  <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{cuenta.codigo}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{cuenta.nombre}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{cuenta.naturaleza}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={3} className="px-6 py-4 text-center text-sm text-gray-500">
                  No se encontraron cuentas contables. Comience por crear su plan de cuentas.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
