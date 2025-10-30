// frontend/src/app/dashboard/prestador/mi-negocio/gestion-financiera/components/BankAccountForm.tsx
'use client';
import React from 'react';
import { useForm } from 'react-hook-form';
// ... (código del formulario BankAccountForm)
export default function BankAccountForm({ onSubmit, initialData, isLoading, currencies }) {
  const { register, handleSubmit } = useForm({ defaultValues: initialData });
  return <form onSubmit={handleSubmit(onSubmit)}>...</form>;
}
