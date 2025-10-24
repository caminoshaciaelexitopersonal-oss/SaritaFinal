'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import useMiNegocioApi from '../../../../../../../components/../../app/dashboard/prestador/mi-negocio/ganchos/useMiNegocioApi';
import { useAuth } from '@/contexts/AuthContext';
import { toast } from 'react-toastify';
import { FiUpload, FiTrash2, FiImage } from 'react-icons/fi';
import { AuthGuard } from '@/components/ui/AuthGuard';

interface ImagenGaleria {
  id: number;
  imagen: string;
  alt_text: string;
}

interface FormData {
  imagen: FileList;
  alt_text: string;
}

const GaleriaManager = () => {
  const [imagenes, setImagenes] = useState<ImagenGaleria[]>([]);
  const { request, loading: apiLoading } = useMiNegocioApi();
  const { register, handleSubmit, reset, formState: { isSubmitting } } = useForm<FormData>();

  const fetchImagenes = useCallback(async () => {
    try {
      const response = await request('/galeria/');
      setImagenes(response.results || response);
    } catch (error) {
      toast.error('No se pudieron cargar las imágenes de la galería.');
    }
  }, [request]);

  useEffect(() => {
    fetchImagenes();
  }, [fetchImagenes]);

  const onSubmit: SubmitHandler<FormData> = async (data) => {
    if (!data.imagen || data.imagen.length === 0) {
      toast.error('Por favor, selecciona una imagen para subir.');
      return;
    }

    const formData = new FormData();
    formData.append('imagen', data.imagen[0]);
    formData.append('alt_text', data.alt_text);

    try {
      await request('/galeria/', {
        method: 'POST',
        body: formData,
        headers: { 'Content-Type': undefined },
      });
      toast.success('¡Imagen subida con éxito!');
      reset();
      fetchImagenes();
    } catch (error) {
      toast.error('Ocurrió un error al subir la imagen.');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar esta imagen?')) {
      try {
        await request(`/galeria/${id}/`, { method: 'DELETE' });
        toast.success('Imagen eliminada con éxito.');
        fetchImagenes();
      } catch (error) {
        toast.error('No se pudo eliminar la imagen.');
      }
    }
  };

  if (apiLoading && imagenes.length === 0) {
    return <div>Cargando galería...</div>;
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <h1 className="text-3xl font-bold text-gray-800 mb-6">Gestionar Galería de Imágenes</h1>

      {/* --- Formulario de subida --- */}
      <form onSubmit={handleSubmit(onSubmit)} className="mb-8 p-4 border rounded-lg bg-gray-50">
        <h2 className="text-xl font-semibold mb-4">Subir Nueva Imagen</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
                <label htmlFor="imagen" className="block text-sm font-medium text-gray-700 mb-1">Archivo de Imagen</label>
                <input
                id="imagen"
                type="file"
                accept="image/*"
                {...register('imagen', { required: true })}
                className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
                />
            </div>
            <div>
                <label htmlFor="alt_text" className="block text-sm font-medium text-gray-700 mb-1">Texto Alternativo (Descripción)</label>
                <input
                id="alt_text"
                type="text"
                {...register('alt_text')}
                placeholder="Ej: Fachada del hotel con sol"
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                />
            </div>
        </div>
        <div className="mt-4">
            <button
                type="submit"
                disabled={isSubmitting}
                className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:bg-blue-300"
            >
                <FiUpload className="mr-2 -ml-1 h-5 w-5" />
                {isSubmitting ? 'Subiendo...' : 'Subir Imagen'}
            </button>
        </div>
      </form>

      {/* --- Galería de imágenes existentes --- */}
      <div>
        <h2 className="text-xl font-semibold mb-4">Imágenes Actuales</h2>
        {imagenes.length > 0 ? (
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
            {imagenes.map((img) => (
              <div key={img.id} className="relative group border rounded-lg overflow-hidden">
                <img src={img.imagen} alt={img.alt_text} className="h-48 w-full object-cover" />
                <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-50 transition-all duration-300 flex items-center justify-center">
                   <button
                    onClick={() => handleDelete(img.id)}
                    className="p-2 bg-red-600 text-white rounded-full opacity-0 group-hover:opacity-100 transform scale-50 group-hover:scale-100 transition-all duration-300"
                    aria-label="Eliminar imagen"
                   >
                     <FiTrash2 className="h-5 w-5" />
                   </button>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-10 px-4 border-2 border-dashed rounded-lg">
            <FiImage className="mx-auto h-12 w-12 text-gray-400" />
            <p className="mt-2 text-sm font-medium text-gray-600">Aún no has subido ninguna imagen a tu galería.</p>
          </div>
        )}
      </div>
    </div>
  );
};


const GaleriaPage = () => {
    return (
        <AuthGuard allowedRoles={['PRESTADOR']}>
            <GaleriaManager />
        </AuthGuard>
    )
}

export default GaleriaPage;