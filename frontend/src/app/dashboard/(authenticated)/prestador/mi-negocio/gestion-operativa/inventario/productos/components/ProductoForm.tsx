// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-operativa/inventario/productos/components/ProductoForm.tsx
'use client';

import React from 'react';
import { useForm } from 'react-hook-form';

interface ProductoFormProps {
  onSubmit: (data: any) => void;
  isLoading: boolean;
}

export default function ProductoForm({ onSubmit, isLoading }: ProductoFormProps) {
  const { register, handleSubmit } = useForm();

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <input type="text" placeholder="Nombre del Producto" {...register('nombre', { required: true })} className="w-full p-2 border rounded" />
      <textarea placeholder="Descripción" {...register('descripcion')} className="w-full p-2 border rounded" />
      <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded">
        {isLoading ? 'Creando...' : 'Crear Producto'}
      </button>
    </form>
  );
}
