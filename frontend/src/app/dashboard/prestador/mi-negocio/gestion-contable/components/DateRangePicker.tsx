// frontend/src/app/dashboard/prestador/mi-negocio/gestion-contable/components/DateRangePicker.tsx
'use client';
import React from 'react';
export default function DateRangePicker({ onSubmit, isLoading }) {
  const today = new Date().toISOString().split('T')[0];
  return (
    <form onSubmit={onSubmit} className="flex items-center gap-4 p-4 bg-gray-50 rounded-lg">
      <input type="date" name="start_date" defaultValue={`${new Date().getFullYear()}-01-01`} className="border-gray-300 rounded-md"/>
      <input type="date" name="end_date" defaultValue={today} className="border-gray-300 rounded-md"/>
      <button type="submit" disabled={isLoading} className="px-4 py-2 bg-blue-600 text-white rounded-md disabled:bg-gray-400">
        {isLoading ? 'Generando...' : 'Generar Informe'}
      </button>
    </form>
  );
}
