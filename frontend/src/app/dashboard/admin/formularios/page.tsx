'use client';

import React, { useState, useEffect } from 'react';
import api from '@/services/api';
import { toast } from 'react-toastify';
import { FiFileText, FiPlus, FiEdit, FiTrash2 } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';
import Link from 'next/link';

// --- Tipos ---
interface Formulario {
  id: number;
  titulo: string;
  descripcion: string;
  es_publico: boolean;
}

const FormularioList = () => {
  const [formularios, setFormularios] = useState<Formulario[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchFormularios = async () => {
    setIsLoading(true);
    try {
      const response = await api.get('/api/formularios/');
      setFormularios(response.data.results || response.data);
    } catch (error) {
      toast.error('No se pudieron cargar los formularios.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchFormularios();
  }, []);

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar este formulario? Todas sus preguntas y respuestas se perderán.')) {
      try {
        await api.delete(`/api/formularios/${id}/`);
        toast.success('Formulario eliminado con éxito.');
        fetchFormularios();
      } catch (error) {
        toast.error('No se pudo eliminar el formulario.');
      }
    }
  };

  if (isLoading) {
    return <div>Cargando formularios...</div>;
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Gestionar Formularios Dinámicos</h1>
        <Link href="/dashboard/admin/formularios/builder">
          <button className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
            <FiPlus className="mr-2" />
            Crear Formulario
          </button>
        </Link>
      </div>

      <div className="space-y-4">
        {formularios.length > 0 ? formularios.map(form => (
          <div key={form.id} className="p-4 border rounded-lg flex items-center justify-between hover:bg-gray-50">
            <div>
              <h3 className="font-bold text-xl text-gray-800">{form.titulo}</h3>
              <p className="text-sm text-gray-600">{form.descripcion}</p>
            </div>
            <div className="flex items-center space-x-2">
              <span className={`px-2 py-1 text-xs font-semibold rounded-full ${form.es_publico ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}`}>
                {form.es_publico ? 'Público' : 'Privado'}
              </span>
              <Link href={`/dashboard/admin/formularios/builder?id=${form.id}`}>
                <button className="p-2 text-gray-500 hover:text-blue-600"><FiEdit /></button>
              </Link>
              <button onClick={() => handleDelete(form.id)} className="p-2 text-gray-500 hover:text-red-600"><FiTrash2 /></button>
            </div>
          </div>
        )) : (
          <div className="text-center py-10 px-4 border-2 border-dashed rounded-lg">
            <FiFileText className="mx-auto h-12 w-12 text-gray-400" />
            <p className="mt-2 text-sm font-medium text-gray-600">No has creado ningún formulario.</p>
          </div>
        )}
      </div>
    </div>
  );
};

const FormulariosPage = () => {
  return (
    <AuthGuard allowedRoles={['ADMIN', 'FUNCIONARIO_DIRECTIVO']}>
      <FormularioList />
    </AuthGuard>
  );
};

export default FormulariosPage;