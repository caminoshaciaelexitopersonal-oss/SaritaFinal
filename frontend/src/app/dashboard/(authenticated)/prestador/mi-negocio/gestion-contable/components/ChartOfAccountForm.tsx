// /app/dashboard/prestador/mi-negocio/gestion-contable/components/ChartOfAccountForm.tsx
'use client';

import React, { useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { ChartOfAccount } from '../../../hooks/useMiNegocioApi';

interface ChartOfAccountFormProps {
  onSubmit: (data: any) => void;
  initialData?: ChartOfAccount | null;
  isLoading: boolean;
}

const natureTypes = [
  { value: 'DEBITO', label: 'Débito' },
  { value: 'CREDITO', label: 'Crédito' },
];

export default function ChartOfAccountForm({ onSubmit, initialData, isLoading }: ChartOfAccountFormProps) {
  const { register, handleSubmit, control, reset, formState: { errors } } = useForm<Omit<ChartOfAccount, 'id'>>({
    defaultValues: initialData || {
      code: '',
      name: '',
      nature: 'DEBITO',
      allows_transactions: true,
    }
  });

  useEffect(() => {
    if (initialData) {
      reset(initialData);
    } else {
      reset({
        code: '',
        name: '',
        nature: 'DEBITO',
        allows_transactions: true,
      });
    }
  }, [initialData, reset]);

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div>
        <label htmlFor="code" className="block text-sm font-medium text-gray-700">Código de Cuenta</label>
        <input
          id="code"
          type="text"
          {...register('code', { required: 'Este campo es obligatorio' })}
          className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        />
        {errors.code && <p className="text-red-500 text-xs mt-1">{errors.code.message}</p>}
      </div>

      <div>
        <label htmlFor="name" className="block text-sm font-medium text-gray-700">Nombre de la Cuenta</label>
        <input
          id="name"
          type="text"
          {...register('name', { required: 'Este campo es obligatorio' })}
          className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        />
        {errors.name && <p className="text-red-500 text-xs mt-1">{errors.name.message}</p>}
      </div>

      <div>
        <label htmlFor="nature" className="block text-sm font-medium text-gray-700">Naturaleza de la Cuenta</label>
        <Controller
          name="nature"
          control={control}
          render={({ field }) => (
            <select {...field} id="nature" className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500">
              {natureTypes.map(type => (
                <option key={type.value} value={type.value}>{type.label}</option>
              ))}
            </select>
          )}
        />
      </div>

      <div className="flex items-center">
        <input
          id="allows_transactions"
          type="checkbox"
          {...register('allows_transactions')}
          className="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
        />
        <label htmlFor="allows_transactions" className="ml-2 block text-sm text-gray-900">Permite Transacciones (Cuenta Auxiliar)</label>
      </div>

      <div className="flex justify-end pt-4">
        <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400">
          {isLoading ? 'Guardando...' : 'Guardar'}
        </button>
      </div>
    </form>
  );
}
