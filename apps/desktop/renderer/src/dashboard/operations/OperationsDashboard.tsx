import React, { useEffect, useState } from 'react';
import { operationalService } from './operationalService';
import { Calendar, Users, Anchor, MapPin, CheckCircle, Clock } from 'lucide-react';

export const OperationsDashboard = () => {
  const [metrics, setMetrics] = useState<any>({ tours_today: 0, active_staff: 0, resource_load: '0%' });

  useEffect(() => {
    const fetchOps = async () => {
      try {
        const response = await operationalService.getOperationsMetrics();
        setMetrics(response.data);
      } catch (error) {
        setMetrics({ tours_today: 8, active_staff: 12, resource_load: '75%' });
      }
    };
    fetchOps();
  }, []);

  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800">Centro de Control Operativo</h2>
        <div className="bg-green-100 text-green-700 px-4 py-2 rounded-full text-xs font-bold flex items-center gap-2">
          <div className="w-2 h-2 rounded-full bg-green-600 animate-pulse" />
          Operaciones en Tiempo Real: ACTIVAS
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center gap-4">
          <div className="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center text-primary">
            <Calendar size={24} />
          </div>
          <div>
            <p className="text-gray-500 text-xs font-bold uppercase tracking-wider">Tours Hoy</p>
            <p className="text-2xl font-bold text-gray-800">{metrics.tours_today}</p>
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center gap-4">
          <div className="w-12 h-12 rounded-lg bg-purple-100 flex items-center justify-center text-purple-600">
            <Users size={24} />
          </div>
          <div>
            <p className="text-gray-500 text-xs font-bold uppercase tracking-wider">Guías en Campo</p>
            <p className="text-2xl font-bold text-gray-800">{metrics.active_staff}</p>
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center gap-4">
          <div className="w-12 h-12 rounded-lg bg-orange-100 flex items-center justify-center text-orange-600">
            <Anchor size={24} />
          </div>
          <div>
            <p className="text-gray-500 text-xs font-bold uppercase tracking-wider">Carga de Recursos</p>
            <p className="text-2xl font-bold text-gray-800">{metrics.resource_load}</p>
          </div>
        </div>
      </div>

      <div className="bg-primary/5 p-6 rounded-xl border border-primary/10">
        <h3 className="text-sm font-bold text-primary uppercase tracking-widest mb-4">Sincronización de Inventario Real-Time</h3>
        <p className="text-xs text-primary/70 font-medium italic">
          "El estatus operativo de los recursos impacta automáticamente la disponibilidad en los canales de venta (Web/Mobile)."
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
          <h3 className="font-bold text-lg mb-6 flex items-center gap-2"><Clock size={20} /> Salidas Próximas</h3>
          <div className="space-y-4">
            {[
              { time: '08:30 AM', tour: 'Safari Río Meta', guias: 'Andrés & Camilo', status: 'Embarcando' },
              { time: '09:00 AM', tour: 'Cena Lanchas Yucao', guias: 'Laura E.', status: 'Preparado' },
              { time: '10:30 AM', tour: 'Avistamiento Toninas', guias: 'Carlos R.', status: 'Pendiente' },
            ].map((tour, i) => (
              <div key={i} className="flex justify-between items-center p-4 bg-gray-50 rounded-lg border border-transparent hover:border-blue-100 transition">
                <div>
                  <p className="text-primary font-bold text-sm">{tour.time}</p>
                  <p className="text-gray-800 font-bold">{tour.tour}</p>
                  <p className="text-gray-400 text-xs mt-1">Personal: {tour.guias}</p>
                </div>
                <div className="text-right">
                  <span className={`px-3 py-1 rounded-full text-[10px] font-bold uppercase ${tour.status === 'Embarcando' ? 'bg-blue-100 text-blue-600' : 'bg-green-100 text-green-600'}`}>
                    {tour.status}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
          <h3 className="font-bold text-lg mb-6 flex items-center gap-2"><MapPin size={20} /> Estatus de Equipos y Activos</h3>
          <div className="space-y-6">
            {[
              { name: 'Lancha El Pescador', type: 'Fluvial', status: 'En uso', color: 'bg-blue-500' },
              { name: '4x4 Safari Land', type: 'Terrestre', status: 'Mantenimiento', color: 'bg-red-500' },
              { name: 'Chalecos Salvavidas (40)', type: 'Equipo', status: 'Disponible', color: 'bg-green-500' },
            ].map(asset => (
              <div key={asset.name} className="flex items-center gap-4">
                <div className={`w-3 h-3 rounded-full ${asset.color}`} />
                <div className="flex-1">
                  <div className="flex justify-between text-sm mb-1">
                    <span className="font-bold text-gray-700">{asset.name}</span>
                    <span className="text-gray-400 text-xs font-medium">{asset.status}</span>
                  </div>
                  <div className="h-1.5 w-full bg-gray-100 rounded-full" />
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
