'use client';

import React, { useEffect } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { toast } from 'react-toastify';
import { useAuth } from '@/contexts/AuthContext';
import { updatePrestadorProfile, PrestadorProfileData } from '@/services/api';

// Tipado para los datos del formulario, basado en el serializer PrestadorServicioUpdateSerializer
type PerfilFormInputs = {
  nombre_negocio: string;
  descripcion: string;
  telefono: string;
  email_contacto: string;
  red_social_facebook: string;
  red_social_instagram: string;
  red_social_tiktok: string;
  red_social_whatsapp: string;
  direccion: string;
  latitud: number | null;
  longitud: number | null;
  promociones_ofertas: string;
};

const Perfil = () => {
  const { user, isLoading, fetchUserData } = useAuth();

  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, errors },
  } = useForm<PerfilFormInputs>();

  useEffect(() => {
    if (user && user.perfil_prestador) {
      reset(user.perfil_prestador);
    }
  }, [user, reset]);

  const onSubmit: SubmitHandler<PerfilFormInputs> = async (data) => {
    try {
      // Limpiamos los campos que no se deben enviar o que son null
      const cleanData: PrestadorProfileData = Object.fromEntries(
        Object.entries(data).filter(([, value]) => value !== null && value !== undefined)
      );

      await updatePrestadorProfile(cleanData);
      await fetchUserData(); // Refrescar los datos del usuario en toda la app
      toast.success('¡Perfil actualizado con éxito!');
    } catch (err) {
      toast.error('Ocurrió un error al actualizar el perfil.');
    }
  };

  if (isLoading) {
    return <div>Cargando perfil...</div>;
  }

  if (!user || !user.perfil_prestador) {
    return <div>No se encontró un perfil de prestador.</div>;
  }

  const { perfil_prestador } = user;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Perfil del Prestador</h1>

      <div className="bg-gray-100 p-4 rounded-lg mb-6">
        <h2 className="text-xl font-semibold">Información General</h2>
        <p><strong>Categoría:</strong> {perfil_prestador.categoria?.nombre || 'No asignada'}</p>
        <p><strong>Estado:</strong> {perfil_prestador.aprobado ? 'Aprobado' : 'Pendiente de Aprobación'}</p>
      </div>

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Columna Izquierda */}
          <div className="space-y-4">
            <div>
              <label htmlFor="nombre_negocio" className="block text-sm font-medium text-gray-700">Nombre del Negocio</label>
              <input
                id="nombre_negocio"
                type="text"
                {...register('nombre_negocio', { required: 'El nombre es obligatorio' })}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
              {errors.nombre_negocio && <p className="text-red-500 text-xs mt-1">{errors.nombre_negocio.message}</p>}
            </div>

            <div>
              <label htmlFor="descripcion" className="block text-sm font-medium text-gray-700">Descripción</label>
              <textarea
                id="descripcion"
                rows={4}
                {...register('descripcion')}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>

            <div>
              <label htmlFor="telefono" className="block text-sm font-medium text-gray-700">Teléfono de Contacto</label>
              <input
                id="telefono"
                type="text"
                {...register('telefono')}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>

            <div>
              <label htmlFor="email_contacto" className="block text-sm font-medium text-gray-700">Email de Contacto</label>
              <input
                id="email_contacto"
                type="email"
                {...register('email_contacto', { pattern: { value: /^\S+@\S+$/i, message: 'Email inválido' } })}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
              {errors.email_contacto && <p className="text-red-500 text-xs mt-1">{errors.email_contacto.message}</p>}
            </div>
          </div>

          {/* Columna Derecha */}
          <div className="space-y-4">
            <div>
              <label htmlFor="red_social_facebook" className="block text-sm font-medium text-gray-700">Facebook URL</label>
              <input
                id="red_social_facebook"
                type="url"
                {...register('red_social_facebook')}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
             <div>
              <label htmlFor="red_social_instagram" className="block text-sm font-medium text-gray-700">Instagram URL</label>
              <input
                id="red_social_instagram"
                type="url"
                {...register('red_social_instagram')}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
             <div>
              <label htmlFor="red_social_tiktok" className="block text-sm font-medium text-gray-700">TikTok URL</label>
              <input
                id="red_social_tiktok"
                type="url"
                {...register('red_social_tiktok')}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
            <div>
              <label htmlFor="red_social_whatsapp" className="block text-sm font-medium text-gray-700">WhatsApp</label>
              <input
                id="red_social_whatsapp"
                type="text"
                {...register('red_social_whatsapp')}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
          </div>
        </div>

        {/* Sección de Ubicación */}
        <div className="border-t pt-6">
          <h2 className="text-xl font-semibold mb-4">Ubicación</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
              <label htmlFor="direccion" className="block text-sm font-medium text-gray-700">Dirección</label>
              <input
                id="direccion"
                type="text"
                {...register('direccion')}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
            <div>
              <label htmlFor="latitud" className="block text-sm font-medium text-gray-700">Latitud</label>
              <input
                id="latitud"
                type="number"
                step="any"
                {...register('latitud', { valueAsNumber: true })}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
            <div>
              <label htmlFor="longitud" className="block text-sm font-medium text-gray-700">Longitud</label>
              <input
                id="longitud"
                type="number"
                step="any"
                {...register('longitud', { valueAsNumber: true })}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
          </div>
        </div>

        {/* Sección de Promociones */}
        <div className="border-t pt-6">
           <label htmlFor="promociones_ofertas" className="block text-sm font-medium text-gray-700">Promociones y Ofertas</label>
            <textarea
                id="promociones_ofertas"
                rows={4}
                {...register('promociones_ofertas')}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
        </div>

        <div className="flex justify-end">
          <button
            type="submit"
            disabled={isSubmitting}
            className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
          >
            {isSubmitting ? 'Guardando...' : 'Guardar Cambios'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default Perfil;