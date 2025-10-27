// frontend/src/app/dashboard/prestador/mi-negocio/gestion-financiera/components/CashTransactionForm.tsx
'use client';
import React from 'react';
import { useForm } from 'react-hook-form';
// ... (código del formulario CashTransactionForm)
export default function CashTransactionForm({ onSubmit, isLoading, bankAccounts, chartOfAccounts }) {
  const { register, handleSubmit } = useForm();
  return <form onSubmit={handleSubmit(onSubmit)}>...</form>;
}
