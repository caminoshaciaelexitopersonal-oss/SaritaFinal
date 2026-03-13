import React, { useEffect, useState } from 'react';
import { DesktopLayout, KpiCard, DataTable } from '@sarita/shared-ui';
import { api } from '../services/api';

export const CouncilDashboard = () => {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    Promise.all([
      api.get('/v1/governance/plataforma/projects/'),
      api.get('/v1/public/consejo-consultivo/')
    ]).then(([proj, docs]) => {
      setData({
        projects_count: proj.data.count || 0,
        documents: docs.data.results || []
      });
    }).catch(err => {
      console.error("Council API Error", err);
    });
  }, []);

  return (
    <DesktopLayout>
      <h1 className="text-3xl font-bold mb-8 text-slate-800">Consejo Municipal de Turismo</h1>
      <div className="grid grid-cols-3 gap-6 mb-10">
        <KpiCard title="Proyectos en Revisión" value={data?.projects_count || '0'} />
        <KpiCard title="Sesiones Programadas" value="S/D" />
        <KpiCard title="Miembros Activos" value="S/D" />
      </div>
      <div className="bg-white p-6 rounded-2xl shadow-lg border border-slate-200">
        <h2 className="text-xl font-bold mb-6">Actas y Resoluciones</h2>
        <DataTable
          columns={[{header: 'Documento', accessor: 'titulo'}, {header: 'Fecha', accessor: 'fecha_publicacion'}]}
          data={data?.documents || []}
        />
      </div>
    </DesktopLayout>
  );
};
