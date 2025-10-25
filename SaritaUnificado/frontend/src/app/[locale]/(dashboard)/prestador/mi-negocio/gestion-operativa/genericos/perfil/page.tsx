// src/app/[locale]/(dashboard)/prestador/mi-negocio/gestion-operativa/genericos/perfil/page.tsx
'use client';

import { useState, useEffect } from 'react';
import { useMiNegocioApi } from '../../../hooks/useMiNegocioApi';

// Tipo de datos del perfil, debe coincidir con el del hook y la API
interface PerfilData {
  nombre_comercial: string;
  telefono_principal: string;
  email_comercial: string;
  direccion: string;
  descripcion_corta: string;
}

export default function PerfilPage() {
  const [perfil, setPerfil] = useState<Partial<PerfilData>>({});
  const { isLoading, error, getPerfil, updatePerfil } = useMiNegocioApi();

  useEffect(() => {
    const loadPerfil = async () => {
      const data = await getPerfil();
      if (data) {
        setPerfil(data);
      }
    };
    loadPerfil();
  }, [getPerfil]);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setPerfil({ ...perfil, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await updatePerfil(perfil);
  };

  if (isLoading && !perfil.nombre_comercial) { // Muestra 'Cargando' solo en la carga inicial
    return <div className="p-6 text-center">Cargando perfil...</div>;
  }

  if (error && !perfil.nombre_comercial) {
    return <div className="p-6 text-red-500 text-center">Error: {error}</div>;
  }

  return (
    <div className="p-4 sm:p-6 md:p-8">
      <h1 className="text-2xl font-bold text-gray-800 mb-6">Gestionar Mi Perfil</h1>
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md space-y-6">
        <div>
          <label htmlFor="nombre_comercial" className="block text-sm font-medium text-gray-700">Nombre Comercial</label>
          <input
            type="text"
            name="nombre_comercial"
            id="nombre_comercial"
            value={perfil?.nombre_comercial || ''}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          />
        </div>

        <div>
          <label htmlFor="telefono_principal" className="block text-sm font-medium text-gray-700">Teléfono</label>
          <input
            type="text"
            name="telefono_principal"
            id="telefono_principal"
            value={perfil?.telefono_principal || ''}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          />
        </div>

        <div>
          <label htmlFor="email_comercial" className="block text-sm font-medium text-gray-700">Email Comercial</label>
          <input
            type="email"
            name="email_comercial"
            id="email_comercial"
            value={perfil?.email_comercial || ''}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          />
        </div>

        <div>
          <label htmlFor="direccion" className="block text-sm font-medium text-gray-700">Dirección</label>
          <input
            type="text"
            name="direccion"
            id="direccion"
            value={perfil?.direccion || ''}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          />
        </div>

        <div>
          <label htmlFor="descripcion_corta" className="block text-sm font-medium text-gray-700">Descripción Corta</label>
          <textarea
            name="descripcion_corta"
            id="descripcion_corta"
            value={perfil?.descripcion_corta || ''}
            onChange={handleInputChange}
            rows={4}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          />
        </div>

        <div className="flex justify-end">
          <button
            type="submit"
            disabled={isLoading}
            className="px-4 py-2 bg-blue-600 text-white font-medium rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:bg-blue-400"
          >
            {isLoading ? 'Guardando...' : 'Guardar Cambios'}
          </button>
        </div>
      </form>
    </div>
  );
}
