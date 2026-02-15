'use client';

import React, { useEffect, useState } from 'react';
import { useMiNegocioApi } from '../hooks/useMiNegocioApi';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import {
  FiDollarSign,
  FiTrendingUp,
  FiAlertCircle,
  FiPieChart,
  FiArrowUpRight,
  FiArrowDownRight,
  FiActivity
} from 'react-icons/fi';
import { Button } from '@/components/ui/Button';

export default function FinanzasDashboard() {
  const { getTesoreria, getIndicadores, isLoading } = useMiNegocioApi();
  const [data, setData] = useState<any>(null);
  const [indicadores, setIndicadores] = useState<any[]>([]);

  useEffect(() => {
    const load = async () => {
      const [t, ind] = await Promise.all([getTesoreria(), getIndicadores()]);
      if (t) setData(t[0]);
      if (ind) setIndicadores(ind);
    };
    load();
  }, [getTesoreria, getIndicadores]);

  const kpis = [
    { label: 'Liquidez Corriente', value: '1.45', icon: FiActivity, color: 'text-blue-600', trend: '+5%' },
    { label: 'Margen EBITDA', value: '28%', icon: FiTrendingUp, color: 'text-green-600', trend: '+2%' },
    { label: 'Endeudamiento', value: '0.35', icon: FiAlertCircle, color: 'text-amber-600', trend: '-1%' },
    { label: 'Rentabilidad Neta', value: '12%', icon: FiPieChart, color: 'text-purple-600', trend: '+0.5%' },
  ];

  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-black text-slate-900 tracking-tight">Gobierno Financiero</h1>
          <p className="text-slate-500">Resumen ejecutivo de salud financiera y liquidez.</p>
        </div>
        <Button className="bg-brand text-white font-black">Exportar Reporte Mensual</Button>
      </div>

      {/* Main Cash Balance */}
      <Card className="bg-slate-900 border-none shadow-2xl overflow-hidden relative">
         <CardContent className="p-12 text-white flex justify-between items-center relative z-10">
            <div>
               <p className="text-xs font-black uppercase tracking-[0.3em] opacity-50 mb-2">Liquidez Total Disponible</p>
               <p className="text-6xl font-black tracking-tighter">
                  ${data ? parseFloat(data.liquidez_disponible).toLocaleString() : '0.00'}
               </p>
               <div className="flex gap-6 mt-6">
                  <div className="flex items-center gap-2">
                     <div className="w-8 h-8 bg-green-500/20 text-green-400 rounded-lg flex items-center justify-center">
                        <FiArrowUpRight />
                     </div>
                     <span className="text-sm font-bold text-slate-400">Ingresos Mes: <span className="text-white">$12.5M</span></span>
                  </div>
                  <div className="flex items-center gap-2">
                     <div className="w-8 h-8 bg-red-500/20 text-red-400 rounded-lg flex items-center justify-center">
                        <FiArrowDownRight />
                     </div>
                     <span className="text-sm font-bold text-slate-400">Gastos Mes: <span className="text-white">$8.2M</span></span>
                  </div>
               </div>
            </div>
            <div className="hidden lg:block text-right">
               <FiDollarSign size={180} className="text-brand opacity-20 -mr-10 -mb-10" />
            </div>
         </CardContent>
         <div className="absolute inset-0 bg-gradient-to-br from-brand/20 to-transparent pointer-events-none" />
      </Card>

      {/* KPI Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
         {kpis.map((kpi) => (
            <Card key={kpi.label} className="border-none shadow-sm bg-white hover:shadow-md transition-all">
               <CardContent className="p-6">
                  <div className="flex justify-between items-start mb-4">
                     <div className={`p-3 rounded-xl bg-slate-50 ${kpi.color}`}>
                        <kpi.icon size={20} />
                     </div>
                     <span className={`text-[10px] font-black px-2 py-1 rounded-full ${kpi.trend.startsWith('+') ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'}`}>
                        {kpi.trend}
                     </span>
                  </div>
                  <p className="text-xs font-bold text-slate-400 uppercase tracking-widest">{kpi.label}</p>
                  <p className="text-2xl font-black text-slate-900 mt-1">{kpi.value}</p>
               </CardContent>
            </Card>
         ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
         <Card className="lg:col-span-2 border-none shadow-sm bg-white">
            <CardHeader>
               <CardTitle>Flujo de Caja Real vs Proyectado</CardTitle>
            </CardHeader>
            <CardContent>
               <div className="h-64 flex items-end justify-between px-4 pb-4">
                  {[40, 65, 45, 80, 55, 90].map((h, i) => (
                     <div key={i} className="w-12 bg-brand/10 rounded-t-lg relative group">
                        <div
                           style={{ height: `${h}%` }}
                           className="absolute bottom-0 left-0 right-0 bg-brand rounded-t-lg group-hover:bg-brand-light transition-all shadow-[0_0_20px_rgba(0,109,91,0.2)]"
                        />
                        <div
                           style={{ height: `${h+10}%` }}
                           className="absolute bottom-0 left-0 right-0 border-t-2 border-dashed border-slate-300 pointer-events-none"
                        />
                     </div>
                  ))}
               </div>
               <div className="flex justify-between px-4 text-[10px] font-black text-slate-400 uppercase mt-4">
                  <span>Ene</span><span>Feb</span><span>Mar</span><span>Abr</span><span>May</span><span>Jun</span>
               </div>
            </CardContent>
         </Card>

         <Card className="border-none shadow-sm bg-white">
            <CardHeader>
               <CardTitle>Alertas de Riesgo</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
               <div className="p-4 bg-red-50 border-l-4 border-red-500 rounded-r-xl">
                  <p className="text-xs font-black text-red-700 uppercase">Liquidez Crítica</p>
                  <p className="text-sm text-red-600 mt-1">El flujo proyectado para el próximo mes está por debajo del margen de seguridad.</p>
               </div>
               <div className="p-4 bg-amber-50 border-l-4 border-amber-500 rounded-r-xl">
                  <p className="text-xs font-black text-amber-700 uppercase">Desviación Presupuesto</p>
                  <p className="text-sm text-amber-600 mt-1">Gasto en 'Marketing Digital' excede el presupuesto trimestral en un 15%.</p>
               </div>
            </CardContent>
         </Card>
      </div>
    </div>
  );
}
