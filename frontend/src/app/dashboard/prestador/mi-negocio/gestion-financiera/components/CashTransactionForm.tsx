// /app/dashboard/prestador/mi-negocio/gestion-financiera/components/CashTransactionForm.tsx
'use client';

import React from 'react';
import { useForm, Controller } from 'react-hook-form';
import { BankAccount, ChartOfAccount } from '../../../hooks/useMiNegocioApi';

interface CashTransactionFormProps {
  onSubmit: (data: any) => void;
  isLoading: boolean;
  bankAccounts: BankAccount[];
  chartOfAccounts: ChartOfAccount[];
}

const transactionTypes = [
  { value: 'DEPOSIT', label: 'Depósito / Ingreso' },
  { value: 'WITHDRAWAL', label: 'Retiro / Egreso' },
];

export default function CashTransactionForm({ onSubmit, isLoading, bankAccounts, chartOfAccounts }: CashTransactionFormProps) {
  const { register, handleSubmit, control, watch } = useForm();
  const generateJournalEntry = watch('generate_journal_entry');

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <Controller name="bank_account" control={control} rules={{ required: true }} render={({ field }) => (
        <select {...field} className="w-full border-gray-300 rounded-md">
            <option value="">Seleccione cuenta bancaria</option>
            {bankAccounts.map(b => <option key={b.id} value={b.id}>{b.bank_name} - {b.account_number}</option>)}
        </select>
      )}/>
      <Controller name="transaction_type" control={control} rules={{ required: true }} render={({ field }) => (
        <select {...field} className="w-full border-gray-300 rounded-md">
            {transactionTypes.map(t => <option key={t.value} value={t.value}>{t.label}</option>)}
        </select>
      )}/>
      <input type="number" step="0.01" {...register('amount', { required: true })} placeholder="Monto" className="w-full border-gray-300 rounded-md"/>
      <input type="date" {...register('date', { required: true })} className="w-full border-gray-300 rounded-md"/>
      <textarea {...register('description')} placeholder="Descripción" rows={3} className="w-full border-gray-300 rounded-md"/>

      <div className="p-4 border rounded-md space-y-3">
        <div className="flex items-center">
            <input type="checkbox" {...register('generate_journal_entry')} id="gen_je" className="h-4 w-4"/>
            <label htmlFor="gen_je" className="ml-2">Generar Asiento Contable</label>
        </div>
        {generateJournalEntry && (
            <div className="space-y-2">
                <Controller name="debit_account_number" control={control} rules={{ required: generateJournalEntry }} render={({ field }) => (
                    <select {...field} className="w-full border-gray-300 rounded-md">
                        <option value="">Seleccione cuenta a debitar</option>
                        {chartOfAccounts.map(a => <option key={a.id} value={a.account_number}>{a.account_number} - {a.name}</option>)}
                    </select>
                )}/>
                <Controller name="credit_account_number" control={control} rules={{ required: generateJournalEntry }} render={({ field }) => (
                     <select {...field} className="w-full border-gray-300 rounded-md">
                        <option value="">Seleccione cuenta a acreditar</option>
                        {chartOfAccounts.map(a => <option key={a.id} value={a.account_number}>{a.account_number} - {a.name}</option>)}
                    </select>
                )}/>
            </div>
        )}
      </div>

      <div className="flex justify-end pt-2">
        <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400">
            {isLoading ? 'Guardando...' : 'Guardar Transacción'}
        </button>
      </div>
    </form>
  );
}
