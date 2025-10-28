// frontend/src/app/dashboard/(authenticated)/prestador/mi-negocio/gestion-comercial/facturas-proveedor/components/FacturaProveedorForm.tsx
'use client';

import React from 'react';
import { useForm, useFieldArray, Controller } from 'react-hook-form';
import { Proveedor, CostCenter } from '../../../../hooks/useMiNegocioApi';

interface FacturaProveedorFormProps {
  onSubmit: (data: any) => void;
  proveedores: Proveedor[];
  costCenters: CostCenter[];
  isLoading: boolean;
}

export default function FacturaProveedorForm({ onSubmit, proveedores, costCenters, isLoading }: FacturaProveedorFormProps) {
  const { register, control, handleSubmit, formState: { errors } } = useForm();
  const { fields, append, remove } = useFieldArray({ control, name: "items" });

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <Controller name="proveedor" control={control} rules={{ required: true }} render={({ field }) => (
        <select {...field} className="w-full p-2 border rounded">
          <option value="">-- Seleccione Proveedor --</option>
          {proveedores.map(p => <option key={p.id} value={p.id}>{p.nombre}</option>)}
        </select>
      )} />

      <Controller name="centro_costo" control={control} render={({ field }) => (
        <select {...field} className="w-full p-2 border rounded">
          <option value="">-- Sin Centro de Costo --</option>
          {costCenters.map(cc => <option key={cc.id} value={cc.id}>{cc.name}</option>)}
        </select>
      )} />

      <input type="date" {...register('fecha_emision', { required: true })} className="w-full p-2 border rounded" />
      <input type="date" {...register('fecha_vencimiento', { required: true })} className="w-full p-2 border rounded" />
      <input type="number" step="0.01" {...register('total', { required: true })} placeholder="Total Factura" className="w-full p-2 border rounded" />

      <h3 className="font-bold">Ítems</h3>
      {fields.map((item, index) => (
        <div key={item.id} className="flex gap-2 items-center">
          <input {...register(`items.${index}.descripcion`)} placeholder="Descripción" className="p-2 border rounded flex-grow" />
          <input type="number" {...register(`items.${index}.cantidad`)} placeholder="Cant." className="p-2 border rounded w-20" />
          <input type="number" step="0.01" {...register(`items.${index}.costo_unitario`)} placeholder="Costo" className="p-2 border rounded w-24" />
          <button type="button" onClick={() => remove(index)} className="text-red-500">X</button>
        </div>
      ))}
      <button type="button" onClick={() => append({})} className="text-blue-500">+ Añadir Ítem</button>

      <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded">
        Guardar Factura
      </button>
    </form>
  );
}
