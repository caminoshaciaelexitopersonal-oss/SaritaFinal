// /app/dashboard/prestador/mi-negocio/gestion-financiera/components/BankAccountForm.tsx
'use client';

import React from 'react';
import { useForm, Controller } from 'react-hook-form';
import { BankAccount } from '../../../hooks/useMiNegocioApi';

interface BankAccountFormProps {
  onSubmit: (data: any) => void;
  initialData?: BankAccount | null;
  isLoading: boolean;
  currencies: { code: string; name: string }[];
}

const accountTypes = [
  { value: 'SAVINGS', label: 'Ahorros' },
  { value: 'CHECKING', label: 'Corriente' },
];

export default function BankAccountForm({ onSubmit, initialData, isLoading, currencies }: BankAccountFormProps) {
  const { register, handleSubmit, control, formState: { errors } } = useForm({
    defaultValues: initialData || {
      bank_name: '',
      account_number: '',
      account_holder: '',
      account_type: 'SAVINGS',
      currency_code: 'COP',
      is_active: true,
    }
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700">Nombre del Banco</label>
        <input {...register('bank_name', { required: true })} className="mt-1 block w-full border-gray-300 rounded-md shadow-sm"/>
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">Número de Cuenta</label>
        <input {...register('account_number', { required: true })} className="mt-1 block w-full border-gray-300 rounded-md shadow-sm"/>
      </div>
       <div>
        <label className="block text-sm font-medium text-gray-700">Titular de la Cuenta</label>
        <input {...register('account_holder', { required: true })} className="mt-1 block w-full border-gray-300 rounded-md shadow-sm"/>
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">Tipo de Cuenta</label>
        <Controller name="account_type" control={control} render={({ field }) => (
            <select {...field} className="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
              {accountTypes.map(t => <option key={t.value} value={t.value}>{t.label}</option>)}
            </select>
        )}/>
      </div>
       <div>
        <label className="block text-sm font-medium text-gray-700">Moneda</label>
        <Controller name="currency_code" control={control} render={({ field }) => (
            <select {...field} className="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
              {currencies.map(c => <option key={c.code} value={c.code}>{c.name}</option>)}
            </select>
        )}/>
      </div>
      <div className="flex items-center">
        <input type="checkbox" {...register('is_active')} className="h-4 w-4 text-blue-600 border-gray-300 rounded"/>
        <label className="ml-2 block text-sm text-gray-900">Activa</label>
      </div>
      <div className="flex justify-end pt-4">
        <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400">
          {isLoading ? 'Guardando...' : 'Guardar'}
        </button>
      </div>
    </form>
  );
}
