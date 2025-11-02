'use client';
import { useState, useEffect } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import api from '@/services/api';

interface Producto {
  id: number;
  nombre: string;
  descripcion: string;
  precio: string;
}

export default function GestionComercialPage() {
  const { user } = useAuth();
  const [productos, setProductos] = useState<Producto[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (user) {
      const fetchProductos = async () => {
        try {
          const response = await api.get('/v1/mi-negocio/comercial/productos/');
          setProductos(response.data.results);
        } catch (err) {
          setError('No se pudo cargar la lista de productos.');
        } finally {
          setIsLoading(false);
        }
      };
      fetchProductos();
    }
  }, [user]);

  if (!user) {
    return <div>Debe iniciar sesión para ver este módulo.</div>;
  }

  if (isLoading) {
    return <div>Cargando Productos...</div>;
  }

  if (error) {
    return <div className="text-red-500">{error}</div>;
  }

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Gestión Comercial - Productos</h1>
      <div className="bg-white p-4 rounded-lg shadow">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
              <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Descripción</th>
              <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Precio</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {productos.length > 0 ? (
              productos.map((producto) => (
                <tr key={producto.id}>
                  <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{producto.nombre}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{producto.descripcion}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${producto.precio}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={3} className="px-6 py-4 text-center text-sm text-gray-500">
                  No tiene productos o servicios registrados.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
