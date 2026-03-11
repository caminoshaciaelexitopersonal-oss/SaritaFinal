import React from 'react';
import { WebLayout, KpiCard, LineChart, DataTable } from '@sarita/shared-ui';

export default function ProviderDashboardPage() {
  const kpis = [
    { title: 'Ventas del Mes', value: ',240', trend: '+5.4%' },
    { title: 'Reservas Activas', value: '12', trend: 'Estable' },
    { title: 'Comisiones', value: '50', trend: '-2.1%' }
  ];

  return (
    <WebLayout>
      <h1 className="text-3xl font-bold mb-10">Mi Negocio - Tablero Principal</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
        {kpis.map((k, i) => <KpiCard key={i} {...k} />)}
      </div>
      <div className="bg-white p-8 rounded-3xl shadow-sm border border-slate-100 mb-12">
        <h2 className="text-xl font-bold mb-6">Tendencia de Ingresos</h2>
        <LineChart data={[{name: 'Sem 1', v: 1200}, {name: 'Sem 2', v: 2400}]} dataKey="v" />
      </div>
      <DataTable
        columns={[{header: 'Cliente', accessor: 'c'}, {header: 'Total', accessor: 't'}]}
        data={[{c: 'John Doe', t: '5'}, {c: 'Jane Smith', t: '20'}]}
      />
    </WebLayout>
  );
}
