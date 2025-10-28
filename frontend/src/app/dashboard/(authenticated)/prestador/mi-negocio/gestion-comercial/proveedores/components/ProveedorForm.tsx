// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/proveedores/components/ProveedorForm.tsx
'use client';

import React, { useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { Proveedor } from '../../../../hooks/useMiNegocioApi';

interface ProveedorFormProps {
  onSubmit: (data: Omit<Proveedor, 'id'>) => void;
  initialData?: Proveedor | null;
  isLoading: boolean;
}

export default function ProveedorForm({ onSubmit, initialData, isLoading }: ProveedorFormProps) {
  const { register, handleSubmit, reset, formState: { errors } } = useForm<Omit<Proveedor, 'id'>>();

  useEffect(() => {
    if (initialData) {
      reset(initialData);
    } else {
      reset({
        nombre: '',
        identificacion: '',
        email: '',
        telefono: '',
        direccion: '',
        is_active: true,
      });
    }
  }, [initialData, reset]);

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <input type="text" placeholder="Nombre" {...register('nombre', { required: 'El nombre es obligatorio' })} className="w-full p-2 border rounded" />
      {errors.nombre && <p className="text-red-500">{errors.nombre.message}</p>}

      <input type="text" placeholder="Identificación" {...register('identificacion')} className="w-full p-2 border rounded" />
      <input type="email" placeholder="Email" {...register('email')} className="w-full p-2 border rounded" />
      <input type="text" placeholder="Teléfono" {...register('telefono')} className="w-full p-2 border rounded" />
      <textarea placeholder="Dirección" {...register('direccion')} className="w-full p-2 border rounded" />

      <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:bg-gray-400">
        {isLoading ? 'Guardando...' : 'Guardar'}
      </button>
    </form>
  );
}
