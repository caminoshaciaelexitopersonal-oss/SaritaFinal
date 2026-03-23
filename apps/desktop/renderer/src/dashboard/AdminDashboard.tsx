import React from 'react';
import { DesktopLayout, KpiCard, DataTable } from '@sarita/shared-ui';

export default function AdminDashboard() {
  return (
    <DesktopLayout>
      <h1 className="text-3xl font-bold mb-8 text-slate-800">Terminal de Control Regional</h1>
      <div className="grid grid-cols-4 gap-6 mb-10">
        <KpiCard title="Nodos Activos" value="124" />
        <KpiCard title="Transacciones" value="4,500" trend="+15%" />
        <KpiCard title="Alertas" value="3" />
        <KpiCard title="Gobernanza" value="OK" />
      </div>
      <div className="bg-white p-6 rounded-2xl shadow-lg border border-slate-200">
        <h2 className="text-xl font-bold mb-6">Auditoría de Sistemas</h2>
        <DataTable
          columns={[{header: 'Servicio', accessor: 's'}, {header: 'Latencia', accessor: 'l'}]}
          data={[{s: 'Core API', l: '45ms'}, {s: 'IA Engine', l: '120ms'}]}
        />
      </div>
    </DesktopLayout>
  );
}
