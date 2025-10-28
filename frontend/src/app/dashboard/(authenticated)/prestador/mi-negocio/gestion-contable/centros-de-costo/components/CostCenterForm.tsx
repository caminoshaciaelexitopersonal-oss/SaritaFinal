// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-contable/centros-de-costo/components/CostCenterForm.tsx
'use client';

import React, { useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { CostCenter } from '../../../../../hooks/useMiNegocioApi';

interface CostCenterFormProps {
  onSubmit: (data: Omit<CostCenter, 'id'>) => void;
  initialData?: CostCenter | null;
  isLoading: boolean;
}

export default function CostCenterForm({ onSubmit, initialData, isLoading }: CostCenterFormProps) {
  const { register, handleSubmit, reset, formState: { errors } } = useForm<Omit<CostCenter, 'id'>>();

  useEffect(() => {
    if (initialData) {
      reset(initialData);
    } else {
      reset({ code: '', name: '' });
    }
  }, [initialData, reset]);

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <input type="text" placeholder="Código" {...register('code', { required: 'El código es obligatorio' })} className="w-full p-2 border rounded" />
      {errors.code && <p className="text-red-500">{errors.code.message}</p>}

      <input type="text" placeholder="Nombre" {...register('name', { required: 'El nombre es obligatorio' })} className="w-full p-2 border rounded" />
      {errors.name && <p className="text-red-500">{errors.name.message}</p>}

      <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:bg-gray-400">
        {isLoading ? 'Guardando...' : 'Guardar'}
      </button>
    </form>
  );
}
