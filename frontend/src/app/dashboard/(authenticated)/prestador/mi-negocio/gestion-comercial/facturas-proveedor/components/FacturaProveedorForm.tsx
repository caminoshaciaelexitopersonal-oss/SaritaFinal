// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/facturas-proveedor/components/FacturaProveedorForm.tsx
'use client';

import React from 'react';
import { useForm, useFieldArray, Controller } from 'react-hook-form';
import { Proveedor } from '../../../../hooks/useMiNegocioApi';

interface FacturaProveedorFormProps {
  onSubmit: (data: any) => void;
  proveedores: Proveedor[];
  isLoading: boolean;
}

export default function FacturaProveedorForm({ onSubmit, proveedores, isLoading }: FacturaProveedorFormProps) {
  const { register, control, handleSubmit, formState: { errors } } = useForm();
  const { fields, append, remove } = useFieldArray({
    control,
    name: "items"
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <Controller
        name="proveedor"
        control={control}
        rules={{ required: 'Debe seleccionar un proveedor' }}
        render={({ field }) => (
          <select {...field} className="w-full p-2 border rounded">
            <option value="">-- Seleccione un Proveedor --</option>
            {proveedores.map(p => <option key={p.id} value={p.id}>{p.nombre}</option>)}
          </select>
        )}
      />
      {errors.proveedor && <p className="text-red-500">{errors.proveedor.message as string}</p>}

      <input type="date" {...register('fecha_emision', { required: true })} className="w-full p-2 border rounded" />
      <input type="date" {...register('fecha_vencimiento', { required: true })} className="w-full p-2 border rounded" />
      <input type="number" step="0.01" {...register('total', { required: true, valueAsNumber: true })} placeholder="Total Factura" className="w-full p-2 border rounded" />

      <h3 className="font-bold">Ítems</h3>
      {fields.map((item, index) => (
        <div key={item.id} className="flex gap-2 items-center">
          <input {...register(`items.${index}.descripcion`, { required: true })} placeholder="Descripción" className="p-2 border rounded flex-grow" />
          <input type="number" {...register(`items.${index}.cantidad`, { required: true, valueAsNumber: true })} placeholder="Cant." className="p-2 border rounded w-20" />
          <input type="number" step="0.01" {...register(`items.${index}.costo_unitario`, { required: true, valueAsNumber: true })} placeholder="Costo" className="p-2 border rounded w-24" />
          <button type="button" onClick={() => remove(index)} className="text-red-500">X</button>
        </div>
      ))}
      <button type="button" onClick={() => append({ descripcion: '', cantidad: 1, costo_unitario: 0 })} className="text-blue-500">
        + Añadir Ítem
      </button>

      <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded">
        {isLoading ? 'Guardando...' : 'Guardar Factura'}
      </button>
    </form>
  );
}
