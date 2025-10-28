// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-contable/activos-fijos/[id]/page.tsx
'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useParams } from 'next/navigation';
import { useMiNegocioApi, ActivoFijo, RegistroDepreciacion } from '../../../../../hooks/useMiNegocioApi';

export default function ActivoDetallePage() {
  const params = useParams();
  const { id } = params;
  const { getActivoFijo, getHistorialDepreciacion, isLoading } = useMiNegocioApi();

  const [activo, setActivo] = useState<ActivoFijo | null>(null);
  const [historial, setHistorial] = useState<RegistroDepreciacion[]>([]);

  const fetchData = useCallback(async () => {
    if (typeof id === 'string') {
      // Nota: getActivoFijo(id) no existe, pero debería. Simulamos su existencia.
      // const activoData = await getActivoFijo(parseInt(id, 10));
      // if (activoData) setActivo(activoData);

      const historialData = await getHistorialDepreciacion(parseInt(id, 10));
      if (historialData) setHistorial(historialData);
    }
  }, [id, getHistorialDepreciacion]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  if (isLoading) return <p>Cargando...</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold">Detalle de Activo: {activo?.nombre || '...'}</h1>
      {/* Aquí iría más info del activo */}

      <h2 className="text-xl font-bold mt-4">Historial de Depreciación</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left">Fecha</th>
              <th className="px-6 py-3 text-right">Monto Depreciado</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {historial.map((r) => (
              <tr key={r.id}>
                <td className="px-6 py-4">{r.fecha}</td>
                <td className="px-6 py-4 text-right">{r.monto}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
