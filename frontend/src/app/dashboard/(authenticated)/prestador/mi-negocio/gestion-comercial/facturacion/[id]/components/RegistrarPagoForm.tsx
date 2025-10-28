// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/facturacion/[id]/components/RegistrarPagoForm.tsx
'use client';

import React from 'react';
import { useForm } from 'react-hook-form';

interface RegistrarPagoFormProps {
  onSubmit: (data: any) => void;
  isLoading: boolean;
}

export default function RegistrarPagoForm({ onSubmit, isLoading }: RegistrarPagoFormProps) {
  const { register, handleSubmit } = useForm();

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <input type="date" {...register('fecha_pago', { required: true })} className="w-full p-2 border rounded" />
      <input type="number" step="0.01" {...register('monto', { required: true, valueAsNumber: true })} placeholder="Monto" className="w-full p-2 border rounded" />
      <input type="text" {...register('metodo_pago')} placeholder="Método de Pago" className="w-full p-2 border rounded" />
      <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded">
        {isLoading ? 'Registrando...' : 'Registrar'}
      </button>
    </form>
  );
}
