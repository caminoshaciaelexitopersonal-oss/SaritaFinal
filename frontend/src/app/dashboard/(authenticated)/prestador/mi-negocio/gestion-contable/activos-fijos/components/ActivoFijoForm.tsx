// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-contable/activos-fijos/components/ActivoFijoForm.tsx
'use client';

import React from 'react';
import { useForm } from 'react-hook-form';

interface ActivoFijoFormProps {
  onSubmit: (data: any) => void;
  isLoading: boolean;
}

export default function ActivoFijoForm({ onSubmit, isLoading }: ActivoFijoFormProps) {
  const { register, handleSubmit } = useForm();

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <input {...register('nombre', { required: true })} placeholder="Nombre del activo" className="w-full p-2 border rounded" />
      <input type="date" {...register('fecha_adquisicion', { required: true })} className="w-full p-2 border rounded" />
      <input type="number" step="0.01" {...register('costo_inicial', { required: true })} placeholder="Costo Inicial" className="w-full p-2 border rounded" />
      <input type="number" step="0.01" {...register('valor_residual')} placeholder="Valor Residual (Opcional)" className="w-full p-2 border rounded" />
      <input type="number" {...register('vida_util_meses', { required: true })} placeholder="Vida Útil (en meses)" className="w-full p-2 border rounded" />

      <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded">
        {isLoading ? 'Guardando...' : 'Guardar Activo'}
      </button>
    </form>
  );
}
