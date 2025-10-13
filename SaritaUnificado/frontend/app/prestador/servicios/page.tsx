"use client";

import React, { useState, useEffect, useCallback } from 'react';
import FormularioServicio from '../../../components/prestador/FormularioServicio';

interface Servicio {
  id: number;
  nombre: string;
  descripcion: string;
  precio: string;
}

const ServiciosPage = () => {
  const [servicios, setServicios] = useState<Servicio[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchServicios = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    const token = localStorage.getItem('access_token');
    if (!token) {
      setError("No estás autenticado. Por favor, inicia sesión.");
      setIsLoading(false);
      return;
    }

    try {
      const response = await fetch('/api/prestador/servicios/', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });

      if (!response.ok) {
        throw new Error('Error al obtener los servicios.');
      }

      const data = await response.json();
      setServicios(data.results || []);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchServicios();
  }, [fetchServicios]);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Gestión de Servicios</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div>
          <h2 className="text-xl font-semibold mb-4">Listado de Servicios</h2>
          {isLoading && <p>Cargando servicios...</p>}
          {error && <p className="text-red-500">{error}</p>}
          {!isLoading && !error && (
            <div className="overflow-x-auto">
              <table className="min-w-full bg-white">
                <thead>
                  <tr>
                    <th className="py-2 px-4 border-b">Nombre</th>
                    <th className="py-2 px-4 border-b">Precio</th>
                    <th className="py-2 px-4 border-b">Acciones</th>
                  </tr>
                </thead>
                <tbody>
                  {servicios.length > 0 ? (
                    servicios.map((servicio) => (
                      <tr key={servicio.id}>
                        <td className="py-2 px-4 border-b">{servicio.nombre}</td>
                        <td className="py-2 px-4 border-b">${parseFloat(servicio.precio).toFixed(2)}</td>
                        <td className="py-2 px-4 border-b">
                          <button className="text-blue-600 hover:underline mr-2">Editar</button>
                          <button className="text-red-600 hover:underline">Eliminar</button>
                        </td>
                      </tr>
                    ))
                  ) : (
                    <tr>
                      <td colSpan={3} className="py-4 px-4 text-center">No tienes servicios registrados.</td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          )}
        </div>
        <div>
          <FormularioServicio onServicioCreado={fetchServicios} />
        </div>
      </div>
    </div>
  );
};

export default ServiciosPage;