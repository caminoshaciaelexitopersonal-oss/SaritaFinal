import React from 'react';
import { WebLayout, KpiCard, LineChart, DataTable } from '@sarita/shared-ui';

export default function AdminDashboardPage() {
  const stats = [
    { title: 'Ingresos Totales', value: '5,230', trend: '+12.5%' },
    { title: 'Nuevos Turistas', value: '1,240', trend: '+5.2%' },
    { title: 'Ocupación Regional', value: '78%', trend: '-2.1%' }
  ];

  const columns = [
    { header: 'Proveedor', accessor: 'name' },
    { header: 'Estado', accessor: 'status' },
    { header: 'Última Actividad', accessor: 'lastSeen' }
  ];

  const data = [
    { name: 'Hotel Central', status: 'Activo', lastSeen: '10 min ago' },
    { name: 'Restaurante El Llano', status: 'Inactivo', lastSeen: '2 days ago' }
  ];

  return (
    <WebLayout>
      <h1 className="text-3xl font-bold mb-8">Panel de Gobernanza</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        {stats.map((s, i) => <KpiCard key={i} {...s} />)}
      </div>
      <div className="bg-white p-6 rounded-xl shadow-sm mb-8">
        <h2 className="text-xl font-semibold mb-4">Crecimiento de Reservas</h2>
        <LineChart data={[{name: 'Ene', sales: 400}, {name: 'Feb', sales: 300}]} dataKey="sales" />
      </div>
      <DataTable columns={columns} data={data} />
    </WebLayout>
  );
}
