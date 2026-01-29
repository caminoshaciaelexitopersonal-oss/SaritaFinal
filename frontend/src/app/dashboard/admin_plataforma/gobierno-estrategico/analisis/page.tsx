'use client';
import React from 'react';
import { useGovernanceApi } from '../hooks/useGovernanceApi';
import Spinner from '@/components/common/Spinner';

export default function ComparativeAnalysis() {
  const { comparative, isLoading } = useGovernanceApi();

  if (isLoading) return <Spinner />;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-gray-800 mb-6">Análisis Comparativo por Segmento</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {comparative?.by_type?.map((item: any, idx: number) => (
          <div key={idx} className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
            <h3 className="text-lg font-semibold text-blue-600 uppercase tracking-wide">{item.label}</h3>
            <div className="mt-4 flex justify-between items-end">
              <div>
                <p className="text-sm text-gray-500">Negocios Registrados</p>
                <p className="text-2xl font-bold">{item.count}</p>
              </div>
              <div className="text-right">
                <p className="text-sm text-gray-500">Ingresos Totales</p>
                <p className="text-xl font-bold text-green-600">$ {item.revenue?.toLocaleString()}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
