// /app/dashboard/prestador/mi-negocio/gestion-contable/components/JournalEntryForm.tsx
'use client';

import React from 'react';
import { useForm, useFieldArray, Controller } from 'react-hook-form';
import { FiPlus, FiTrash2 } from 'react-icons/fi';
import { ChartOfAccount } from '../../../hooks/useMiNegocioApi';

interface JournalEntryFormProps {
  onSubmit: (data: any) => void;
  isLoading: boolean;
  accounts: ChartOfAccount[]; // Lista de cuentas para los selectores
}

type FormValues = {
  date: string;
  description: string;
  transactions_data: {
    account_number: string;
    debit: number;
    credit: number;
  }[];
};

export default function JournalEntryForm({ onSubmit, isLoading, accounts }: JournalEntryFormProps) {
  const { register, control, handleSubmit, watch, formState: { errors } } = useForm<FormValues>({
    defaultValues: {
      date: new Date().toISOString().split('T')[0],
      description: '',
      transactions_data: [
        { account_number: '', debit: 0, credit: 0 },
        { account_number: '', debit: 0, credit: 0 },
      ],
    },
  });

  const { fields, append, remove } = useFieldArray({
    control,
    name: "transactions_data",
  });

  const transactions = watch("transactions_data");
  const totalDebit = transactions.reduce((acc, current) => acc + (parseFloat(String(current.debit)) || 0), 0);
  const totalCredit = transactions.reduce((acc, current) => acc + (parseFloat(String(current.credit)) || 0), 0);
  const difference = totalDebit - totalCredit;

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div className="grid grid-cols-1 gap-6">
        <div>
          <label htmlFor="date" className="block text-sm font-medium text-gray-700">Fecha</label>
          <input type="date" {...register('date', { required: true })} className="mt-1 block w-full border-gray-300 rounded-md shadow-sm"/>
        </div>
        <div>
          <label htmlFor="description" className="block text-sm font-medium text-gray-700">Descripción</label>
          <textarea {...register('description', { required: true })} rows={3} className="mt-1 block w-full border-gray-300 rounded-md shadow-sm"></textarea>
        </div>
      </div>

      <div className="mt-6">
        <h3 className="text-lg font-medium">Transacciones</h3>
        <div className="mt-2 space-y-4">
          {fields.map((item, index) => (
            <div key={item.id} className="grid grid-cols-12 gap-x-4 items-center">
              <div className="col-span-5">
                <Controller
                  name={`transactions_data.${index}.account_number`}
                  control={control}
                  rules={{ required: true }}
                  render={({ field }) => (
                     <select {...field} className="block w-full border-gray-300 rounded-md shadow-sm">
                       <option value="">Seleccione cuenta</option>
                        {accounts.map(acc => <option key={acc.id} value={acc.account_number}>{acc.account_number} - {acc.name}</option>)}
                    </select>
                  )}
                />
              </div>
              <div className="col-span-3">
                 <input type="number" step="0.01" {...register(`transactions_data.${index}.debit`)} placeholder="Débito" className="block w-full border-gray-300 rounded-md shadow-sm text-right"/>
              </div>
              <div className="col-span-3">
                 <input type="number" step="0.01" {...register(`transactions_data.${index}.credit`)} placeholder="Crédito" className="block w-full border-gray-300 rounded-md shadow-sm text-right"/>
              </div>
              <div className="col-span-1">
                <button type="button" onClick={() => remove(index)} className="text-red-500 hover:text-red-700"><FiTrash2 /></button>
              </div>
            </div>
          ))}
        </div>
        <button type="button" onClick={() => append({ account_number: '', debit: 0, credit: 0 })} className="mt-2 text-blue-600 hover:text-blue-800 flex items-center text-sm">
          <FiPlus className="mr-1"/> Añadir Fila
        </button>
      </div>

      <div className="mt-6 border-t pt-4 flex justify-between items-center font-bold">
        <div>Totales:</div>
        <div className="grid grid-cols-2 gap-x-4 w-1/2">
            <div className="text-right">{totalDebit.toFixed(2)}</div>
            <div className="text-right">{totalCredit.toFixed(2)}</div>
        </div>
      </div>
       {difference !== 0 &&
            <div className="text-right text-red-600 font-semibold">
                Diferencia: {difference.toFixed(2)}
            </div>
        }

      <div className="flex justify-end mt-6">
        <button type="submit" disabled={isLoading || difference !== 0} className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400">
          {isLoading ? 'Guardando...' : 'Guardar Asiento'}
        </button>
      </div>
    </form>
  );
}
