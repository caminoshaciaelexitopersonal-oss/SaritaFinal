// /app/dashboard/prestador/mi-negocio/gestion-contable/components/ChartOfAccountForm.tsx
'use client';

import React, { useState, useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { ChartOfAccount } from '../../../hooks/useMiNegocioApi';

interface ChartOfAccountFormProps {
  onSubmit: (data: any) => void;
  initialData?: ChartOfAccount | null;
  isLoading: boolean;
}

const accountTypes = [
  { value: 'ASSET', label: 'Activo' },
  { value: 'LIABILITY', label: 'Pasivo' },
  { value: 'EQUITY', label: 'Patrimonio' },
  { value: 'REVENUE', label: 'Ingreso' },
  { value: 'EXPENSE', label: 'Gasto' },
];

export default function ChartOfAccountForm({ onSubmit, initialData, isLoading }: ChartOfAccountFormProps) {
  const { register, handleSubmit, control, reset, formState: { errors } } = useForm<Omit<ChartOfAccount, 'id'>>({
    defaultValues: initialData || {
      account_number: '',
      name: '',
      account_type: 'ASSET',
      is_active: true,
      parent: null,
    }
  });

  useEffect(() => {
    if (initialData) {
      reset(initialData);
    }
  }, [initialData, reset]);

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div>
        <label htmlFor="account_number" className="block text-sm font-medium text-gray-700">Número de Cuenta</label>
        <input
          id="account_number"
          type="text"
          {...register('account_number', { required: 'Este campo es obligatorio' })}
          className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        />
        {errors.account_number && <p className="text-red-500 text-xs mt-1">{errors.account_number.message}</p>}
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
        <label htmlFor="account_type" className="block text-sm font-medium text-gray-700">Tipo de Cuenta</label>
        <Controller
          name="account_type"
          control={control}
          render={({ field }) => (
            <select {...field} id="account_type" className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500">
              {accountTypes.map(type => (
                <option key={type.value} value={type.value}>{type.label}</option>
              ))}
            </select>
          )}
        />
      </div>

      <div className="flex items-center">
        <input
          id="is_active"
          type="checkbox"
          {...register('is_active')}
          className="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
        />
        <label htmlFor="is_active" className="ml-2 block text-sm text-gray-900">Activa</label>
      </div>

      <div className="flex justify-end pt-4">
        <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400">
          {isLoading ? 'Guardando...' : 'Guardar'}
        </button>
      </div>
    </form>
  );
}
