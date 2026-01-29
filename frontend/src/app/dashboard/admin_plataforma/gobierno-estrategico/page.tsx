'use client';

import React from 'react';
import { useGovernanceApi } from './hooks/useGovernanceApi';
import { FiDollarSign, FiUsers, FiBox, FiTrendingUp, FiActivity } from 'react-icons/fi';
import Spinner from '@/components/common/Spinner';

export default function GovernanceDashboard() {
  const { summary, ranking, isLoading, isError } = useGovernanceApi();

  if (isLoading) return <Spinner />;
  if (isError) return <div className="p-4 text-red-500">Error cargando datos de gobernanza.</div>;

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold text-gray-800">Gobierno Estratégico - Dashboard Global</h1>

      {/* Resumen Ejecutivo */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          title="Ingresos Totales (SITYC)"
          value={`$${summary?.total_revenue?.toLocaleString()}`}
          icon={FiDollarSign}
          color="bg-green-500"
        />
        <StatCard
          title="Prestadores Activos"
          value={summary?.active_providers}
          icon={FiUsers}
          color="bg-blue-500"
        />
        <StatCard
          title="Catálogo Global"
          value={summary?.total_catalog_size}
          icon={FiBox}
          color="bg-purple-500"
        />
        <StatCard
          title="Ingreso Promedio / Negocio"
          value={`$${summary?.avg_revenue_per_provider?.toLocaleString()}`}
          icon={FiTrendingUp}
          color="bg-orange-500"
        />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">
        {/* Ranking de Top Performers */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
          <h2 className="text-lg font-semibold mb-4 flex items-center">
            <FiActivity className="mr-2" /> Top Performers (Facturación)
          </h2>
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead>
                <tr>
                  <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase">Prestador</th>
                  <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase">Tipo</th>
                  <th className="px-4 py-2 text-right text-xs font-medium text-gray-500 uppercase">Total Ingresos</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200">
                {ranking?.map((item: any, idx: number) => (
                  <tr key={idx}>
                    <td className="px-4 py-3 text-sm font-medium text-gray-900">{item.provider_name}</td>
                    <td className="px-4 py-3 text-sm text-gray-500">{item.type}</td>
                    <td className="px-4 py-3 text-sm text-right text-green-600 font-semibold">
                      ${item.revenue?.toLocaleString()}
                    </td>
                  </tr>
                ))}
                {(!ranking || ranking.length === 0) && (
                  <tr>
                    <td colSpan={3} className="px-4 py-4 text-center text-gray-400">Sin datos registrados</td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>

        {/* Sección Informativa de Gobernanza */}
        <div className="bg-blue-50 p-6 rounded-xl border border-blue-100">
          <h2 className="text-lg font-semibold text-blue-800 mb-4">Principios de Gobierno</h2>
          <ul className="space-y-3 text-sm text-blue-700">
            <li className="flex items-start">
              <span className="mr-2 font-bold">•</span>
              Supervisión consolidada sin intervención en la autonomía operativa de los prestadores.
            </li>
            <li className="flex items-start">
              <span className="mr-2 font-bold">•</span>
              Acceso a datos de facturación, inventario y ocupación en modo Solo Lectura.
            </li>
            <li className="flex items-start">
              <span className="mr-2 font-bold">•</span>
              Identificación proactiva de riesgos y anomalías en el ecosistema.
            </li>
            <li className="flex items-start">
              <span className="mr-2 font-bold">•</span>
              Normalización de indicadores para permitir comparabilidad regional y sectorial.
            </li>
          </ul>
          <div className="mt-6">
            <button className="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-700 transition-colors">
              Generar Reporte Consolidado
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

function StatCard({ title, value, icon: Icon, color }: any) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center">
      <div className={`p-3 rounded-lg ${color} text-white mr-4`}>
        <Icon size={24} />
      </div>
      <div>
        <p className="text-sm text-gray-500 font-medium uppercase">{title}</p>
        <p className="text-2xl font-bold text-gray-900">{value}</p>
      </div>
    </div>
  );
}
