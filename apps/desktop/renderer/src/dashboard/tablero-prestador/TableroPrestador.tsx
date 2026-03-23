import React, { useEffect, useState } from 'react';
import { businessService } from '../../services/businessService';
import { Card } from '../../components/Card';

export const TableroPrestador = () => {
  const [stats, setStats] = useState<any>(null);

  useEffect(() => {
    businessService.getOperativaDashboard()
      .then(res => setStats(res.data))
      .catch(console.error);
  }, []);

  return (
    <div className="p-8 space-y-8 bg-slate-50 min-h-screen">
      <div>
         <h1 className="text-3xl font-black text-emerald-900 tracking-tight italic">Tablero ERP Mi Negocio</h1>
         <p className="text-slate-500 font-bold uppercase text-xs tracking-widest mt-1">Operativa Turística Unificada</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
         <Card className="p-6 bg-white border-b-4 border-b-emerald-500 shadow-sm">
            <p className="text-xs font-black text-slate-400 uppercase">Reservas Hoy</p>
            <p className="text-3xl font-black text-slate-800">{stats?.total_reservas || 0}</p>
         </Card>
         <Card className="p-6 bg-white border-b-4 border-b-blue-500 shadow-sm">
            <p className="text-xs font-black text-slate-400 uppercase">Ventas Brutas</p>
            <p className="text-3xl font-black text-slate-800">${stats?.total_ventas?.toLocaleString() || 0}</p>
         </Card>
         <Card className="p-6 bg-white border-b-4 border-b-indigo-500 shadow-sm">
            <p className="text-xs font-black text-slate-400 uppercase">Disponibilidad</p>
            <p className="text-3xl font-black text-slate-800">{stats?.disponibilidad_media || '100'}%</p>
         </Card>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
         <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
            <h3 className="font-black text-slate-800 mb-4 uppercase text-sm tracking-wider">Próximas Reservas</h3>
            <div className="space-y-4">
               {/* List of real reservations would go here */}
               <p className="text-slate-400 italic text-sm">Cargando flujo transaccional...</p>
            </div>
         </div>
         <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
            <h3 className="font-black text-slate-800 mb-4 uppercase text-sm tracking-wider">Alertas SG-SST</h3>
            <div className="p-4 bg-amber-50 rounded-xl border border-amber-100">
               <p className="text-amber-800 font-bold text-sm">Pendiente: Renovación de extintores (Nodo Central)</p>
            </div>
         </div>
      </div>
    </div>
  );
}

export const TableroPrestadorStub = TableroPrestador;
