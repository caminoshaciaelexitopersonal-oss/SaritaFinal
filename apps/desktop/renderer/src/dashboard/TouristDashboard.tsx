import React, { useEffect, useState } from 'react';
import { DesktopLayout, KpiCard, DataTable } from '@sarita/shared-ui';
import { api } from '../services/api';

export const TouristDashboard = () => {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    api.get('/tourists/me/dashboard/').then(res => setData(res.data)).catch(() => {
      // Fallback a endpoints individuales si el unificado no existe
      Promise.all([
        api.get('/mi-viaje/'),
        api.get('/v1/turismo/tourism-reservations/')
      ]).then(([favs, resv]) => {
        setData({
          reservations_count: resv.data.count || 0,
          favorites_count: favs.data.count || 0,
          points: 0
        });
      });
    });
  }, []);

  return (
    <DesktopLayout>
      <h1 className="text-3xl font-bold mb-8 text-slate-800">Panel del Turista</h1>
      <div className="grid grid-cols-3 gap-6 mb-10">
        <KpiCard title="Mis Reservas" value={data?.reservations_count || '0'} />
        <KpiCard title="Favoritos" value={data?.favorites_count || '0'} />
        <KpiCard title="Puntos SARITA" value={data?.points || '0'} />
      </div>
      <div className="bg-white p-6 rounded-2xl shadow-lg border border-slate-200">
        <h2 className="text-xl font-bold mb-6">Próximas Experiencias</h2>
        {data?.next_experience ? (
           <p className="font-bold text-primary">{data.next_experience.name}</p>
        ) : (
           <p className="text-slate-500">No tienes experiencias programadas para hoy.</p>
        )}
      </div>
    </DesktopLayout>
  );
};
